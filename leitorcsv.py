import csv
from insertMovimentacaoBem import montaInsertPatrimonioBem

with open('dadosParaInsert.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")
    f = open('insertsGerados.txt','w')
    for row in readCSV:       
        f.write(montaInsertPatrimonioBem(row) + "\n\n")
        print(montaInsertPatrimonioBem(row) + "\n\n")
    f.close()


