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
