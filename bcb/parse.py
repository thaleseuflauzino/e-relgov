from bs4 import BeautifulSoup
from datetime import datetime
import locale
import re
import pandas as pd
import json
# Defining locale for Brazilian Portuguese
locale.setlocale(locale.LC_TIME, 'pt_BR')

# Function to remove HTML tags
def remove_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    cleaned_text = soup.get_text(separator=" ")
    cleaned_text = ' '.join(cleaned_text.split())  # Remove extra spaces
    return cleaned_text

# Function to format date
def formatar_data(data_evento):
    data_datetime = datetime.strptime(data_evento, "%Y-%m-%dT%H:%M:%SZ")
    data_formatada = data_datetime.strftime("%d de %B de %Y")
    return data_formatada


# Function to process JSON and save back to file
def processar_e_salvar_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        try:
            json_data = json.load(file)
            
            for item in json_data:
                item['dataEvento'] = formatar_data(item['dataEvento'])
                
                if 'descricao' in item:
                    item['descricao'] = remove_html_tags(item['descricao'])            
            with open(filename, 'w', encoding='utf-8') as outfile:
                json.dump(json_data, outfile, indent=4, ensure_ascii=False)
            
            print(f"Dados processados e salvos de volta no arquivo '{filename}'.")
        
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON: {e}")

# Replace with your actual JSON file path
filename = r'C:\Users\thale\OneDrive\Área de Trabalho\unb\seletivo\bcb\output.json'

# Process and save the JSON
processar_e_salvar_json(filename)

import pandas as pd
import json

# Função para carregar dados de um arquivo JSON
def carregar_dados_json(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as file:
        dados = json.load(file)
    return dados

# Função para limpar a descrição removendo tags HTML (caso necessário)
def limpar_descricao(descricao):
    # Aqui você pode adicionar lógica para limpar as tags HTML, se necessário
    return descricao

# Função para processar os dados e retornar um DataFrame pandas
def processar_dados_json(dados):
    eventos = []
    for evento in dados:
        evento_limpo = {
            "dataEvento": evento["dataEvento"],
            "descricao": limpar_descricao(evento["descricao"]),
            "autoridade": evento["autoridade"],
            "cargo": evento["cargo"],
            "orgao": evento["orgao"],
        }
        eventos.append(evento_limpo)
    
    # Criar DataFrame
    df = pd.DataFrame(eventos)
    return df

# Função para formatar descrição em Markdown com ênfase em "Manhã", "Tarde" e "Noite"
def formatar_descricao_markdown(descricao):
    descricao_formatada = descricao.replace('Manhã', '<br>**Descrição**<br>**Manhã**<br>').replace('Tarde', '<br>**Tarde**<br>').replace('Noite', '<br>**Noite**<br>')
    return descricao_formatada

# Nome do arquivo JSON
nome_arquivo_json = 'output.json'

# Carregar dados do arquivo JSON
dados_json = carregar_dados_json(nome_arquivo_json)

# Processar dados e criar DataFrame
df_eventos = processar_dados_json(dados_json)

# Salvando em Excel
nome_arquivo_excel = 'eventos_processados.xlsx'
df_eventos.to_excel(nome_arquivo_excel, index=False, engine='openpyxl')

print(f"Dados processados salvos em {nome_arquivo_excel}")

# Salvando em Markdown
nome_arquivo_md = 'eventos_processados.md'
with open(nome_arquivo_md, 'w', encoding='utf-8') as file:
    for index, row in df_eventos.iterrows():
        file.write(f"### {row['dataEvento']}\n\n")
        file.write(f"**Autoridade:** {row['autoridade']}\n")
        file.write(f"<br> **Cargo:** {row['cargo']}\n")
        file.write(f"<br> **Órgão:** {row['orgao']}\n\n")
        file.write(formatar_descricao_markdown(row['descricao']) + "\n\n")
        
print(f"Dados processados salvos em {nome_arquivo_md}")
