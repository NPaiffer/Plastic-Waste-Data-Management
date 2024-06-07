import pandas as pd

def exibir_dados_csv(caminho):
    df = pd.read_csv(caminho)
    print(df)

def menu():
    print("Menu de Consulta")
    print("1. Consultar dados de participação de despejo de resíduo plástico")
    print("2. Consultar dados de desperdício de plástico per capita")
    print("3. Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Dados de participação de despejo de resíduo plástico:")
            exibir_dados_csv('csv/2- participacao-despejo-residuo-plastico.csv')
        elif opcao == "2":
            print("Dados de desperdício de plástico per capita:")
            exibir_dados_csv('csv/4- desperdicio-plastico-per-capita.csv')
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
