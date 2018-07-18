def montaString(arquivo):
    with open(arquivo) as file:
        lista = []
        for row in file:
            lista.append("'" + row.replace("\n", "") + "'")        
        return lista

def montaInt(arquivo):
    with open(arquivo) as file:
        lista = []
        for row in file:
            lista.append(row.replace("\n", ""))
        return lista

def montarQuery(nomeTabela, nomeCampo, valores):
    listaValores = ', '.join(valores)
    if(len(listaValores) > 300):
        f = open('arquivos/resultadoInSql.txt','w')
        f.write('''SELECT * FROM {nomeTabela} WHERE {nomeCampo} IN ({valores});'''.format(nomeTabela=nomeTabela, nomeCampo=nomeCampo, valores=listaValores))
        return "Resultado gerado no arquivo /arquivos/resultadoInSql.txt, devido a grande quantidade de dados."
    else:
        return '''SELECT * FROM {nomeTabela} WHERE {nomeCampo} IN ({valores});'''.format(nomeTabela=nomeTabela, nomeCampo=nomeCampo, valores=listaValores)
    
ARQUIVO = 'arquivos/lista.txt' #Caminho do arquivo que vai ser lido   
tabela = input("Informe o nome da tabela: ")
campo = input("Informe o campo utilizado na comparação: ") #Campo será feita o IN
print(montarQuery(tabela, campo, montaInt(ARQUIVO)))
input("Aperte enter para sair")
