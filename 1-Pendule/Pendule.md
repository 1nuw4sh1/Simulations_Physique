# Pendule

Soit un pendule attaché à fil rigide avec les données et paramètres initaux suivants :
- Accélération Pesanteur : $\quad g = 9.81$
- Masse : $\quad m = 1$
- Longueur : $\quad L = 1$
- Coefficient d'amortissement : $\quad \gamma \geq 0$
- Angle : $\quad \theta_0 =  \frac{2 \pi}{3} \quad$ (relatif à la verticale)
- Vitesse Angulaire : $\quad \omega_0 = \theta_t(t=0) = 0$

Considérons, pour ce problème, les équations suivantes :
- Moment cinétique : $\quad \theta_{tt} = - \gamma \theta_t - \frac{g}{L} sin(\theta)$
- Energie : $\quad E = E_c + E_p = \frac{1}{2} \omega^2 L^2 + g L (1 - cos(\theta))$

Trois schémas temporels (explicites) ont été implémenté :
- Euler : $o(\Delta t)$
- Runge-Kutta 2 : $o(\Delta t^2)$
- Runge-Kutta 4 : $o(\Delta t^4) \quad$ (choisis comme référence) 
