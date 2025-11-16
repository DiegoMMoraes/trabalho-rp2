import pandas as pd

# Lista atualizada para remover colunas de ID, proficiência E perguntas não-comuns (Q23)
colunas_para_remover = [
    'Unnamed: 0', 'ID_SAEB', 'ID_REGIAO', 'ID_MUNICIPIO', 'ID_ESCOLA', 'ID_TURMA', 'ID_SERIE',
    'IN_SITUACAO_CENSO', 'IN_PREENCHIMENTO_LP', 'IN_PREENCHIMENTO_MT', 'IN_PRESENCA_LP', 'IN_PRESENCA_MT',
    'ID_CADERNO_LP', 'ID_BLOCO_1_LP', 'ID_BLOCO_2_LP', 'ID_CADERNO_MT', 'ID_BLOCO_1_MT', 'ID_BLOCO_2_MT',
    'TX_RESP_BLOCO_1_LP', 'TX_RESP_BLOCO_2_LP', 'TX_RESP_BLOCO_1_MT', 'TX_RESP_BLOCO_2_MT',
    'IN_PROFICIENCIA_LP', 'IN_PROFICIENCIA_MT', 'IN_AMOSTRA', 'ESTRATO', 'PESO_ALUNO_LP', 'PROFICIENCIA_LP',
    'ERRO_PADRAO_LP', 'PESO_ALUNO_MT', 'PROFICIENCIA_MT', 'ERRO_PADRAO_MT', 'IN_PREENCHIMENTO_QUESTIONARIO',
    'IN_INSE', 'INSE_ALUNO',
    # Adicionando perguntas não-comuns (Q23 - Clima Escolar)
    'TX_RESP_Q23a', 'TX_RESP_Q23b', 'TX_RESP_Q23c', 'TX_RESP_Q23d',
    'TX_RESP_Q23e', 'TX_RESP_Q23f', 'TX_RESP_Q23g', 'TX_RESP_Q23h', 'TX_RESP_Q23i'
]

df = pd.read_csv('Dados_Saeb_2023/DADOS/dados_filtrados_2023.csv', dtype=str)

# Manter apenas colunas que NÃO ESTÃO na lista de remoção
colunas_para_manter = [col for col in df.columns if col not in colunas_para_remover]
df = df[colunas_para_manter]

print("\nColunas mantidas no SAEB 2023:")
print(df.info())
df.to_csv('dados_filtrados_comuns_2023.csv')