# Gerenciamento-de-Dados-de-Desperdicio-de-Plastico
Este projeto tem como objetivo gerenciar dados relacionados ao desperdício de resíduos plásticos em diferentes países. Utiliza-se um banco de dados Oracle para armazenar os dados e scripts em Python para criar tabalas, inserir dados a partir de arquivos CSV e fornecer uma interface de consulta. Estudos sobre gestão de resíduos plásticos.
 
# Integrantes: RM552535 Melissa | RM554145 Nicolas
 
# Descrição
Este projeto tem como objetivo gerenciar dados relacionados ao despejo e desperdício de resíduos plásticos em diferentes países. Utiliza-se um banco de dados Oracle para armazenar os dados e scripts em Python para criar tabelas, inserir dados a partir de arquivos CSV e fornecer uma interface de consulta. O projeto é ideal para análises ambientais e estudos sobre a gestão de resíduos plásticos.
# Estrutura do Projeto
- `conexao_bd.py`: Este script contém as funções para carregar credenciais do banco de dados a partir de um arquivo JSON e estabelecer a conexão com o banco de dados Oracle.
- `criar_tabelas.py`: Este script cria as tabelas no banco de dados necessárias para armazenar os dados de participação no despejo de resíduos plásticos e desperdício de plástico per capita.
- `inserir_dados.py`: Este script lê os dados de arquivos CSV e insere os registros nas tabelas do banco de dados.
- `menu_consulta.py`: Este script fornece uma interface de menu para exibir os dados dos arquivos CSV.
- `credenciais.json`: Arquivo JSON que armazena as credenciais do banco de dados.
- `csv/`: Diretório contendo os arquivos CSV com os dados a serem inseridos no banco de dados.
  - `2- participacao-despejo-residuo-plastico.csv`
  - `4- desperdicio-plastico-per-capita.csv`
- `script.sql`: Script SQL para a criação das tabelas diretamente no banco de dados.
# Funcionalidades
1. **Conexão com o Banco de Dados**:
    - Carrega credenciais do arquivo `credenciais.json`.
    - Estabelece conexão com o banco de dados Oracle.
2. **Criação de Tabelas**:
    - Cria as tabelas `participacao_despejo_residuo_plastico` e `desperdicio_plastico_per_capita`.
3. **Inserção de Dados**:
    - Lê dados dos arquivos CSV.
    - Insere os dados nas tabelas do banco de dados.
4. **Consulta de Dados**:
    - Fornece um menu para exibir os dados dos arquivos CSV.

### Considerações Finais
Este projeto foi desenvolvido para fins de estudos, mas também para praticar e facilitar a gestão e análise de dados relacionados ao despejo e desperdício de resíduos plásticos. Com o uso de um banco de dados Oracle, permite um armazenamento eficiente e consultas rápidas aos dados inseridos.
