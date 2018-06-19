import constantes
#Insert para termo de responsabilidade
# Um termo de responsabilidade é o documento pelo qual uma pessoa declara ter recebido e se tornado responsável 
# pela guarda e zelo de um ou mais bens. Comprometendo-se também a informar o Setor de Patrimônio sobre todas as ocorrências relativas 
# aos referidos bens e ainda ressarcir o Órgão por perdas e danos caso comprovada a omissão da responsabilidade de sua parte.
def montarInsertTermoResponsabilidade(row):
    insert = """INSERT INTO patrimonio.termo_responsabilidade(
            id, numero, ano, data, id_unidade_responsavel, id_ugp, 
            observacao, 
            tipo_tombamento, id_projeto, id_usuario, ano_termo_funpec, numero_termo_funpec, 
            empenho_funpec, id_local_bem, id_unidade_origem, id_local_origem, 
            id_responsavel, id_responsavel_local, codmerg, id_unidade_legado, 
            codmerg_lagarto, codmerg_sc)
    VALUES (NEXTVAL({seqIdTermo}), NEXTVAL({seqNumTermo}), 2017, CURRENT_TIMESTAMP, 1791, 657, 
            'TRANSFERÊNCIA CADASTRADA DIRETAMENTE NO BANCO DE DADOS.', 
            10, null, 1, null, null, 
            null, null, 1794, null, 
            8579, null, null, null, 
            null, null);""".format(seqIdTermo=SEQ_ID_TERMO, seqNumTermo=SEQ_NUM_TERMO_RESPONSABILIDADE, 
                ano=ANO, idOrigem=row[0], idDestino = row[1], tipoMovimentacao=4, idBem=row[2], unidadeRespAtual=row[3])
    return insert