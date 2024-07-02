import scrapy
from datetime import datetime, timedelta
import json

class AgendaSpider(scrapy.Spider):
    name = 'agenda_api'
    start_date = datetime(2023, 2, 28)  # Data de início ajustada
    end_date = datetime(2024, 6, 28)    # Data de fim ajustada
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }

    def start_requests(self):
        delta = timedelta(days=1)
        current_date = self.start_date
        while current_date <= self.end_date:
            formatted_date = current_date.strftime('%Y-%m-%d')
            url = f'https://www.bcb.gov.br/api/servico/sitebcb/agendadiretoria?lista=Agenda%20da%20Diretoria&inicioAgenda=%27{formatted_date}%27&fimAgenda=%27{formatted_date}%27'
            yield scrapy.Request(url, self.parse)
            current_date += delta
    def parse(self, response):
        data = response.json()['conteudo']
        for item in data:
            if item['autoridade'] == "Roberto Campos Neto":
                yield {
                    'dataEvento': item['dataEvento'],
                    'descricao': item['descricao'],
                    'autoridade': item['autoridade'],
                    'cargo': 'Presidente do Banco Central do Brasil',
                    'orgao': 'Banco Central do Brasil',
                }
        