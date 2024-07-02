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
filename = r'C:\Users\thale\OneDrive\Área de Trabalho\unb\seletivo\output.json'

# Process and save the JSON
processar_e_salvar_json(filename)
