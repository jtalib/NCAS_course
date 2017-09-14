''' script which will calculate the total variation diminishing scheme'''

def calculate_streamfunction(phi,nx):
    streamfunction = phi.copy()
    for j in xrange(1,nx):
        if (phi[j+1]-phi[j]) != 0.0:
            streamfunction[j] = (phi[j]-phi[j-1])/(phi[j+1]-phi[j])
        else:
            streamfunction[j] = 1.0
    if (phi[0]-phi[nx]) != 0.0:
        streamfunction[nx] = (phi[nx]-phi[nx-1])/(phi[0]-phi[nx])
    else:
        streamfunction[nx] = 1.0
    streamfunction[0] = streamfunction[nx]
    return streamfunction
    
def calculate_theta_high_low(phi,courant):
    theta_high = phi.copy()
    theta_low = phi.copy()
    # work out theta high
    for j in xrange(1,nx):
        theta_high[j] = (0.5*(1.+courant)*phi[j])+(0.5*(1.-courant)*phi[j+1])
    theta_high[nx] = (0.5*(1.+courant)*phi[nx])+(0.5*(1.-courant)*phi[0])
    theta_high[0] = theta_high[nx]
    # work out theta low
    u = (courant*dx)/dt
    for j in xrange(1,nx):
        if u >= 0.0:
            theta_low[j] = phi[j]
        else:
            theta_low[j] = phi[j+1]
    # work out theta low at the boundaries.
    if u >= 0.0:
        theta_low[0] = phi[0]
        theta_low[nx] = theta_low[0]
    else:
        theta_low[0] = phi[1]
        theta_low[nx] = theta_low[0]
    return theta_high, theta_low
    
def new_Phi_function(phi,phi_half,courant):
    phi_New = phi.copy()
    for j in xrange(1,nx):
        phi_New[j] = -courant*(phi_half[j]-phi_half[j-1]) + phi[j]
    phi_New[0] = -courant*(phi_half[0]-phi_half[nx-1]) + phi[0]
    phi_New[nx] = phi_New[0]
    return phi_New
    
def TVD_scheme(phi,courant):
    nt = total_nt/dt
    print (nt)
    for t in xrange(0,nt):
        # work out streamfunction
        streamfunction = calculate_streamfunction(phi,nx)
        # work out theta_high and theta_low
        theta_high, theta_low = calculate_theta_high_low(phi,courant)
        # work out phi_half
        phi_half = (streamfunction*theta_high)+\
                        (1-streamfunction)*theta_low
        phi_New = new_Phi_function(phi,phi_half,courant)
        phi = phi_New.copy()
    return phi_New,phi
    
def warming_beam_phi_half(phi,courant):
    phi_half = phi.copy()
    for j in xrange(1,nx):
        phi_half[j] = (0.5*(3.-courant)*phi[j]) - (0.5*(1-courant)*phi[j-1])
    phi_half[0] = (0.5*(3.-courant)*phi[0]) - (0.5*(1-courant)*phi[nx])
    phi_half[nx] = phi_half[0]
    return phi_half
    
def warming_beam(phi,courant):
    nt = total_nt/dt
    print (nt)
    phi_New = phi.copy()
    for t in xrange(0,nt):
        phi_half = warming_beam_phi_half(phi,courant)
        for j in xrange(1,nx):
            phi_New[j] = -courant*(phi_half[j]-phi_half[j-1]) + phi[j]
        phi_New[0] = -courant*(phi_half[0]-phi_half[nx-1]) + phi[0]
        phi_New[nx] = phi_New[0]
        phi = phi_New.copy()
    return phi_New
    
def lax_wendroff_phi_half(phi,courant):
    phi_half = phi.copy()
    for j in xrange(1,nx):
        phi_half[j] = (0.5*(1.+courant)*phi[j]) + (0.5*(1-courant)*phi[j+1])
    phi_half[0] = (0.5*(1.+courant)*phi[0]) + (0.5*(1-courant)*phi[1])
    phi_half[nx] = phi_half[0]
    return phi_half
    
def lax_wendroff(phi,courant):
    nt = total_nt/dt
    print (nt)
    phi_New = phi.copy()
    for t in xrange(0,nt):
        phi_half = lax_wendroff_phi_half(phi,courant)
        for j in xrange(1,nx):
            phi_New[j] = -courant*(phi_half[j]-phi_half[j-1]) + phi[j]
        phi_New[0] = -courant*(phi_half[0]-phi_half[nx-1]) + phi[0]
        phi_New[nx] = phi_New[0]
        phi = phi_New.copy()
    return phi_New
    
    
        
    
