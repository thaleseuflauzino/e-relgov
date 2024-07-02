# Projeto de Raspagem de Dados do Banco Central do Brasil

Este projeto realiza a raspagem de dados da agenda do Presidente do Banco Central do Brasil usando Scrapy e processa os dados extraídos para formatos Excel (.xlsx) e Markdown (.md).

## Pré-requisitos

- Python 3.7+
- pip

## Configuração do Ambiente

## 1. Clone o repositório:
```sh
   git clone https://github.com/thaleseuflauzino/e-relgov.git
   cd e-relgov
   ```
## 2. Crie um ambiente virtual:
```sh
  python -m venv venv
  ```
## 3. Ative o ambiente virtual:

No Windows (PowerShell):
```sh
.\venv\Scripts\Activate.ps1
```
No macOS/Linux:
```sh
source venv/bin/activate
```
## 4. Instale as dependências:

```sh
pip install -r requirements.txt
```
## 5. Executando a Raspagem
Navegue até o diretório do projeto Scrapy:

```sh
cd bcb
```
Execute o spider do Scrapy para coletar os dados:

```sh
scrapy crawl agenda_api -o output.json
```
## 6. Processando os Dados
Execute o script de processamento para gerar os arquivos .xlsx e .md:
```sh
python parse.py
```
##### Após isso, será gerado um eventos_processados.md e um eventos_processados.xlsx, permitindo assim, ao usuário, escolher a forma que preferir, ler todo o projeto.

Estrutura do Projeto

```plaintext
e-relgov/
├── bcb/
│   ├── spiders/
│   │   ├── agenda_api.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── ...
├── output.json
├── parse.py
├── requirements.txt
└── README.md


Descrição dos Arquivos
- bcb/: Diretório do projeto Scrapy.
- spiders/: Contém o spider agenda_api.py que realiza a raspagem dos dados.
- output.json: Arquivo JSON gerado pelo spider contendo os dados raspados.
- parse.py: Script Python para processar os dados do JSON e salvar em .xlsx e .md.
- requirements.txt: Lista de dependências do projeto.
- README.md: Este arquivo de documentação.
