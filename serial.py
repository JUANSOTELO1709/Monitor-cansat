import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

class CanSatInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Interfaz CanSat")

        self.canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
        self.canvas.pack(fill=tk.BOTH, expand=True)

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
        self.canvas.create_window(10 + col*200, 10 + row*100, anchor='nw', window=frame)  # Ajusta las posiciones según sea necesario

        label = ttk.Label(frame, text="Valor:")
        label.pack(side="left")

        value = ttk.Label(frame, text="0")
        value.pack(side="left")

    def create_graph_frame(self):
        frame = ttk.LabelFrame(self.root, text="Gráficos en Tiempo Real")
        self.canvas.create_window(10, 300, anchor='nw', window=frame)  # Ajusta la posición según sea necesario

        fig, self.ax = plt.subplots()
        self.canvas_plot = FigureCanvasTkAgg(fig, master=frame)
        self.canvas_plot.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.ax.plot([random.randint(0, 100) for _ in range(10)], label="Muestra")
        self.ax.legend()

        self.update_graph()

    def update_graph(self):
        self.ax.clear()
        self.ax.plot([random.randint(0, 100) for _ in range(10)], label="Muestra")
        self.ax.legend()
        self.canvas_plot.draw()
        self.root.after(1000, self.update_graph)

root = tk.Tk()
app = CanSatInterface(root)
root.mainloop()
