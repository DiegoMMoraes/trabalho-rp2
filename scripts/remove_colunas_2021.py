import pandas as pd

colunas_para_remover = ['Unnamed: 0','ID_SAEB', 'ID_REGIAO', 'ID_MUNICIPIO', 'ID_ESCOLA', 'ID_TURMA', 'ID_SERIE', 'IN_SITUACAO_CENSO', 'IN_PREENCHIMENTO_LP', 'IN_PREENCHIMENTO_MT', 'IN_PRESENCA_LP', 'IN_PRESENCA_MT', 'ID_CADERNO_LP', 'ID_BLOCO_1_LP', 'ID_BLOCO_2_LP', 'ID_CADERNO_MT', 'ID_BLOCO_1_MT', 'ID_BLOCO_2_MT', 'TX_RESP_BLOCO_1_LP', 'TX_RESP_BLOCO_2_LP', 'TX_RESP_BLOCO_1_MT', 'TX_RESP_BLOCO_2_MT', 'IN_PROFICIENCIA_LP', 'IN_PROFICIENCIA_MT', 'IN_AMOSTRA', 'ESTRATO', 'PESO_ALUNO_LP', 'PROFICIENCIA_LP', 'ERRO_PADRAO_LP', 'PESO_ALUNO_MT', 'PROFICIENCIA_MT', 'ERRO_PADRAO_MT', 'IN_PREENCHIMENTO_QUESTIONARIO', 'IN_INSE', 'INSE_ALUNO']

df = pd.read_csv('Dados_Saeb_2021/DADOS/dados_filtrados_2021.csv', dtype=str)
colunas_para_manter = [col for col in df.columns if col not in colunas_para_remover]
df = df[colunas_para_manter]
print(df.info())
df.to_csv('dados_filtrados_sem_coluna.csv')