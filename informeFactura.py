import os
from reportlab.platypus import (SimpleDocTemplate,PageBreak, Image,
                                Spacer, Paragraph, Table, TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from sqlite3 import dbapi2
try:
    bbdd = dbapi2.connect ("facturaBD.dat")
    cursor = bbdd.cursor ()
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
    facturas =[]

    try:
        cursorConsultaNumFacturas = cursor.execute ("select numFactura from facturas")
    except (dbapi2.DatabaseError):
        print("Erro na base de datos: ConsultaNumFacturas")

    listaFacturas = list()
    for numFactura in cursorConsultaNumFacturas:
        if numFactura [0] not in listaFacturas:
            listaFacturas.append(numFactura[0])



    for numFactura in listaFacturas:
        codigoCliente = None
        consultaFactura = None
        try:
            cursorConsultaFactura= cursor.execute ("select codCliente, codProducto, cantidade from facturas where numFactura = ?", (int(numFactura),))
            codigoCliente = cursorConsultaFactura.fetchone()[0]


        except (dbapi2.DatabaseError):
            print("Erro na base de datos: consultaFactura")

        detalleFactura.append (['Cod Cliente:', codigoCliente,'','Factura Num:', numFactura])

        try:
            cursorConsultaFactura = cursor.execute ("select nombre, direccion from clientes where codCliente = ?", (codigoCliente,))
            rexistroCliente = cursorConsultaFactura.fetchone()

        except (dbapi2.DatabaseError):
                print("Erro na base de datos: consultaCliente ")
        except dbapi2.OperationalError as err :
            print("Erroro operacional: consultaCliente")

        detalleFactura.append (['Nome: ',rexistroCliente[0],'','',''])
        detalleFactura.append (['Dirección:',rexistroCliente[1],'','',''])

        cursorConsultaDetalleFactura = cursor.execute("select codProducto, cantidade number from facturas where numFactura = ? ", (numFactura,))
        lconsultaDetalleFactura = []
        for elementoFactura in cursorConsultaDetalleFactura:
            lconsultaDetalleFactura.append ([elementoFactura[0],elementoFactura[1]])

        for elemento in lconsultaDetalleFactura:

            cursorConsultaProducto= cursor.execute ("select descripcion, prezo from productos where codProducto = ?", (elemento[0]))
            rexistroProducto = cursorConsultaProducto.fetchone()
            detalleFactura.append ([elementoFactura[0],rexistroProducto[0], elementoFactura[1], rexistroProducto[1], elementoFactura[1]*rexistroProducto[1]])

        print(detalleFactura)
        facturas.append(list(detalleFactura))
        detalleFactura.clear()

        #except dbapi2.OperationalError as err :
        #    print("Erroro operacprint (detalleFactura)ional: consultaFactura")
    print(facturas)
    print (facturas[0])

finally:

    print ("Pechando cursor e conexión base datos")
    cursor.close()
    bbdd.close()



doc = SimpleDocTemplate ("exemploTaboas.pdf", pagesize = A4)
guion = []


for factura in facturas:


    taboa  = Table (factura, colWidths=80, rowHeights=30)
    taboa.setStyle(TableStyle([
      ('TEXTCOLOR', (0,0),(-1,0), colors.blue),
      ('TEXTCOLOR', (0,1),(-1,-1), colors.green),
      ('BACKGROUND', (0,3),(-1,-1), colors.lightcyan),
      ('VALIGN', (0,0),(-1,-1), 'MIDDLE') ,
      ('BOX', (0,3),(-1,-1), 1,  colors.black),
      ('INNERGRID', (0,3),(-1,-1),0.5, colors.grey)
    ]))

    guion.append (taboa)
    guion.append (Spacer(0,20))

doc.build (guion)