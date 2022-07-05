import sys
import csv
import datetime

if len(sys.argv) < 5 or len(sys.argv) > 7:
    print("Numero de argumentos incorrecto")
    exit(1)

nombre_archivo_csv = sys.argv[1]
numero_dni = sys.argv[2]
salida = sys.argv[3]
tipo_de_cheque = sys.argv[4]
estado_de_cheque = None
rango_de_fecha = None

if len(sys.argv) >= 6:
    estado_de_cheque = sys.argv[5]

    if len(sys.argv) == 7:
        rango_de_fecha = sys.argv[6]

cabecera = []
cheques_filtrado = []

with open(nombre_archivo_csv) as f:  #iteramos linea por linea
    duplicados_por_dni = []

    reader = csv.reader(f)
    num_linea = 0
    for row in reader:
        if num_linea == 0:
            cabecera = row
            num_linea += 1
            continue

        numero_de_cheque_linea = row[0]
        dni_linea = row[8]
        tipo_linea = row[9]
        estado_linea = row[10]

        if (numero_de_cheque_linea, dni_linea) in duplicados_por_dni:
            print('Dado el DNI {} existen numeros de cheques duplicados (nro. {}).'.format(dni_linea, numero_de_cheque_linea))
            sys.exit(1)

        duplicados_por_dni.append((numero_de_cheque_linea, dni_linea))

        if numero_dni == dni_linea and (tipo_de_cheque == tipo_linea) and \
                (estado_de_cheque is None or estado_de_cheque == estado_linea):

            cheques_filtrado.append(row)

        num_linea += 1

if salida == 'PANTALLA':
    print("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}".format(cabecera[0], cabecera[1], cabecera[2], cabecera[3],
                                                                cabecera[4], cabecera[5], cabecera[6], cabecera[7],
                                                                cabecera[8], cabecera[9], cabecera[10]))

    for row in cheques_filtrado:
        print("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}".format(row[0], row[1], row[2], row[3], row[4], row[5],
                                                                    row[6], row[7], row[8], row[9], row[10]))
elif salida == 'CSV':
    ahora = datetime.datetime.now()
    nombre_archivo_salida = '{}-{}.csv'.format(numero_dni, ahora.strftime('%Y-%m-%d-%H:%M:%S'))

    with open(nombre_archivo_salida, 'w') as f:
        f.write("{},{},{},{}\n".format(cabecera[4], cabecera[5], cabecera[6], cabecera[7]))

        for row in cheques_filtrado:
            f.write("{},{},{},{}\n".format(row[4], row[5], row[6], row[7]))