import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parámetros de entrada
R1 = float(input("Ingrese el valor de R1 (ohms): "))
R2 = float(input("Ingrese el valor de R2 (ohms): "))
R3 = float(input("Ingrese el valor de R3 (ohms): "))
Vg = float(input("Ingrese el valor de Vg (voltios): "))
Vs = float(input("Ingrese el valor de Vs (voltios): "))
P_max = input("Ingrese la potencia máxima (0.25_W, 0.50_W, 1.00_W, 2.00_W): ")

# Cálculo de corrientes y potencias
Ig = Vg / R1
Is = Vs / R2
I_center = (Vg - Vs) / R3

P_max_values = {'0.25_W': 0.25, '0.50_W': 0.5, '1.00_W': 1, '2.00_W': 2}
P_max_R1 = P_max_values[P_max]
P_max_R2 = P_max_values[P_max]
P_max_R3 = P_max_values[P_max]

# Verificación de potencias máximas
if R1 > P_max_R1 or R2 > P_max_R2 or R3 > P_max_R3:
    print("Advertencia: Una o más resistencias exceden la potencia máxima.")

# Función de animación
def animate(frame):
    ax.clear()

    # Dibujar resistencias
    ax.plot([1, 1], [0, 1], 'k-', linewidth=2)  # R1
    ax.plot([2, 2], [0, 1], 'k-', linewidth=2)  # R2
    ax.plot([1, 2], [0.5, 0.5], 'k-', linewidth=2)  # R3

    # Dibujar fuentes
    ax.text(0.5, 1.1, f'Vg\n{Vg}V', ha='center', va='center', fontsize=10)
    ax.text(2.5, 1.1, f'Vs\n{Vs}V', ha='center', va='center', fontsize=10)

    # Dibujar corriente en R1
    ax.arrow(0.8, 0.75, 0.2, 0, head_width=0.05, head_length=0.05, fc='blue', ec='blue')
    
    # Dibujar corriente en R2
    ax.arrow(2.2, 0.75, 0.2, 0, head_width=0.05, head_length=0.05, fc='red', ec='red')

    # Dibujar corriente en R3
    ax.arrow(1.5, 0.45, 0, -0.2, head_width=0.05, head_length=0.05, fc='green', ec='green')

    # Configuraciones adicionales
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 1.5)
    ax.set_title(f'Frame {frame}')
    ax.set_xlabel('Componentes del Circuito')
    ax.set_ylabel('Dirección de Corriente')

# Configuración de la animación
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, animate, frames=100, interval=100, blit=False)
plt.show()