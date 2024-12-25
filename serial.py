import tkinter as tk
from tkinter import ttk
import serial

# Configuración del puerto serie
arduino_port = 'COM3'  # Reemplaza con tu puerto COM
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate)

# Función para actualizar los datos desde Arduino
def update_data():
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        data = line.split(',')
        if len(data) == 3:
            temp_data = data[0].split(':')[1]
            pres_data = data[1].split(':')[1]
            hum_data = data[2].split(':')[1]
            temp_label.config(text=f"Temperatura: {temp_data} °C")
            pres_label.config(text=f"Presión: {pres_data} hPa")
            hum_label.config(text=f"Humedad: {hum_data} %")
    root.after(1000, update_data)  # Actualizar cada segundo

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Datos del CanSat")
root.geometry("450x350")
root.configure(bg="#e6e6fa")  # Color de fondo morado claro

# Estilo personalizado
style = ttk.Style()
style.configure("TFrame", background="#e6e6fa")
style.configure("TLabel", background="#e6e6fa", font=("Helvetica", 14))
style.configure("Title.TLabel", font=("Helvetica", 18, "bold"))

# Crear Frame principal
frame1 = ttk.Frame(root, padding="20", style="TFrame")
frame1.pack(fill=tk.BOTH, expand=True)

# Título
title_label = ttk.Label(frame1, text="Monitor del CanSat", style="Title.TLabel")
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Agregar Widgets
temp_label = ttk.Label(frame1, text="Temperatura: --- °C")
temp_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

pres_label = ttk.Label(frame1, text="Presión: --- hPa")
pres_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

hum_label = ttk.Label(frame1, text="Humedad: --- %")
hum_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

# Iniciar la actualización de datos desde el puerto serie
update_data()

root.mainloop()
