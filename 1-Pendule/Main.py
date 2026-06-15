from Parametres_Fonctions import *
from scipy.signal import find_peaks

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D






def main(dt, it = None):

    t = np.arange(0, T + 1e-12, dt)

    X_Euler_Simple, Y_Euler_Simple, E_Euler_Simple = Euler(θ_init, ω_init, γ_simple, dt)
    X_Euler_Amorti, Y_Euler_Amorti, E_Euler_Amorti = Euler(θ_init, ω_init, γ_amorti, dt)

    X_RK2_Simple, Y_RK2_Simple, E_RK2_Simple = RungeKutta2(θ_init, ω_init, γ_simple, dt)
    X_RK2_Amorti, Y_RK2_Amorti, E_RK2_Amorti = RungeKutta2(θ_init, ω_init, γ_amorti, dt)

    X_RK4_Simple, Y_RK4_Simple, E_RK4_Simple = RungeKutta4(θ_init, ω_init, γ_simple, dt)
    X_RK4_Amorti, Y_RK4_Amorti, E_RK4_Amorti = RungeKutta4(θ_init, ω_init, γ_amorti, dt)




    peaks_simple, _ = find_peaks(Y_Euler_Simple)
    peaks_simple = np.concatenate(([0], peaks_simple))
    segments_simple = [(peaks_simple[k], peaks_simple[k+1]) for k in range(len(peaks_simple)-1)]
    peaks_amorti, _ = find_peaks(Y_Euler_Amorti)
    peaks_amorti = np.concatenate(([0], peaks_amorti))
    segments_amorti = [(peaks_amorti[k], peaks_amorti[k+1]) for k in range(len(peaks_amorti)-1)]






    fig, axes = plt.subplots(2, 2, figsize = (12, 12))
    ax1, ax2 = axes[0, 0], axes[0, 1]
    ax3, ax4 = axes[1, 0], axes[1, 1]
    plt.suptitle(rf'$[0, T] = [0,${T:.1f}$] \quad \Delta t =$ {dt:.1e}')
    ax1.set_title('Pendule simple' + '\n' + 'cas parfait')
    ax2.set_title('Pendule amorti' + '\n' + 'cas réel')



    Euler_Simple_Pendul, = ax1.plot([], [], **param3)
    Euler_Simple_Trainee, = ax1.plot([], [], **param3bis)

    Euler_Amorti_Pendul, = ax2.plot([], [], **param3)
    Euler_Amorti_Trainee, = ax2.plot([], [], **param3bis)

    Euler_Simple_E, = ax3.plot([], [], **param3ter)
    Euler_Amorti_E, = ax4.plot([], [], **param3ter)




    RK2_Simple_Pendul, = ax1.plot([], [], **param2)
    RK2_Simple_Trainee, = ax1.plot([], [], **param2bis)

    RK2_Amorti_Pendul, = ax2.plot([], [], **param2)
    RK2_Amorti_Trainee, = ax2.plot([], [], **param2bis)

    RK2_Simple_E, = ax3.plot([], [], **param2ter)
    RK2_Amorti_E, = ax4.plot([], [], **param2ter)



    RK4_Simple_Pendul, = ax1.plot([], [], **param1)
    RK4_Simple_Trainee, = ax1.plot([], [], **param1bis)

    RK4_Amorti_Pendul, = ax2.plot([], [], **param1)
    RK4_Amorti_Trainee, = ax2.plot([], [], **param1bis)

    RK4_Simple_E, = ax3.plot([], [], **param1ter)
    RK4_Amorti_E, = ax4.plot([], [], **param1ter)


    for i, ax in enumerate(axes.flatten()):
        if i <= 1 :
            ax.set_xlim(-L * 1.1, L * 1.1)
            ax.set_ylim(-L * 1.1, L * 1.1)
            ax.set_aspect('equal')
        else:
            ax.set_xlim(- 0.1, T + 0.1)
            if i <= 2 :
                ax.set_ylim(np.min(E_RK4_Simple) * (1 - 1e-6), np.max(E_RK4_Simple) * (1 + 1e-5))
            else :
                ax.set_ylim(np.min(E_RK4_Amorti) * 0.95, np.max(E_RK4_Amorti) * 1.05)

        

        ax.grid()
        ax2.legend(fontsize = 8, loc = 'upper center', ncol = 3, handles = [
        Line2D([0], [0], color = param3bis['color'], label = param3bis['label'], lw=2),
        Line2D([0], [0], color = param2bis['color'], label = param2bis['label'], lw=2),
        Line2D([0], [0], color = param1bis['color'], label = param1bis['label'], lw=2),
    ])
    
    


    def update(i):


        j_simple = Trainee(i, segments_simple)
        j_amorti = Trainee(i, segments_amorti)


        # Euler Simple
        Euler_Simple_Pendul.set_data([0, X_Euler_Simple[i]], 
                                    [0, Y_Euler_Simple[i]])
        Euler_Simple_Trainee.set_data(X_Euler_Simple[j_simple : i], 
                                    Y_Euler_Simple[j_simple : i])
        Euler_Simple_E.set_data(t[:i], E_Euler_Simple[:i])

        
        # Euler Amorti
        Euler_Amorti_Pendul.set_data([0, X_Euler_Amorti[i]], 
                                    [0, Y_Euler_Amorti[i]])
        Euler_Amorti_Trainee.set_data(X_Euler_Amorti[j_amorti : i], 
                                    Y_Euler_Amorti[j_amorti : i])
        Euler_Amorti_E.set_data(t[:i], E_Euler_Amorti[:i])



        # RK2 Simple
        RK2_Simple_Pendul.set_data([0, X_RK2_Simple[i]], 
                                    [0, Y_RK2_Simple[i]])
        RK2_Simple_Trainee.set_data(X_RK2_Simple[j_simple : i], 
                                    Y_RK2_Simple[j_simple : i])
        RK2_Simple_E.set_data(t[:i], E_RK2_Simple[:i])


        # RK2 Amorti
        RK2_Amorti_Pendul.set_data([0, X_RK2_Amorti[i]], 
                                    [0, Y_RK2_Amorti[i]])
        RK2_Amorti_Trainee.set_data(X_RK2_Amorti[j_amorti : i], 
                                    Y_RK2_Amorti[j_amorti : i])
        RK2_Amorti_E.set_data(t[:i], E_RK2_Amorti[:i])



        # RK4 Simple
        RK4_Simple_Pendul.set_data([0, X_RK4_Simple[i]], 
                                    [0, Y_RK4_Simple[i]])
        RK4_Simple_Trainee.set_data(X_RK4_Simple[j_simple : i], 
                                    Y_RK4_Simple[j_simple : i])
        RK4_Simple_E.set_data(t[:i], E_RK4_Simple[:i])

        


        # RK4 Amorti
        RK4_Amorti_Pendul.set_data([0, X_RK4_Amorti[i]], 
                                    [0, Y_RK4_Amorti[i]])
        RK4_Amorti_Trainee.set_data(X_RK4_Amorti[j_amorti : i], 
                                    Y_RK4_Amorti[j_amorti : i])
        RK4_Amorti_E.set_data(t[:i], E_RK4_Amorti[:i])



        return (Euler_Simple_Pendul, 
                Euler_Simple_Trainee, 
                Euler_Simple_E,
                Euler_Amorti_Pendul, 
                Euler_Amorti_Trainee,
                Euler_Amorti_E,
                RK2_Simple_Pendul,
                RK2_Simple_Trainee,
                RK2_Simple_E,
                RK2_Amorti_Pendul,
                RK2_Amorti_Trainee,
                RK2_Amorti_E,
                RK4_Simple_Pendul,
                RK4_Simple_Trainee,
                RK4_Simple_E,
                RK4_Amorti_Pendul,
                RK4_Amorti_Trainee,
                RK4_Amorti_E)



    ani = FuncAnimation(
        fig,
        update,
        frames=np.linspace(0, T / dt, int(T) * 30 + 1, dtype=int),
        interval=1e3 / 30,
        blit=True
    )

    name = f"dt={dt :.1e}.gif"
    full_name = f"{it}-" + name if it is not None else name
    ani.save(full_name, writer='pillow', fps=30, dpi = 150)
    plt.close(fig)
    # plt.show()





if __name__ == '__main__' :
    val_dt = [5e-3, 2.5e-3, 1e-3, 1e-4]
    for i, dt in enumerate(val_dt) :
        main(dt, it = i)