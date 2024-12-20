import pandas as pd
import matplotlib.pyplot as plt

from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

# cargamos la página web a una variable que pandas la pueda utilizar
url: str = 'http://127.0.0.1:8001/'
tablas = pd.read_html(url)
df = tablas[0]

# analizamos info para calcular edad promedio
edad_promedio = df['Edad'].mean()
promedio_edad_ciudad = df.groupby('Ciudad')['Edad'].mean()

# filtro para los mayores de 30 años
mayores_30 = df[df['Edad'] > 30]  # creamos lista analizando la lista original y lo hacemos en una sola línea

# creamos gráfica
plt.figure(figsize=(8, 6))
promedio_edad_ciudad.plot(kind='bar', color='skyblue')
plt.title('Promedio de edades por ciudad')
[plt.text(index, value, str(value), ha='center', va='bottom') for index, value in enumerate(promedio_edad_ciudad)]
plt.xlabel('Ciudad')
plt.ylabel('Edad Promedio')
plt.tight_layout()
plt.savefig('edades.png')
plt.close()

data_users = [['Ciudad', 'Edad Promedio']] + [[ciudad, edad] for ciudad, edad in promedio_edad_ciudad.items()]
tabla_content = Table(data_users)
tabla_content.setStyle(TableStyle(
    [("BACKGROUND", (0, 0), (-1, 0), colors.grey),
     ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
     ("ALIGN", (0, 0), (-1, -1), "CENTER"),
     ("BACKGROUND", (0, 1), (-1, -1), colors.lightblue),
     ("GRID", (0, 0), (-1, -1), 1, colors.black)]
))

# creamos pdf
pdf_path = 'resultados_edades_ciudad.pdf'
c = canvas.Canvas(pdf_path, pagesize=letter)
c.setFont('Helvetica-Bold', 16)
c.drawString(30, 750, "Análisis de Edad")

c.setFont('Helvetica', 10)
c.drawString(30, 730, 'Análisis de edad de usuario por ciudad')
c.drawString(30, 715, f'Edad promedio: {edad_promedio}')

tabla_content.wrapOn(c, 300, 500)
tabla_content.drawOn(c, 300, 500)

c.drawImage('edades.png', 50, 400, width=250, height=200)
c.save()
print('Pdf generado')
