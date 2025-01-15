import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

class CanSatInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Interfaz CanSat")

        # Crear los cuadros para los parámetros
        self.create_param_frame("Presión (hPa)", 0, 0)
        self.create_param_frame("Temperatura (°C)", 1, 0)
        self.create_param_frame("Velocidad (m/s)", 0, 1)
        self.create_param_frame("Aceleración (m/s²)", 1, 1)
        self.create_param_frame("CO₂ (ppm)", 2, 0)

        # Crear la sección de gráficos
        self.create_graph_frame()

    def create_param_frame(self, param_name, row, col):
        frame = ttk.LabelFrame(self.root, text=param_name)
        frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        label = ttk.Label(frame, text="Valor:")
        label.pack(side="left")

        value = ttk.Label(frame, text="0")
        value.pack(side="left")

    def create_graph_frame(self):
        frame = ttk.LabelFrame(self.root, text="Gráficos en Tiempo Real")
        frame.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky="nsew")

        fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(fig, master=frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.ax.plot([random.randint(0, 100) for _ in range(10)], label="Muestra")
        self.ax.legend()

        self.update_graph()

    def update_graph(self):
        self.ax.clear()
        self.ax.plot([random.randint(0, 100) for _ in range(10)], label="Muestra")
        self.ax.legend()
        self.canvas.draw()
        self.root.after(1000, self.update_graph)

root = tk.Tk()
app = CanSatInterface(root)
root.mainloop()
