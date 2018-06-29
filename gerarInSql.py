def montaString(arquivo):
    with open(arquivo) as file:
        lista = []
        for row in file:
            lista.append(row.replace("\n", ""))        
        return lista

def montaInt(arquivo):
    with open(arquivo) as file:
        lista = []
        for row in file:
            lista.append(int(row))
        return lista

#print(montaString('arquivos/lista.txt'))
print(montaInt('arquivos/lista.txt'))
