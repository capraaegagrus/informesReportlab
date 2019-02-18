import os

from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

follaEstilo = getSampleStyleSheet()

guion = []

cabeceira = follaEstilo ['Heading4']
cabeceira.pageBreakBefore = 1
cabeceira.keepWithNext = 1
cabeceira.backColor = colors.lightcyan
parrafo = Paragraph("Cabeceira do documento", cabeceira)
guion.append (parrafo)

cadea =  "Exemplo de texto con paragrafos en platypus " *500

estilo = follaEstilo ['BodyText']
paragrafo2 = Paragraph (cadea, estilo)
guion.append (paragrafo2)

guion.append (Spacer (0,20))

imaxe = Image (os.path.realpath("/home/manuel/Imaxes/cabra-800x445.jpg"), width = 400, height= 222)
guion.append(imaxe)

doc = SimpleDocTemplate ("exemploInformePlatypus.pdf", pagesize=A4, showBoundary = 0)
doc.build(guion)
