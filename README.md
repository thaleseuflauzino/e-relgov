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
##### Após isso, serão gerados os arquivos eventos_processados.md e eventos_processados.xlsx, permitindo ao usuário escolher a forma preferida para ler os dados.

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
├── parse.py
├── requirements.txt
└── README.md


Descrição dos Arquivos
- bcb/: Diretório do projeto Scrapy.
- spiders/: Contém o spider agenda_api.py que realiza a raspagem dos dados.
- parse.py: Script Python para processar os dados do JSON e salvar em .xlsx e .md.
- requirements.txt: Lista de dependências do projeto.
- README.md: Este arquivo de documentação.
``` 
## Arquivos Gerados na Execução
Na pasta "arquivos gerados na execução", estão os arquivos que serão gerados após a execução correta do projeto, permitindo análise e comparação.

## Observações sobre a Implementação
O projeto incluía uma etapa onde era necessário separar o "local da reunião" dos dados fornecidos. No entanto, a API utilizada não forneceu esta informação específica. Por esse motivo, optei por não implementar algoritmos de busca para determinar o local da reunião, devido à sua potencial instabilidade e risco de inconsistências nos resultados.

A decisão foi tomada para garantir a integridade e a precisão dos dados processados, mantendo a confiabilidade da aplicação. 
