import csv
from insertMovimentacaoBem import montaInsertPatrimonioBem

#Os dados passados no arquivo listaUnidades devem conter o código siapecad e o nome da unidade
with open('sigrh/csv/listaUnidades.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")
    f = open('sigrh/updates/updates.txt','w')
    codigo = 111016 #Aqui deve ser informado o último utilizado no banco de produção que vai ser utilizado como base para geração.
    for row in readCSV:       
        codigo += 1
        update = """--Unidade: {}
        UPDATE COMUM.UNIDADE SET CODIGO_UNIDADE = {} WHERE CODIGO_SIAPECAD = {};""".format(row[1], codigo, row[0])     
        f.write(update + "\n\n")
        print(update + "\n\n")
    f.close()


