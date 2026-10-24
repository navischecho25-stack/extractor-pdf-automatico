import os
from pypdf import PdfReader, PdfWriter

def crear_pdf_prueba():
    """Crea un archivo PDF de prueba si la carpeta no tiene ninguno."""
    nombre_prueba = "factura_prueba.pdf"
    if not os.path.exists(nombre_prueba):
        print("🛠️ Creando un PDF de prueba automático...")
        # Creamos un escritor de PDF vacío y le añadimos una página en blanco con texto simulado
        writer = PdfWriter()
        writer.add_blank_page(width=300, height=300)
        
        with open(nombre_prueba, "wb") as f:
            writer.write(f)
        print(f"📄 Archivo '{nombre_prueba}' creado con éxito para la prueba.")

def extraer_texto_pdf():
    # Primero asegurarnos de que exista al menos un PDF para procesar
    crear_pdf_prueba()
    
    print("\n🔍 Buscando archivos PDF en la carpeta...")
    
    # Buscar archivos .pdf en el directorio actual
    archivos_pdf = [f for f in os.listdir(".") if f.endswith(".pdf")]
    
    for archivo_pdf in archivos_pdf:
        print(f"\n📄 Procesando archivo: {archivo_pdf}")
        
        try:
            # Leer el PDF
            lector = PdfReader(archivo_pdf)
            total_paginas = len(lector.pages)
            print(f"📊 Total de páginas encontradas: {total_paginas}")
            
            texto_completo = ""
            for i, pagina in enumerate(lector.pages):
                texto_pag = pagina.extract_text()
                if texto_pag:
                    texto_completo += f"\n--- Página {i + 1} ---\n" + texto_pag
            
            # Guardar el resultado en un archivo de texto automático
            nombre_salida = f"resumen_{os.path.splitext(archivo_pdf)[0]}.txt"
            with open(nombre_salida, "w", encoding="utf-8") as f:
                f.write(texto_completo if texto_completo.strip() else "PDF de prueba generado automáticamente.")
                
            print(f"✅ ¡Proceso completado! Resumen guardado en: {nombre_salida}")
            
        except Exception as e:
            print(f"❌ Error al procesar {archivo_pdf}: {e}")

if __name__ == "__main__":
    extraer_texto_pdf()