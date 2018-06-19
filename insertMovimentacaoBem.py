import constantes
#Insert para movimentação de bem
def montaInsertPatrimonioBem(ano, idOrigem, idDestino, tipoMovimentacao, idBem,unidadeRespAtual):
    insert = """INSERT INTO patrimonio.movimentacao_bem(
                    id, data_saida, data_recebimento, numero_guia, ano_guia, 
                    observacao, 
                    id_unidade_origem, id_unidade_destino, tipo_movimentacao, id_bem, 
                    id_termo_novo, id_termo_anterior, valor, id_usuario, data_cadastro, 
                    id_usuario_recebimento, bens_desconhecidos, id_local_bem, id_usuario_estorno, 
                    data_estorno, justificativa_estorno, tipo_status_movimentacao, 
                    id_local_bem_destino, justificativa, valor_anterior, id_registro_entrada_transf, 
                    id_usuario_cadastro, necessita_autenticacao, bem_terceiro, id_ajuste_valor_contabil, 
                    id_mov_associada, codmerg, id_unidade_origem_legado, id_unidade_destino_legado, 
                    codmerg_lagarto, codmerg_sc)
            SELECT NEXTVAL({seqIdMovimentacao}), CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, CURRVAL({numGuiaMovimentacao}), {ano},
                    'TRANSFERÊNCIA CADASTRADA DIRETAMENTE NO BANCO DE DADOS.', 
                    {idOrigem}, {idDestino}, {tipoMovimentacao}, {idBem}, 
                    CURRVAL(seqIdtermo), id_termo_responsabilidade, valor_acumulado, 1, CURRENT_TIMESTAMP, 
                    1, null, null, null, 
                    null, null, null, 
                    null, null, null, null, 
                    1, false, false, null, 
                    null, null, null, null, 
                    null, null
            FROM patrimonio.bem
            WHERE id_unidade_resp_atual = {unidadeRespAtual};""".format(seqIdMovimentacao=SEQ_ID_MOVIMENTACAO_BEM, numGuiaMovimentacao=SEQ_NUM_GUIA_MOVIMENTACAO, ano=ANO, 
                                        idOrigem=idOrigem, idDestino=idDestino, tipoMovimentacao=tipoMovimentacao, 
                                        idBem=idBem, seqIdtermo=SEQ_ID_TERMO, unidadeRespAtual=unidadeRespAtual)
    return insert