INSERT INTO patrimonio.termo_responsabilidade(
            id, numero, ano, data, id_unidade_responsavel, id_ugp, 
            observacao, 
            tipo_tombamento, id_projeto, id_usuario, ano_termo_funpec, numero_termo_funpec, 
            empenho_funpec, id_local_bem, id_unidade_origem, id_local_origem, 
            id_responsavel, id_responsavel_local, codmerg, id_unidade_legado, 
            codmerg_lagarto, codmerg_sc)
    VALUES (NEXTVAL('public.termo_seq'), NEXTVAL('public.seq_3_2018'), 2018, CURRENT_TIMESTAMP, 169, 657, 
            'TRANSFERÊNCIA CADASTRADA DIRETAMENTE NO BANCO DE DADOS- Tarefa #.', 
            10, null, 1, null, null, 
            null, null, 13, null, 
            3624, null, null, null, 
            null, null);
 
 
SELECT NEXTVAL('public.seq_12_2018');
 
 
INSERT INTO patrimonio.movimentacao_bem(
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
     SELECT NEXTVAL('patrimonio.movimento_bem_seq'), CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, CURRVAL('public.seq_12_2018'), 2018,
            'TRANSFERÊNCIA CADASTRADA DIRETAMENTE NO BANCO DE DADOS.', 
            13, 169, 4, id, 
            CURRVAL('public.termo_seq'), id_termo_responsabilidade, valor_acumulado, 1, CURRENT_TIMESTAMP, 
            1, null, null, null, 
            null, null, null, 
            null, null, null, null, 
            1, false, false, null, 
            null, null, null, null, 
            null, null
       FROM patrimonio.bem
      WHERE id_unidade_resp_atual = 13 AND mat.ID_GRUPO = 891;
 
 
UPDATE patrimonio.bem 
SET id_termo_responsabilidade = CURRVAL('public.termo_seq'),
    id_unidade_resp_atual = 169
WHERE id_unidade_resp_atual = 13 AND mat.ID_GRUPO = 891;