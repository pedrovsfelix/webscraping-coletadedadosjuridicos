from http_client import HttpClient
from scraper import STJScraper
import json

if __name__ == "__main__":
  def solicitar_processo():
    message = """
    Informe um identificador de processo do STJ.

    Formatos aceitos:
    REsp 123456                -> Processo no STJ
    XXXXXXX-XX.XXXX.X.XX.XXXX  -> Número Único de Processo (NUP)
    2007/0249585-9             -> Número de registro no STJ
    200702495859               -> Processo na origem
    """
    print(message)
    return input("Processo: ").strip()
  numero = solicitar_processo()
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
