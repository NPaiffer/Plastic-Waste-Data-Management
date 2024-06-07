import pandas as pd
from conexao_bd import conectar_bd
 
def ler_csv(caminho):
    df = pd.read_csv(caminho)
    df.columns = df.columns.str.strip()
    return df
 
def inserir_dados(conexao, tabela, df):
    cursor = conexao.cursor()
    cols = ", ".join([str(i) for i in df.columns.tolist()])
    
    for _, row in df.iterrows():
        row_values = [None if pd.isna(val) else val for val in row]
        sql = f"INSERT INTO {tabela} ({cols}) VALUES (:" + ", :".join([str(i) for i in range(1, len(row) + 1)]) + ")"
        
        try:
            cursor.execute(sql, row_values)
        except oracledb.DatabaseError as e:
            error, = e.args
            print(f"Erro ao inserir dados: {error.message}")
            print(f"SQL: {sql}")
            print(f"Dados: {row_values}")
    
    conexao.commit()
    cursor.close()
 
conexao = conectar_bd("oracle.fiap.com.br", "1521", "orcl")
 
if conexao:
    df1 = ler_csv('csv/2- participacao-despejo-residuo-plastico.csv')
    print("Colunas do CSV 1:", df1.columns)
    df1 = df1.rename(columns={
        "Entidade": "Pais",
        "Ano": "Ano",
        "Participação na emissão global de plásticos para o oceano": "Participacao_residuo_plastico"
    })
    df1 = df1[["Ano", "Pais", "Participacao_residuo_plastico"]]
 
    df2 = ler_csv('csv/4- desperdicio-plastico-per-capita.csv')
    print("Colunas do CSV 2:", df2.columns)
    df2 = df2.rename(columns={
        "Entidade": "Pais",
        "Ano": "Ano",
        "Lixo plástico mal gerenciado por pessoa (kg por ano)": "Desperdicio_per_capita"
    })
    df2 = df2[["Ano", "Pais", "Desperdicio_per_capita"]]
 
    inserir_dados(conexao, "participacao_despejo_residuo_plastico", df1)
    inserir_dados(conexao, "desperdicio_plastico_per_capita", df2)
 
    conexao.close()
    print("Dados inseridos com sucesso!")
else:
    print("Não foi possível conectar ao banco de dados")