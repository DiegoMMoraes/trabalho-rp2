import pandas as pd

df1 = pd.read_csv("../Dados_Saeb_2021/DADOS/SP_TS_ALUNO_34EM_parte_006.csv")
df2 = pd.read_csv("../Dados_Saeb_2021/DADOS/SP_TS_ALUNO_34EM_parte_007.csv")

df1_filtrado = df1[
    (df1["IN_PREENCHIMENTO_LP"] == 1) &
    (df1["IN_PREENCHIMENTO_MT"] == 1) &
    (df1["IN_PRESENCA_LP"] == 1) &
    (df1["IN_PRESENCA_MT"] == 1) &
    (df1["IN_PROFICIENCIA_LP"] == 1) &
    (df1["IN_PROFICIENCIA_MT"] == 1) &
    (df1["IN_PREENCHIMENTO_QUESTIONARIO"] == 1)
]

df2_filtrado = df2[
    (df2["IN_PREENCHIMENTO_LP"] == 1) &
    (df2["IN_PREENCHIMENTO_MT"] == 1) &
    (df2["IN_PRESENCA_LP"] == 1) &
    (df2["IN_PRESENCA_MT"] == 1) &
    (df2["IN_PROFICIENCIA_LP"] == 1) &
    (df2["IN_PROFICIENCIA_MT"] == 1) &
    (df2["IN_PREENCHIMENTO_QUESTIONARIO"] == 1)
]

df_filtrado_mesclado = pd.concat([df1_filtrado, df2_filtrado], ignore_index=True)

cols_tx_resp = [c for c in df_filtrado_mesclado.columns if c.startswith("TX_RESP")]

if cols_tx_resp:
    df_filtrado_mesclado = df_filtrado_mesclado[~df_filtrado_mesclado[cols_tx_resp].isin(["*", "."]).any(axis=1)]

df_filtrado_mesclado.to_csv("dados_filtrados_2021.csv", index=False)

print("Arquivo 'dados_filtrados_2021.csv' gerado com sucesso!")
