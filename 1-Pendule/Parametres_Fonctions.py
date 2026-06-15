import numpy as np





# === Paramètres === #

g = 9.81

L = 1.
T = 10.

γ_simple = 0.0
γ_amorti = 0.25

θ_init = 2 * np.pi / 3
ω_init = 0.0





def Equations(θ, ω, γ):
    dθ = ω
    dω = - g / L * np.sin(θ) - γ * ω
    return dθ, dω

def MAJ(θ, ω, dθ, dω, dt):
    θ_new = θ + dθ * dt
    ω_new = ω + dω * dt
    return θ_new, ω_new

def Coord_Cartesien(θ):
    x = L*np.sin(θ)
    y = -L*np.cos(θ)
    return x, y

def Energies(θ, ω):
    Ec = 0.5 * L**2 * ω**2
    Ep = g * L * (1 - np.cos(θ))
    E = Ec + Ep
    return E





def Euler(θ_init, ω_init, γ, dt):

    t = 0
    θ, ω = θ_init, ω_init
    x, y = Coord_Cartesien(θ)
    X, Y, E = [x], [y], [Energies(θ, ω)]

    while t <= T :

        dθ, dω = Equations(θ, ω, γ)
        θ, ω = MAJ(θ, ω, dθ, dω, dt)

        x, y = Coord_Cartesien(θ)

        X.append(x)
        Y.append(y)
        E.append(Energies(θ, ω))     

        t += dt

    return X, Y, E






def RungeKutta2(θ_init, ω_init, γ, dt):

    t = 0
    θ, ω = θ_init, ω_init
    x, y = Coord_Cartesien(θ)
    X, Y, E = [x], [y], [Energies(θ, ω)]


    while t <= T :

        # k1
        dθ_mid, dω_mid = Equations(θ, ω, γ)
        θ_mid, ω_mid = MAJ(θ, ω, 0.5 * dθ_mid, 0.5 * dω_mid, dt)

        # k2
        dθ, dω = Equations(θ_mid, ω_mid, γ)
        θ, ω = MAJ(θ, ω, dθ, dω, dt)

        x, y = Coord_Cartesien(θ)
        
        X.append(x)
        Y.append(y)
        E.append(Energies(θ, ω))  

        t += dt

    return X, Y, E





def RungeKutta4(θ_init, ω_init, γ, dt):

    t = 0
    θ, ω = θ_init, ω_init
    x, y = Coord_Cartesien(θ)
    X, Y, E = [x], [y], [Energies(θ, ω)]

    while t <= T :

        # k1
        dθ_quart, dω_quart = Equations(θ, ω, γ)
        θ_quart, ω_quart = MAJ(θ, ω, 0.5 * dθ_quart, 0.5 * dω_quart, dt)

        # k2
        dθ_mid, dω_mid = Equations(θ_quart, ω_quart, γ)
        θ_mid, ω_mid = MAJ(θ, ω, 0.5 * dθ_mid, 0.5 * dω_mid, dt)

        # k3
        dθ_3quart, dω_3quart = Equations(θ_mid, ω_mid, γ)
        θ_3quart, ω_3quart = MAJ(θ, ω, dθ_3quart, dω_3quart, dt)

        # k4
        dθ, dω = Equations(θ_3quart, ω_3quart, γ)
        θ, ω = MAJ(θ, ω, 
                   (dθ_quart + 2 * dθ_mid + 2 * dθ_3quart + dθ) / 6, 
                   (dω_quart + 2 * dω_mid + 2 * dω_3quart + dω) / 6,
                   dt)

        x, y = Coord_Cartesien(θ)
        
        X.append(x)
        Y.append(y)
        E.append(Energies(θ, ω))  

        t += dt

    return X, Y, E










param1 = {'linestyle' : '-', 
          'linewidth' : 3, 
          'marker' : 'o', 
          'markersize' : 10, 
          'color' : 'black', 
          'zorder' : 5}

param2 = {'linestyle' : '-', 
          'linewidth' : 3, 
          'marker' : 'o', 
          'markersize' : 10, 
          'color' : 'black', 
          'zorder' : 5}

param3 = {'linestyle' : '-', 
          'linewidth' : 3, 
          'marker' : 'o', 
          'markersize' : 10, 
          'color' : 'black', 
          'zorder' : 5}



param1bis = {'linestyle' : '-', 
             'linewidth' : 10, 
             'color' : 'red', 
             'zorder' : 1, 
             'label' : 'Runge-Kutta 4'}

param2bis = {'linestyle' : '-', 
             'linewidth' : 6, 
             'color' : 'cyan', 
             'zorder' : 2, 
             'label' : 'Runge-Kutta 2'}

param3bis = {'linestyle' : '-', 
             'linewidth' : 2, 
             'color' : 'blue', 
             'zorder' : 3, 
             'label' : 'Euler'}



param1ter = {'linestyle' : '-', 
             'linewidth' : 6, 
             'color' : 'red', 
             'zorder' : 1, 
             'label' : 'Runge-Kutta 4'}

param2ter = {'linestyle' : '-', 
             'linewidth' : 4, 
             'color' : 'cyan', 
             'zorder' : 2, 
             'label' : 'Runge-Kutta 2'}

param3ter = {'linestyle' : '-', 
             'linewidth' : 2, 
             'color' : 'blue', 
             'zorder' : 3, 
             'label' : 'Euler'}








def Trainee(i, segment):
    
    S1 = segment[:-1]
    S2 = segment[1:]

    for s1, s2 in zip(S1, S2):
        start, end = s1[0], s2[1]
        if (i >= start) & (i < end) :
            return start
    return s1[1]