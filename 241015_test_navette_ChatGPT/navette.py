import numpy as np
import matplotlib.pyplot as plt

# Paramètres de la navette
vitesse_initiale = 50 # en m/s
angle_de_atterrissage = 30 # en degrés
g = 9.81 # Accélération due à la gravité en m/s^2

# Conversion de l'angle en radians
angle_rad = np.radians(angle_de_atterrissage)

# Calcul des composantes de la vitesse
vitesse_x = vitesse_initiale * np.cos(angle_rad)
vitesse_y = vitesse_initiale * np.sin(angle_rad)

# Temps de vol
temps_vol = (2 * vitesse_y) / g

# Création des points de temps
t = np.linspace(0, temps_vol, num=100)

# Calcul des positions
x = vitesse_x * t
y = vitesse_y * t - 0.5 * g * t**2

# Tracé de la trajectoire
plt.figure(figsize=(10, 5))
plt.plot(x, y)
plt.title("Trajectoire d'atterrissage de la navette")
plt.xlabel("Distance (m)")
plt.ylabel("Hauteur (m)")
plt.axhline(0, color='black', lw=0.5, ls='--') # Ligne de sol
plt.grid()
plt.xlim(0, max(x))
plt.ylim(0, max(y) * 1.1)
plt.show()