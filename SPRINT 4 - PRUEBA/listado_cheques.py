import sys
import csv
import datetime

datos = []
header = []
chequesPorDNI = []
chequesPorTipo = []
chequesPorEstado = []

with open('test.csv', 'r') as file:
    fileCSV = csv.reader(file)
    header = next(fileCSV)
    for row in fileCSV:
        dato = dict(zip(header, row))
        datos.append(dato)

def inicio():
    if 4 <= len(sys.argv) <= 6:
        identificarDNI()
    else:
        print('Numero de argumentos incorrectos.')
        exit(1)

def identificarDNI():
    for elem in datos:
        if sys.argv[1] == elem.get('DNI'):
            chequesPorDNI.append(elem)
        else:
            " "
    if len(chequesPorDNI) != 0:
        validarCheques()
    else:
        print('No se han encontrado cheques asociados al DNI ingresado.')
        exit(1)


def validarCheques():
    numerosDeCheque = []
    for elem in chequesPorDNI:
        numerosDeCheque.append(elem.get('NroCheque'))
    numerosDeChequeUnicos = set(numerosDeCheque)
    if len(numerosDeCheque) == len(numerosDeChequeUnicos):
        identificarTipo()
    else:
        print('Existen dos o más cheques para los cuales su número de identificación es el mismo.')


def identificarTipo():
    for elem in chequesPorDNI:
        if sys.argv[3] == elem.get('Tipo'):
            chequesPorTipo.append(elem)
        else:
            " "
    if len(chequesPorTipo) != 0:
        if len(sys.argv) >= 5:
            identificarEstado()
        elif len(sys.argv) == 4:
            identificarSalida(chequesPorTipo)
        else:
            " "
    else:
        if(sys.argv[3] == 'DEPOSITADO' or sys.argv[3] == 'EMITIDO'):
            print('No existen cheques asociados a ese DNI que hayan sido ' + sys.argv[3].lower() + 's.')
            exit(1)
        else:    
            print('El tipo de cheque ingresado es incorrecto.')
            exit(1)


def identificarEstado():
    for elem in chequesPorTipo:
        if sys.argv[4] == elem.get('Estado'):
            chequesPorEstado.append(elem)
        else:
            " "
    if len(chequesPorEstado) != 0:
        if len(sys.argv) == 6:
            print('fecha')
        elif len(sys.argv) == 5:
            identificarSalida(chequesPorEstado)
        else:
            " "
    else:
        if(sys.argv[4] == 'APROBADO' or sys.argv[4] == 'RECHAZADO' or  sys.argv[4] == 'PENDIENTE'):
            print('No existen cheques asociados a ese DNI con el es estado de ' + sys.argv[4].lower() + 's.')
            exit(1)
        else:
            print('El tipo de estado ingresado es incorrecto.')
            exit(1)

def identificarSalida(cheques):
    if sys.argv[2] == 'PANTALLA':
        print(cheques)
    elif sys.argv[2] == 'CSV':
        escribirCSV(cheques)
        print('csv')
    else:
        print('El argumento de salida es incorrecto, se debe ingresar "PANTALLA" o "CSV')
        exit(1)

def escribirCSV(cheques):
    descarga = []

    for elem in cheques:
        values = {'NumeroCuentaDestino': elem['NumeroCuentaDestino'], 'Valor': (elem['Valor']),
                  'FechaOrigen': elem['FechaOrigen'], 'FechaPago': elem['FechaPago']}
        descarga.append(values)

    now = datetime.datetime.now()
    with open(sys.argv[1] + " - " + now.strftime('%Y-%m-%d-%H.%M.%S') + '.csv', "w", newline='') as archivo:
        fieldnames = ['NumeroCuentaDestino',
                      'Valor', 'FechaOrigen', 'FechaPago']
        writer = csv.DictWriter(archivo, fieldnames=fieldnames)
        writer.writeheader()
        for elem in descarga:
            writer.writerow(elem)





inicio()
