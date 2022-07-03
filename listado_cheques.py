import csv

with open('cheques.csv') as f: # lo que estamos haciendo aqui es iterar linea por linea
    reader = csv.reader(f)
    for row in reader:
        print("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))



