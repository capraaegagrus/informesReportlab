from reportlab.pdfgen import canvas

aux = canvas.Canvas ("informeImaxesReportlab.pdf")
aux.drawImage ("/home/manuel/Imaxes/cabra-800x445.jpg", 50, 200, 500, 270)
aux.drawString (50,150, "Exemplo de intsercion de imaxes en PDF")

aux.showPage()
aux.save()

print ("Segundo informe con imaxes")
