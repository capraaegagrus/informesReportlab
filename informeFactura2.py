
from reportlab.platypus import (SimpleDocTemplate, PageBreak,
                                Spacer, Table, TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from sqlite3 import dbapi2

try:
    bbdd = dbapi2.connect("facturaBD.dat")
    cursor = bbdd.cursor()
    '''
    cursor.execute("""create table clientes (codCliente text,
                       nombre text, direccion text)""")
    cursor.execute("""create table facturas (numFactura number, codCliente text,
                       codProducto text, cantidade number)""")
    cursor.execute("""create table productos (codProducto text,
                       descripcion text, prezo number)""")

    cursor.execute("""insert into clientes
                   values ('333', 'Maria ', 'Canceleiro')""")
    cursor.execute("""insert into clientes
                   values ('222', 'Pedro ', 'Rosalia')""")

    cursor.execute("""insert into facturas
                   values (2, '333', '1',3)""")
    cursor.execute("""insert into facturas
                   values (2, '333', '2',5)""")
    cursor.execute("""insert into facturas
                   values (3, '333', '3',1)""")


    cursor.execute("""insert into productos
                   values ('1', 'Tizas', 9)""")
    cursor.execute("""insert into productos
                   values ('2', 'Rotuladores', 5)""")
    cursor.execute("""insert into productos
                   values ('3', 'Borradores', 4)""")

    bbdd.commit()
    '''

    detalleFactura = []
    facturas = []

    cursorConsultaNumFacturas = cursor.execute("select numFactura from facturas")
    listaFacturas = list()
    for numFactura in cursorConsultaNumFacturas:
        if numFactura[0] not in listaFacturas:
            listaFacturas.append(numFactura[0])

    #print (listaFacturas)

    for numFactura in listaFacturas:
        codigoCliente = None
        consultaFactura = None
        cursorConsultaFactura = cursor.execute ("select codCliente from facturas where numFactura = ?", (int(numFactura),))
        codigoCliente = cursorConsultaFactura.fetchone()[0]

        detalleFactura.append (['Cod Cliente:',codigoCliente,'','Num Factura:',numFactura])

        cursorConsultaFactura = cursor.execute ("select nombre, direccion from clientes where codCliente = ?", (codigoCliente,))
        rexistroCliente = cursorConsultaFactura.fetchone()

        detalleFactura.append(['Nome', rexistroCliente [0],'','',''])
        detalleFactura.append (['Dirección',rexistroCliente[1],'','',''])

        cursorConsultaDetalleFactura = cursor.execute ("select codProducto, cantidade from facturas where numFactura = ?", (int(numFactura),))
        lconsultaDetalleFactura = []
        for elementoFactura in cursorConsultaDetalleFactura:
            lconsultaDetalleFactura.append([elementoFactura[0],elementoFactura[1]])
        detalleFactura.append(["", "", "", "", ""])
        detalleFactura.append(["Código producto", "Descripción", "Cantidade", "Prezo unitario:", "Prezo"])
        prezoTotal = 0
        for elemento in lconsultaDetalleFactura:
            cursorConsultaProducto = cursor.execute ("select descripcion, prezo from productos where codProducto = ?", (elemento[0]))
            rexistroProducto =cursorConsultaProducto.fetchone()
            prezo = elemento[1]*rexistroProducto[1]
            detalleFactura.append ([elemento[0],rexistroProducto[0],elemento[1],rexistroProducto[1], prezo])
            prezoTotal = prezoTotal + prezo

        detalleFactura.append (["","","","Prezo total:", prezoTotal])
        facturas.append (list(detalleFactura))
        detalleFactura.clear()

finally:

    print("Pechando cursor e conexión base datos")
    cursor.close()
    bbdd.close()


doc = SimpleDocTemplate("exemploFacturas.pdf", pagesize=A4)
guion = []


for factura in facturas:

    taboa = Table(factura, colWidths=80, rowHeights=30)

    taboa.setStyle(TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, 2), colors.blue),
        ('TEXTCOLOR', (0, 4), (-1, -1), colors.green),
        ('BACKGROUND', (0, 4), (-1, -1), colors.lightcyan),
        ('ALIGN', (2,5), (-1, -1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOX', (0, 0), (-1, 2), 1, colors.black),
        ('BOX', (0, 4), (-1, -2), 1, colors.black),
        ('INNERGRID', (0, 4), (-1, -2), 0.5, colors.grey)
    ]))

    guion.append(taboa)
    guion.append(Spacer(0, 40))
    guion.append(PageBreak())

doc.build(guion)
