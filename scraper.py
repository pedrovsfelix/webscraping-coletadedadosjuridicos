from http_client import HttpClient
from parser import STJParser

class STJScraper:
  BASE_URL = "https://processo.stj.jus.br/processo/pesquisa/"

  def __init__(self):
    self.client = HttpClient()
    self.parser = STJParser()

  def search_process(self, numero):
    numero_tratado = ''.join(filter(str.isdigit, str(numero)))
    tam = len(numero_tratado)
    if tam == 12:
      url = f"{self.BASE_URL}?aplicacao=processos.ea&num_registro={numero_tratado}"
    elif tam == 20:
      url = f"{self.BASE_URL}?aplicacao=processos.ea&tipoPesquisa=tipoPesquisaNumeroUnico&termo={numero_tratado}"
    else:
      raise ValueError(f"Número de processo inválido.")

    html = self.client.get(url)
    data = self.parser.parse(html)

    return data
