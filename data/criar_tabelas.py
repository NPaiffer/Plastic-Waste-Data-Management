from conexao_bd import conectar_bd
 
def criar_tabelas(conexao):
    cursor = conexao.cursor()
 
    cursor.execute("""
        BEGIN
            EXECUTE IMMEDIATE 'DROP TABLE participacao_despejo_residuo_plastico';
        EXCEPTION
            WHEN OTHERS THEN
                IF SQLCODE != -942 THEN
                    RAISE;
                END IF;
        END;
    """)
 
    cursor.execute("""
        BEGIN
            EXECUTE IMMEDIATE 'DROP TABLE desperdicio_plastico_per_capita';
        EXCEPTION
            WHEN OTHERS THEN
                IF SQLCODE != -942 THEN
                    RAISE;
                END IF;
        END;
    """)
 
    cursor.execute("""
        CREATE TABLE participacao_despejo_residuo_plastico (
            Ano NUMBER,
            Pais VARCHAR2(100),
            Participacao_residuo_plastico NUMBER
        )
    """)
    
    cursor.execute("""
        CREATE TABLE desperdicio_plastico_per_capita (
            Ano NUMBER,
            Pais VARCHAR2(100),
            Desperdicio_per_capita NUMBER
        )
    """)
    
    conexao.commit()
    cursor.close()
 
conexao = conectar_bd("oracle.fiap.com.br", "1521", "orcl")  # Corrigido os parâmetros
 
if conexao:
    criar_tabelas(conexao)
    conexao.close()
    print("Tabelas criadas com sucesso!")
else:
    print("Não foi possível conectar ao banco de dados")