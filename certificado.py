from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import pandas as pd
import os

# Cargar base de datos
try:
    df = pd.read_excel("datos/datos_consolidados.xlsx")
except FileNotFoundError:
    print("Error: No se encontró el archivo 'datos/datos_consolidadosp.xlsx'. Verifica la ruta.")
    exit()

# Imagen de fondo
fondo_certificado = "datos/logos/fondo1.png"
if not os.path.exists(fondo_certificado):
    print(f"Error: No se encontró la imagen de fondo '{fondo_certificado}'. Verifica la ruta.")
    exit()

# Crear carpeta Certificados
output_folder = "Constancia"
os.makedirs(output_folder, exist_ok=True)

# Crear carpeta para estudiantes sin identificación
output_folder_sin_id = "Estudiantes_Sin_Identificacion"
os.makedirs(output_folder_sin_id, exist_ok=True)

# Fuente
fuente_titulo = "Helvetica-Bold"
fuente_texto = "Helvetica"

# Estudiantes sin identificación
estudiantes_sin_id = []

# Procesar datos
estudiantes = df.groupby('Nombre')

for nombre, registros in estudiantes:
    identificacion = registros['Identificación'].iloc[0]

    if pd.isna(identificacion):
        estudiantes_sin_id.append(registros.iloc[0])
        continue

    identificacion = str(int(identificacion)) if pd.notna(identificacion) else ""

    periodos = registros['Periodo'].unique()
    periodos_str = ", ".join(sorted([str(p) for p in periodos]))
    cantidad_periodos = len(periodos)

    # Primer semillero del primer periodo registrado
    registros_sorted = registros.sort_values(by=['Periodo'])
    semillero = registros_sorted.iloc[0]['Semillero']

    nombre_archivo_seguro = "".join(c for c in nombre.replace(' ', '_') if c.isalnum() or c in ('_', '-'))
    nombre_archivo = f"{output_folder}/Constancia_{nombre_archivo_seguro}.pdf"

    c = canvas.Canvas(nombre_archivo, pagesize=landscape(A4))
    ancho, alto = landscape(A4)

    c.drawImage(ImageReader(fondo_certificado), 0, 0, width=ancho, height=alto, preserveAspectRatio=True, anchor='c')

    y_pos = alto - 150

    c.setFont(fuente_titulo, 30)
    c.drawCentredString(ancho / 2, y_pos, "CONSTANCIA DE PARTICIPACIÓN")
    y_pos -= 30
    c.drawCentredString(ancho / 2, y_pos, "EN SEMILLERO DE INVESTIGACIÓN")
    y_pos -= 40

    c.setFont(fuente_texto, 16)
    c.drawCentredString(ancho / 2, y_pos, "La Facultad de Ingeniería Industrial Seccional Villavicencio hace constar que el estudiante:")
    y_pos -= 40

    c.setFont(fuente_titulo, 20)
    c.drawCentredString(ancho / 2, y_pos, nombre)
    y_pos -= 30

    c.setFont(fuente_texto, 16)
    c.drawCentredString(ancho / 2, y_pos, f"Con Identificación: {identificacion}")
    y_pos -= 40

    periodo_palabra = "periodo" if cantidad_periodos == 1 else "periodos"

    texto_participacion_1 = f"Participó en el semillero "
    texto_participacion_2 = f"{semillero}"
    texto_participacion_3 = f" durante {cantidad_periodos} {periodo_palabra}: {periodos_str},"

    text_width_1 = c.stringWidth(texto_participacion_1, fuente_texto, 16)
    text_width_2 = c.stringWidth(texto_participacion_2, fuente_titulo, 16)
    text_width_3 = c.stringWidth(texto_participacion_3, fuente_texto, 16)

    total_width = text_width_1 + text_width_2 + text_width_3
    x_start = (ancho - total_width) / 2

    c.setFont(fuente_texto, 16)
    c.drawString(x_start, y_pos, texto_participacion_1)
    c.setFont(fuente_titulo, 16)
    c.drawString(x_start + text_width_1, y_pos, texto_participacion_2)
    c.setFont(fuente_texto, 16)
    c.drawString(x_start + text_width_1 + text_width_2, y_pos, texto_participacion_3)

    y_pos -= 25
    c.drawCentredString(ancho / 2, y_pos, "demostrando compromiso y excelencia académica.")
    y_pos -= 60

    c.setFont(fuente_texto, 14)
    c.drawCentredString(ancho / 2, y_pos, "El certificado es otorgado el día 01 de abril de 2025")

    firma_y = 95
    c.drawCentredString(ancho / 2, firma_y + 20, "______________________________")
    c.setFont(fuente_titulo, 14)
    c.drawCentredString(ancho / 2, firma_y, "VÍCTOR ANDRÉS RINCÓN GONZÁLEZ")
    c.setFont(fuente_texto, 14)
    c.drawCentredString(ancho / 2, firma_y - 20, "Decano de la Facultad de Ingeniería Industrial")

    c.save()
    print(f"Certificado generado: {nombre_archivo}")

# Exportar estudiantes sin identificación
if estudiantes_sin_id:
    df_sin_id = pd.DataFrame(estudiantes_sin_id)
    df_sin_id.to_excel(f"{output_folder_sin_id}/Estudiantes_Sin_Identificacion.xlsx", index=False)
    print("Archivo Excel generado con estudiantes sin identificación.")

print("Generación de certificados completada.")
