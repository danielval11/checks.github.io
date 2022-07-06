# Nombre del proyecto:
checks.github.io

## Dependencias:
Python 3 https://www.python.org/downloads/

## Problemática del proyecto:
Se quiere poder consultar los cheques que tiene emitidos y depositados en sus cuentas un determinado cliente, pudiendo estar estos pendientes, aprobado o rechazado. La información se tiene que obtener desde un archivo.

## Descripción del proyecto:
El proyecto consta de un script de Python que recibe argumentos de un archivo csv.
El programa analiza, organiza e imprime por pantalla o por csv (creando un archivo) los argumentos determinados.
Si dos cheques de un mismo DNI tienen el mismo número se muestra error por pantalla.
Si no se recibe como argumento el estado del cheque, se deberán imprimir los cheques sin filtrar por estado.
Si el parámetro salida es 'PANTALLA' se deberá imprimir por pantalla todos los valores que se tienen.
Si el parámetro salida es 'CSV' se exporta con las siguientes condiciones:
*DNI-TIMESTAMPS ACTUAL.csv
*se exportan las 2 fechas, el valor del cheque y la cuenta
 

## Comando para la ejecución del programa:
python3 listado_cheques.py argumentos

los argumentos son los siguientes y en el orden en que se nombran:
1. Nombre del archivo csv. 
2. DNI del cliente donde se filtraran. 
3. Salida: PANTALLA o CSV 
4. Tipo de cheque: EMITIDO o DEPOSITADO 
5. Estado del cheque: PENDIENTE, APROBADO, RECHAZADO. (Opcional) 
6. Rango fecha: xx-xx-xxxx:yy-yy-yyyy (Opcional) 

## Lista de autores del proyecto

1. Julian scarramberg
2. Lara victoria Pereyra
3. Rocio Ayelen Gómez
4. Milena Fernández
5. Daniel alejandro valbuena prieto
