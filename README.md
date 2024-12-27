# Monitor del CanSat

Este proyecto proporciona una interfaz gráfica en Python para visualizar en tiempo real los datos de un CanSat. Los datos pueden provenir de un Arduino conectado con sensores o ser simulados aleatoriamente para pruebas.

## Características

- **Visualización en tiempo real** de temperatura, presión y humedad.
- **Interfaz gráfica interactiva** desarrollada con `tkinter`.
- **Dos modos de funcionamiento**: simulación y lectura de datos desde un Arduino.

---

## Requisitos

### Hardware
- Arduino (con sensores de temperatura, presión y humedad).
- Cable USB para conectar el Arduino al ordenador.

### Software
- **Python 3.x** instalado.
- Bibliotecas requeridas:
  - `tkinter` (incluido con Python).
  - `pyserial` para comunicación serial.

---

## Instalación

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/tu_usuario/monitor-cansat.git
´´´

# Monitor del CanSat

## Uso

### Modo Simulación
1. Ejecuta el script de simulación:  
   `python monitor_cansat_simulacion.py`

2. La interfaz mostrará datos generados aleatoriamente para temperatura, presión y humedad.

### Modo Arduino
1. Conecta tu Arduino al ordenador.
2. Verifica el puerto serial asignado al Arduino.
3. Ejecuta el script para lectura desde Arduino e instala libreria:  
   `python monitor_cansat_serial.py`
   ```bash
   pip install pyserial tk
´´´
4. La interfaz gráfica mostrará los datos enviados por el Arduino.
![monitor](https://github.com/user-attachments/assets/0e21fdb5-95f4-4f5c-bd0b-6dcd1bf6bab0)
---

## Estructura del Proyecto

- **`monitor_cansat_simulacion.py`**: Simula datos para probar la interfaz gráfica.
- **`monitor_cansat_serial.py`**: Lee datos reales del Arduino por el puerto serial y los muestra en la interfaz gráfica.

---

## Ejemplo de Uso en Simulación

El siguiente es un fragmento del código de simulación para ilustrar cómo se generan y visualizan los datos:

import tkinter as tk
from tkinter import ttk
import random

# Función para actualizar los datos simulados
   ```bash
  def update_data():
   temp = round(random.uniform(20, 30), 2)
    pres = round(random.uniform(1000, 1020), 2)
    hum = round(random.uniform(40, 60), 2)
    temp_label.config(text=f"Temperatura: {temp} °C")
    pres_label.config(text=f"Presión: {pres} hPa")
    hum_label.config(text=f"Humedad: {hum} %")
    root.after(1000, update_data)

  # Configuración de la interfaz gráfica
  root = tk.Tk()
  root.title("Monitor del CanSat")
  temp_label = tk.Label(root, text="Temperatura: --- °C")
  temp_label.pack()
  pres_label = tk.Label(root, text="Presión: --- hPa")
  pres_label.pack()
  hum_label = tk.Label(root, text="Humedad: --- %")
  hum_label.pack()

  update_data()
  root.mainloop()
