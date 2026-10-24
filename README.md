# 📄 Extractor Automático de Datos en PDFs (`extractor_pdf.py`)

## 🎯 Descripción del Proyecto
Este script de automatización en Python (BPA - Business Process Automation) resuelve la necesidad empresarial de procesar documentos PDF repetitivos. El script detecta archivos PDF de forma autónoma, extrae su contenido de texto página por página y genera un resumen ordenado en formato de texto (`.txt`), ahorrando horas de revisión manual.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.14
* **Librería Externa:** `pypdf` (instalada vía `python -m pip install pypdf`)
* **Módulos Nativos:** `os` (gestión de rutas y directorios)

## 🚀 Características
* **Autonomía Total:** Incluye una función incorporada que genera un archivo PDF de prueba si la carpeta de trabajo está vacía, permitiendo validar la ejecución de inmediato.
* **Extracción Dinámica:** Lee múltiples archivos PDF de forma masiva en un solo ciclo de ejecución.
* **Control de Errores:** Bloque de protección `try-except` para evitar interrupciones ante archivos corruptos o ilegibles.

## 💻 Instrucciones de Uso
1. Asegúrate de tener la librería instalada:
   ```bash
   python -m pip install pypdf