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
    
print(montarQuery('teste', 'teste2', montaString('arquivos/lista.txt')))