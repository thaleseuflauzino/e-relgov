from bs4 import BeautifulSoup
from datetime import datetime
import locale
import pandas as pd
import json

locale.setlocale(locale.LC_TIME, 'pt_BR')

def remove_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    cleaned_text = soup.get_text(separator=" ")
    cleaned_text = ' '.join(cleaned_text.split())  # Remove espaços extras
    return cleaned_text

def formatar_data(data_evento):
    data_datetime = datetime.strptime(data_evento, "%Y-%m-%dT%H:%M:%SZ")
    data_formatada = data_datetime.strftime("%d de %B de %Y")
    return data_formatada

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

filename = r'C:\Users\thale\OneDrive\Área de Trabalho\unb\seletivo\bcb\output.json'

processar_e_salvar_json(filename)

def carregar_dados_json(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as file:
        dados = json.load(file)
    return dados

def limpar_descricao(descricao):
    return descricao

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
    
    df = pd.DataFrame(eventos)
    df['dataEvento'] = pd.to_datetime(df['dataEvento'], format='%d de %B de %Y')
    df = df.sort_values(by='dataEvento').reset_index(drop=True)
    df['dataEvento'] = df['dataEvento'].dt.strftime('%d de %B de %Y')
    
    eventos_ordenados = df.to_dict(orient='records')
    with open(filename, 'w', encoding='utf-8') as outfile:
        json.dump(eventos_ordenados, outfile, indent=4, ensure_ascii=False)
    
    return df

def formatar_descricao_markdown(descricao):
    descricao_formatada = descricao.replace('Manhã', '<br>**Manhã**<br>').replace('Tarde', '<br>**Tarde**<br>').replace('Noite', '<br>**Noite**<br>')
    return descricao_formatada

nome_arquivo_json = 'output.json'

dados_json = carregar_dados_json(nome_arquivo_json)

df_eventos = processar_dados_json(dados_json)

nome_arquivo_excel = 'eventos_processados.xlsx'
df_eventos.to_excel(nome_arquivo_excel, index=False, engine='openpyxl')

print(f"Dados processados salvos em {nome_arquivo_excel}")

nome_arquivo_md = 'eventos_processados.md'
with open(nome_arquivo_md, 'w', encoding='utf-8') as file:
    for index, row in df_eventos.iterrows():
        file.write(f"### {row['dataEvento']}\n\n")
        file.write(f"**Autoridade:** {row['autoridade']}\n")
        file.write(f"<br> **Cargo:** {row['cargo']}\n")
        file.write(f"<br> **Órgão:** {row['orgao']}\n\n")
        file.write(formatar_descricao_markdown(row['descricao']) + "\n\n")

print(f"Dados processados salvos em {nome_arquivo_md}")
