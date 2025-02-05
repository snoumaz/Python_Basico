from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
script = input("Dime la ubicacion del archivo Python: ")
pdf_file = input("Dime el nombre del archivo PDF:  ")

def py_to_pdf(py_file, pdf_file):
    with open(py_file, "r") as f:
        lines = f.readlines()
    
    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter
    y_position = height - 40

    for line in lines:
        c.drawString(40, y_position, line.strip())
        y_position -= 15  
        if y_position < 40:  
            c.showPage()
            y_position = height - 40  

    c.save()

py_to_pdf(script, pdf_file)
print("El documento PDF se ha generado exitosamente. Consulte el archivo en la ubicacion especificada.  \nSi desea volver a generar un documento PDF, ingrese nuevamente los nombres de archivo.  \nSi desea salir,")

