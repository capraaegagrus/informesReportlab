from reportlab.pdfgen import canvas

texto = ['Este é o texto de exemplo', 'no que imos a ter varias liñas',
         'para mostrar as cararterísticas', 'do obxecto canvas']

aux = canvas.Canvas ("probaTextoCanvas.pdf")

obxectoTexto = aux.beginText ()
obxectoTexto.setTextOrigin (100,800)
obxectoTexto.setFont ("Courier", 14)
espacio = 0
for linha in texto:
    #obxectoTexto.textLine (linha)
    obxectoTexto.setCharSpace (espacio)
    obxectoTexto._textOut(linha)
    obxectoTexto.moveCursor(20,15)
    espacio = espacio + 2
obxectoTexto.setFillGray (0.5)

obxectoTexto.setCharSpace(0)

linhas_texto = '''
Este é un exemplo con texto multiliña.
Escribimos texto con Reportlab .
Tendo en conta que traballamos en varias
liñas.'''
obxectoTexto.setWordSpace (15)
obxectoTexto.textLines(linhas_texto)


obxectoTexto.setWordSpace (0)
cadea = "Tipo de letra con ReportLab 1234"
for tipo_letra in aux.getAvailableFonts():
    obxectoTexto.setFont (tipo_letra, 12)
    obxectoTexto.textLine (tipo_letra + ": " + cadea)

aux.drawText (obxectoTexto)


aux.showPage()
aux.save()



