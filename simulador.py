import tkinter as tk
from tkinter import ttk
import random

# Función para actualizar los datos simulados
def update_data():
    temp_data = round(random.uniform(20, 30), 2)  # Simular datos de temperatura
    pres_data = round(random.uniform(1000, 1020), 2)  # Simular datos de presión
    hum_data = round(random.uniform(40, 60), 2)  # Simular datos de humedad
    alt_data = round(random.uniform(100, 500), 2)  # Simular datos de altura

    temp_label.config(text=f"Temperatura: {temp_data} °C")
    pres_label.config(text=f"Presión: {pres_data} hPa")
    hum_label.config(text=f"Humedad: {hum_data} %")
    alt_label.config(text=f"Altura: {alt_data} m")
    alt_scale.set(1000 - alt_data)  # Invertir los valores para que 0 esté en la parte inferior

    root.after(1000, update_data)  # Actualizar cada segundo

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Datos del CanSat")
root.geometry("450x450")
root.configure(bg="#e6e6fa")  # Color de fondo morado claro (lavanda)

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

alt_label = ttk.Label(frame1, text="Altura: --- m")
alt_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")

alt_scale = ttk.Scale(frame1, from_=1000, to=0, orient="vertical", length=200)
alt_scale.grid(row=1, column=1, rowspan=4, padx=10, pady=10)

# Iniciar la actualización de datos simulados
update_data()

root.mainloop()
