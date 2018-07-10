def montaInsert():    
    #Caso você ainda não saiba o id, passe a consulta para recuperar o mesmo entre ()
    #Se souber o id passe o mesmo como string como mostrado abaixo
    #ID_FERIAS_CONF = '600'
    ID_FERIAS_CONF = '(SELECT ID_FERIAS_CONFIGURACAO FROM FUNCIONAL.FERIAS_CONFIGURACAO WHERE ID_SITUACAO = 40 AND ID_CATEGORIA = 1 AND ID_TIPO_REGIME_JURIDICO = 4 AND DIREITO_ABONO = FALSE AND MAXIMO_PARCELAS = 3 LIMIT 1)'
    with open('sigrh/ferias/combinacoesPossiveis.txt') as combinacoes, open('sigrh/ferias/parcelas.txt') as parcelas:
        for c, p in zip(combinacoes, parcelas):
            INSERT_BASE = '''INSERT INTO funcional.ferias_divisao_periodo (id_ferias_divisao_periodo, divisao, id_ferias_configuracao, parcelas) VALUES(nextval('funcional.ferias_divisao_seq'), '{divisao}', {feriasConf}, {parcela});
            '''.format(divisao=c.replace("\n", ""), parcela=p.replace("\n", ""), feriasConf=ID_FERIAS_CONF.replace("\n", ""))
            print(INSERT_BASE.replace("\n", ""))           
montaInsert()            


