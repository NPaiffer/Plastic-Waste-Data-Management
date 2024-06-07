import oracledb
import json

def carregar_credenciais(cred_file):
    with open(cred_file, 'r') as file:
        return json.load(file)
    
def conectar_bd(endereco, porta, sid, cred_file= 'credenciais.json'):
    creds = carregar_credenciais(cred_file)
    usuario = creds['user']
    senha = creds['pass']
    dsn_tns = oracledb.makedsn(endereco, porta, sid)

    try:
        conexao = oracledb.connect(user=usuario, password=senha,dsn=dsn_tns)
        print("Conexao bem-sucedida!")
        return conexao
    except oracledb.DatabaseError as e:
        error, = e.argsprint("Erro de conexao:",error.message)
        return None