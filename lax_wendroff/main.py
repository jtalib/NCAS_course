execfile('../burger_equation/initial.py')
execfile('TVD.py')
import matplotlib.pyplot as plt

if __name__ == "__main__":
    courant =0.8
    nx,dt,dx,total_nt,x = initial_constants(100,1,100)
    curve = initial_square(x)
    phi_TVD, new_Phi = TVD_scheme(curve,courant)
    phi_lax_wendroff = lax_wendroff(curve,courant)
    phi_warming_beam = warming_beam(curve,courant)
    
    u = (courant*dx)/dt
    plt.plot(x,initial_square(x-u*total_nt),'r',label='Analytical')
    plt.plot(x,phi_TVD,'b',label='TVD')
    plt.plot(x,phi_lax_wendroff,'g',label='Lax Wendroff')
    plt.plot(x,phi_warming_beam,'k',label='Warming & Beam')
    #plt.ylim([-0.1,1.1])
    plt.legend(fontsize=8.0)
    plt.title('Courant Number = '+str(courant)+', nx = '+str(nx)+', dt = '+str(dt)+',\n dx = '+str(dx)+', total time = '+str(total_nt))

    plt.savefig('square_100time.jpg')
    plt.close()
    
    
