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
    return '''SELECT * FROM {nomeTabela} WHERE {nomeCampo} IN ({valores})'''.format(nomeTabela=nomeTabela, nomeCampo=nomeCampo, valores=listaValores);
    
ARQUIVO = 'arquivos/lista.txt' #Caminho do arquivo que vai ser lido   
NOME_TABELA = 'schema.tabela' #Nome da tabela que será feito o Select
CAMPO_COMPARADOR = 'nome_campo' #Campo será feita o IN
print(montarQuery(NOME_TABELA, CAMPO_COMPARADOR, montaString(ARQUIVO)))