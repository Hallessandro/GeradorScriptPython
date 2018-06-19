import csv

with open('dadosParaInsert.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")
    f = open('insertsGerados.txt','w')
    for row in readCSV:
        insert = "INSERT INTO COMUM.TESTE (id, nome) VALUES (" + row[0] + "," + "'" + row[1] +"'"+");"
        f.write(insert + "\n")
    f.close()