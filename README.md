# Certificados Semilleros USTA - Facultad de Ingeniería Industrial, Villavicencio

Este proyecto automatiza la generación de constancias de participación en formato PDF para los estudiantes de los semilleros de investigación de la Facultad de Ingeniería Industrial de la Universidad Santo Tomás, Seccional Villavicencio.

## Descripción General

El script principal `certificado.py` lee los datos de participación de los estudiantes desde un archivo Excel consolidado (`datos/datos_consolidados.xlsx`), procesa la información de cada estudiante (nombre, identificación, semillero, y periodos de participación), y genera una constancia individual en formato PDF utilizando una plantilla de fondo. Adicionalmente, identifica y reporta a los estudiantes para quienes no se pudo generar una constancia por falta del número de identificación.

## Características Principales

* **Generación masiva de PDFs:** Crea constancias individuales para múltiples estudiantes.
* **Consolidación de periodos:** Agrupa todos los periodos de participación de un estudiante en una única constancia.
* **Uso de plantilla:** Aplica una imagen de fondo estándar (`datos/logos/fondo1.png`) para todas las constancias.
* **Manejo de estudiantes sin identificación:** Genera un listado en Excel (`Estudiantes_Sin_Identificacion/Estudiantes_Sin_Identificacion.xlsx`) con los estudiantes que no tienen un número de identificación en el archivo de datos.
* **Nomenclatura de archivos:** Guarda las constancias con un nombre estandarizado: `Constancia/Constancia_[NOMBRE_ALUMNO].pdf`.
* **Información en la constancia:**
    * Nombre completo del estudiante.
    * Número de identificación.
    * Nombre del semillero (toma el primer semillero asociado al primer periodo registrado del estudiante).
    * Listado de todos los periodos de participación.
    * Fecha de expedición (actualmente fija al 01 de abril de 2025).
    * Firma del Decano de la Facultad de Ingeniería Industrial (VÍCTOR ANDRÉS RINCÓN GONZÁLEZ).

## Estructura del Repositorio

.
├── Constancia/                     # Carpeta de salida para los PDFs generados
│   └── Constancia_*.pdf
├── Estudiantes_Sin_Identificacion/ # Carpeta de salida para el Excel de estudiantes sin ID
│   └── Estudiantes_Sin_Identificacion.xlsx
├── datos/
│   ├── datos_consolidados.xlsx     # Archivo principal de entrada con los datos de los estudiantes
│   ├── logos/
│   │   └── fondo1.png              # Imagen de fondo para las constancias
│   ├── Inscripción de Semilleros de Investigación.xlsx - Sheet1.csv # Datos brutos de inscripción
│   ├── Plan de trabajo J Palomino 2023 -2.xlsx - *.csv            # Planes de trabajo semillero Turing
│   ├── Plan de trabajo N Meneses 2023 -2.xlsx - *.csv           # Planes de trabajo semillero Gindeollanos
│   └── Plan de trabajo N Meneses 2024-1 - FS.xlsx - *.csv         # Planes de trabajo semillero Logprox
├── certificado.py                  # Script principal de Python para generar las constancias
└── README.md                       # Este archivo


## Requisitos

* Python 3.x
* Bibliotecas de Python:
    * `pandas`
    * `reportlab`
    * `openpyxl` (necesario para que pandas lea archivos .xlsx)

Puedes instalar las bibliotecas necesarias usando pip:
```bash
pip install pandas reportlab openpyxl
Archivo de Entrada Principal
El script utiliza el archivo datos/datos_consolidados.xlsx como fuente principal de datos. Este archivo debe tener la siguiente estructura (columnas):

Periodo: El periodo académico de participación (e.g., "2024-1").
Semillero: Nombre del semillero de investigación.
Semestre: Semestre del estudiante en ese periodo.
Nombre: Nombre completo del estudiante.
Identificación: Número de identificación del estudiante.
Nota: Es crucial que este archivo esté correctamente formateado y ubicado en la ruta datos/datos_consolidados.xlsx.

Uso
Clona o descarga el repositorio.

Verifica los requisitos: Asegúrate de tener Python y las bibliotecas mencionadas instaladas.

Prepara los datos:

Asegúrate de que el archivo datos/datos_consolidados.xlsx contenga la información actualizada de los estudiantes.
Verifica que la imagen de fondo datos/logos/fondo1.png esté presente.
Ejecuta el script:
Abre una terminal o línea de comandos, navega hasta la raíz del proyecto y ejecuta:

Bash

python certificado.py
Revisa los resultados:

Las constancias en PDF se guardarán en la carpeta Constancia/.
Si hubo estudiantes sin número de identificación, se generará un archivo Estudiantes_Sin_Identificacion/Estudiantes_Sin_Identificacion.xlsx.
Personalización (Opcional)
Plantilla de fondo: Para cambiar la imagen de fondo, reemplaza el archivo datos/logos/fondo1.png por tu nueva imagen, manteniendo el mismo nombre y ruta, o modifica la variable fondo_certificado en certificado.py.
Fecha de expedición: La fecha de expedición está actualmente codificada en el script ("El certificado es otorgado el día 01 de abril de 2025"). Para cambiarla, debes modificar esta línea directamente en el archivo certificado.py.
Firmante: El nombre y cargo del firmante (VÍCTOR ANDRÉS RINCÓN GONZÁLEZ, Decano de la Facultad de Ingeniería Industrial) también están codificados en el script. Puedes modificarlos en las líneas correspondientes dentro de certificado.py.
Consideraciones
El script toma el nombre del semillero del primer periodo registrado para cada estudiante. Si un estudiante ha estado en múltiples semilleros y se desea un comportamiento diferente, el script necesitaría ser ajustado.
Los nombres de archivo de salida se generan reemplazando espacios por guiones bajos y eliminando caracteres no alfanuméricos para asegurar compatibilidad.
Posibles Mejoras Futuras
Permitir la configuración de la fecha de expedición y los datos del firmante a través de un archivo de configuración o argumentos de línea de comandos.
Manejo más avanzado de estudiantes que participan en múltiples semilleros en el mismo periodo o a lo largo del tiempo (e.g., permitir elegir cuál semillero mostrar o listar todos).
Interfaz gráfica de usuario (GUI) para facilitar el uso a personal no técnico.
Mejorar la validación de datos del archivo Excel de entrada.
