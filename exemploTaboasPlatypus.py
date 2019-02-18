import os
from reportlab.platypus import (SimpleDocTemplate,PageBreak, Image,
                                Spacer, Paragraph, Table, TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

doc = SimpleDocTemplate ("exemploTaboasPlatypus.pdf", pagesize = A4)
guion = []

datosTaboa =[['', 'Ventas', 'Compras'],
              ['Xaneiro', 5000, 4000],
             ['Febreiro', 6000, 3000],
             ['Marzo', 8000,5000]]

taboa  = Table (datosTaboa, colWidths=80, rowHeights=30)
taboa.setStyle(TableStyle([
    ('TEXTCOLOR', (0,1),(0,-1), colors.blue),
    ('TEXTCOLOR', (1,1),(2,-1), colors.green),
    ('BACKGROUND', (1,1),(-1,-1), colors.lightcyan),
    ('VALIGN', (0,0),(-1,-1), 'MIDDLE') ,
    ('BOX', (1,1),(-1,-1), 1,  colors.black),
    ('INNERGRID', (1,1),(-1,-1),0.5, colors.grey)


]))

#

guion.append (taboa)

doc.build (guion)

