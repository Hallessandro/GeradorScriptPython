import psycopg2
import sys
import pprint

def main():
	#conn_string = "host='ufsj' dbname='administrativo' user='desenvolvedor' password='d3s3nvs1g' port='25432'"
    conn_string = "host='ufsj' dbname='administrativo' user='desenvolvedor' password='d3s3nvs1g' port='25432'"
	# get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
	# conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
	# execute the Query
    cursor.execute("SELECT * FROM FINANCEIRO.FICHA_FINANCEIRA WHERE ANO = 2018 limit 1;")
    #open the file
    f = open('updatesFicha.txt','w')
    # retrieve the records from the database        
    for row in cursor:
        f.write(montarUpdate(row).strip() + "\n")        
	# print out the records using pretty print
	# note that the NAMES of the columns are not shown, instead just indexes.
	# for most people this isn't very useful so we'll show you how to return
	# columns as a dictionary (hash) in the next example.
    cursor.close()
 
def montarUpdate(row):
     update = '''UPDATE financeiro.ficha_financeira SET ano_char_apagar=NULL, rendimento_desconto=NULL, janeiro={jan}, fevereiro={fev}, marco={mar}, abril={abr}, maio={maio}, junho={jun}, julho={jul}, agosto={ago}, setembro={setem}, outubro={out}, novembro={nov}, dezembro={dez}, id_servidor={servidor}, id_rubrica={rubrica}, multiplicador={multiplicador}, sequencia={sequencia}, codmergrh=NULL, ano={ano}, origem={origem}, migracao=false WHERE id_ficha_financeira={idFicha};
     '''.format(jan=row[3], fev=row[4], mar=row[5], abr=row[6], maio=row[7], jun=row[8], jul=row[9], 
        ago=row[10], setem=row[11], out=row[12], nov=row[13], dez=row[14], servidor=row[15], idFicha=row[0], 
        rubrica=row[16], multiplicador=row[17], sequencia=row[18], ano=row[20], origem=row[21])
     return update
if __name__ == "__main__":
	main()