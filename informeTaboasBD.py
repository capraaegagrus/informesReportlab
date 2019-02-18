import os
from reportlab.platypus import (SimpleDocTemplate,PageBreak, Image,
                                Spacer, Paragraph, Table, TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from sqlite3 import dbapi2

bbdd = dbapi2.connect ("bbdd.dat")
cursor = bbdd.cursor ()
cursor.execute ("select * from usuarios")

doc = SimpleDocTemplate ("exemploTaboas.pdf", pagesize = A4)
guion = []

datosTaboa =[['Dni', 'Nome', 'Direccion']]

for rexistro in cursor:
    datosTaboa.append (rexistro)

print (datosTaboa)

taboa  = Table (datosTaboa, colWidths=80, rowHeights=30)
taboa.setStyle(TableStyle([
    ('TEXTCOLOR', (0,0),(-1,0), colors.blue),
    ('TEXTCOLOR', (0,1),(-1,-1), colors.green),
    ('BACKGROUND', (0,1),(-1,-1), colors.lightcyan),
    ('VALIGN', (0,0),(-1,-1), 'MIDDLE') ,
    ('BOX', (0,1),(-1,-1), 1,  colors.black),
    ('INNERGRID', (0,1),(-1,-1),0.5, colors.grey)


]))

#

guion.append (taboa)

doc.build (guion)
