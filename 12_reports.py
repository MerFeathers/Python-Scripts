#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

#Using the reportlab Python library, define the method generate_report to build the PDF reports. 
# create a PDF report named processed.pdf

def generate_report(filename, title, additional_info):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    report_info = [Paragraph(info, styles["BodyText"]) for info in additional_info]
    empty_line = Spacer(1,20)
    report.build([report_title, empty_line] + report_info)
    


#Cuando el script reports.py recibe la lista de cadenas de texto (cada una representando una línea del archivo de texto), cada cadena se convierte en un objeto Paragraph. Un objeto Paragraph en reportlab representa un párrafo en el PDF.
#Cuando se añade un objeto Paragraph al PDF, reportlab automáticamente añade un salto de línea después de cada párrafo. Por lo tanto, si tienes dos cadenas en tu lista que representan “name: Apple” y “weight: 500 lbs”, se convertirán en dos objetos Paragraph y se añadirán al PDF como dos líneas separadas.
#Además, si tienes una cadena vacía en tu lista (que representa una línea en blanco en el archivo de texto), también se convertirá en un objeto Paragraph. Sin embargo, dado que la cadena está vacía, este párrafo no tendrá contenido visible y aparecerá como una línea en blanco en el PDF.
