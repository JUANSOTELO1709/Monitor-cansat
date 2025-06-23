# 📡 Visualización en Tiempo Real de Altura, Temperatura, Presión y Velocidad

Este proyecto de Python permite visualizar en tiempo real los datos enviados por un microcontrolador (como Arduino) a través del puerto serial. Se procesan los datos para calcular la **altura atmosférica** utilizando la **ecuación barométrica**, y se grafican relaciones entre altura, temperatura, presión y velocidad.

## 🔧 Requisitos

- Python 3.x
- Arduino (u otro microcontrolador) que envíe datos por serial en formato:  
  `temperatura (°C),presion (hPa),velocidad (m/s)`
- Librerías de Python:

   ⚙️ Hardware esperado
   El Arduino debe estar conectado a sensores que puedan medir:

    Temperatura del aire

    Presión atmosférica

    Velocidad de ascenso/descenso (estimada por GPS o barómetro)

## 📈 ¿Qué grafica el programa?

Se generan 3 gráficos en tiempo real con barras de error para cada eje:

- 📊 Altura vs Temperatura (K)
- 📊 Altura vs Presión (hPa)
- 📊 Altura vs Velocidad (m/s)

> Se distinguen los datos durante el **ascenso** (↓ presión) y el **descenso** (↑ presión).

## 🧠 Principales ecuaciones y constantes

**Altura calculada mediante la ecuación barométrica:**

\[
h = \frac{T_0}{L} \left(1 - \left(\frac{P}{P_0}\right)^{0.1903} \right)
\]

**Constantes utilizadas:**

| Constante | Valor             | Significado                       |
|-----------|-------------------|-----------------------------------|
| `P0`      | 1013.25 hPa       | Presión al nivel del mar          |
| `T0`      | 288.15 K          | Temperatura de referencia         |
| `L`       | 0.0065 K/m        | Gradiente térmico                 |
| `g`       | 9.80665 m/s²      | Gravedad                          |
| `R`       | 8.314 J/mol·K     | Constante universal de los gases |
| `M`       | 0.0289644 kg/mol  | Masa molar del aire              |
| `g0`      | 9.80665 m/s²      | Gravedad
## 🔄 Funcionamiento del código

- Lee los datos del puerto serial (`COM3` por defecto).
- Divide los datos en **temperatura**, **presión** y **velocidad**.
- Calcula la **altura** usando la ecuación barométrica.
- Determina si el objeto está en **ascenso** o **descenso** según la variación de presión.
- Actualiza tres gráficas en tiempo real diferenciando ascenso y descenso con barras de error:

  - 📈 Altura vs Temperatura
  - 📈 Altura vs Presión
  - 📈 Altura vs Velocidad

## 🖼️ Ejemplo de formato de datos esperado desde Arduino

```plaintext
25.0,1005.6,3.1
24.7,1003.2,3.3
24.4,1001.1,3.6
```


## 🚀 Cómo ejecutar

1. Asegúrate de conectar tu Arduino y que el puerto serial esté configurado correctamente en el código (`COM3` por defecto).
2. Ejecuta el script en tu entorno de desarrollo con el siguiente comando:

   ```bash
   python graficador_altura.py
```

Autor: Juan David Sotelo