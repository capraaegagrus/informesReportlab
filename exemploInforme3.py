from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4

imaxes = []

imaxe = Image (400, 0, 596,133, "/home/manuel/Imaxes/200.jpg")

debuxo = Drawing (30,30)
debuxo.add (imaxe)
debuxo.translate (0,0)
imaxes.append (debuxo)

debuxo = Drawing (30,30)
debuxo.add (imaxe)

debuxo.scale (1.5, 0.5)
debuxo.translate (-300, 300)
debuxo.rotate (45)
imaxes.append (debuxo)

debuxo = Drawing (30,30)
debuxo.add (imaxe)
debuxo.rotate (theta = 60)
debuxo.translate (-400, 00)
imaxes.append (debuxo)

debuxo = Drawing(A4[0],A4[1])

for aux in imaxes:
    debuxo.add(aux)
renderPDF.drawToFile (debuxo, "probaInformes3.pdf")


