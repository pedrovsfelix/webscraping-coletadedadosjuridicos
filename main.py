from http_client import HttpClient
from scraper import STJScraper
import json

if __name__ == "__main__":
  numero = input("Digite o número do processo: ")
  client = HttpClient()
  scraper = STJScraper()
  result = scraper.search_process(numero)
  try:
    html = client.get(HttpClient.url)
    print('Tamanho do HTML retornado: ', len(html))
    print(numero)
  except Exception as e:
    print('Erro ao consultar o arquivo HTML')

  print(json.dumps(result, indent=2, ensure_ascii=False))
