import serial
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Configurar puerto serial
arduino = serial.Serial('COM3', 9600, timeout=1)  # Ajusta el puerto correcto

# Constantes
P0 = 1013.25  # Presión a nivel del mar (hPa)
T0 = 288.15   # Temperatura de referencia en Kelvin (15 °C)
L = 0.0065    # Gradiente térmico (K/m)
g = 9.80665   # Gravedad (m/s²)
R = 8.314     # Constante de gases (J/mol·K)
M = 0.0289644 # Masa molar del aire (kg/mol)



# Listas para almacenar datos
alturas_ascenso, temperaturas_ascenso, presiones_ascenso, velocidades_ascenso = [], [], [], []
alturas_descenso, temperaturas_descenso, presiones_descenso, velocidades_descenso = [], [], [], []
ultima_presion = None



# Configuración de la figura con tres subgráficos
fig, ax = plt.subplots(2, 2, figsize=(15, 15))

# Asignar cada subplot correctamente
ax1 = ax[0, 0]  # Primera fila, primera columna
ax2 = ax[0, 1]  # Primera fila, segunda columna
ax3 = ax[1, 0]  # Segunda fila, primera columna
ax4 = ax[1, 1]  # Segunda fila, segunda columna



# Función para actualizar la gráfica
def actualizar(frame):
    global ultima_presion

    try:
        datos = arduino.readline().decode().strip()
        if datos:
            valores = datos.split(',')
            if len(valores) >= 3:  # Ahora hay 3 valores: Temp, Presión, Velocidad
                temp = float(valores[0])
                presion = float(valores[1])
                velocidad = float(valores[2])  


                # Calcular altura con ecuación barométrica
                altura = (T0 / L) * (1 - (presion / P0) ** 0.1903)


                # Convertir temperatura a Kelvin
                temp_K = temp + 273.15


                # Determinar ascenso o descenso
                if ultima_presion is not None:
                    if presion < ultima_presion:  # Ascenso
                        temperaturas_ascenso.append(temp_K)
                        alturas_ascenso.append(altura)
                        presiones_ascenso.append(presion)
                        velocidades_ascenso.append(velocidad)

                    else:  # Descenso
                        temperaturas_descenso.append(temp_K)
                        alturas_descenso.append(altura)
                        presiones_descenso.append(presion)
                        velocidades_descenso.append(velocidad)


                ultima_presion = presion


                # Calcular desviaciones estándar
                std_temp_ascenso = min(np.std(temperaturas_ascenso), 0.3) if len(temperaturas_ascenso) > 1 else 0.1
                std_temp_descenso = min(np.std(temperaturas_descenso), 0.3) if len(temperaturas_descenso) > 1 else 0.1
                std_altura_ascenso = min(np.std(alturas_ascenso), 20) if len(alturas_ascenso) > 1 else 1
                std_altura_descenso = min(np.std(alturas_descenso), 20) if len(alturas_descenso) > 1 else 1
                std_presion_ascenso = min(np.std(presiones_ascenso), 2) if len(presiones_ascenso) > 1 else 0.5
                std_presion_descenso = min(np.std(presiones_descenso), 2) if len(presiones_descenso) > 1 else 0.5
                std_velocidad_ascenso = min(np.std(velocidades_ascenso), 1) if len(velocidades_ascenso) > 1 else 0.2
                std_velocidad_descenso = min(np.std(velocidades_descenso), 1) if len(velocidades_descenso) > 1 else 0.2


                # Graficar Altura vs Temperatura
                ax1.clear()
                ax1.set_xlabel('Temperatura [K]', fontsize=12)
                ax1.set_ylabel('Altura [m]', fontsize=12)
                ax1.grid(True)
                ax1.set_title('Altura vs Temperatura con Desviación Estándar', fontsize=14)
                if temperaturas_ascenso:
                    ax1.errorbar(temperaturas_ascenso, alturas_ascenso, xerr=std_temp_ascenso, yerr=std_altura_ascenso, fmt='g--o', capsize=5, label='Ascenso')
                if temperaturas_descenso:
                    ax1.errorbar(temperaturas_descenso, alturas_descenso, xerr=std_temp_descenso, yerr=std_altura_descenso, fmt='r--v', capsize=5, label='Descenso')
                ax1.legend()


                # Graficar Altura vs Presión
                ax2.clear()
                ax2.set_xlabel('Presión [hPa]', fontsize=12)
                ax2.set_ylabel('Altura [m]', fontsize=12)
                ax2.grid(True)
                ax2.set_title('Altura vs Presión con Desviación Estándar', fontsize=14)
                if presiones_ascenso:
                    ax2.errorbar(presiones_ascenso, alturas_ascenso, xerr=std_presion_ascenso, yerr=std_altura_ascenso, fmt='b--o', capsize=5, label='Ascenso')
                if presiones_descenso:
                    ax2.errorbar(presiones_descenso, alturas_descenso, xerr=std_presion_descenso, yerr=std_altura_descenso, fmt='y--v', capsize=5, label='Descenso')
                ax2.legend()


                # Graficar Altura vs Velocidad (NUEVA GRÁFICA)
                ax3.clear()
                ax3.set_xlabel('Velocidad [m/s]', fontsize=12)
                ax3.set_ylabel('Altura [m]', fontsize=12)
                ax3.grid(True)
                ax3.set_title('Altura vs Velocidad con Desviación Estándar', fontsize=14)
                if velocidades_ascenso:
                    ax3.errorbar(velocidades_ascenso, alturas_ascenso, xerr=std_velocidad_ascenso, yerr=std_altura_ascenso, fmt='c--o', capsize=5, label='Ascenso')
                if velocidades_descenso:
                    ax3.errorbar(velocidades_descenso, alturas_descenso, xerr=std_velocidad_descenso, yerr=std_altura_descenso, fmt='m--v', capsize=5, label='Descenso')
                ax3.legend()

    except Exception as e:
        print("Error:", e)

# Animación en tiempo real
ani = FuncAnimation(fig, actualizar, interval=500)
plt.show()
