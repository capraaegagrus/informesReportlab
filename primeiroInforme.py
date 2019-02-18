from reportlab.pdfgen import canvas

aux = canvas.Canvas ("proba.pdf")

aux.drawString (0,0,"Posición orixen (x,y) = (0,0)")
aux.drawString (50,100,"Posición  (x,y) = (50,100)")
aux.drawString (150,20,"Posición (x,y)j = (150,20)")

aux.showPage( )
aux.save()

print ("Informe feito")