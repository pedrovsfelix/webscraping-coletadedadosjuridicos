import re
from http_client import HttpClient
from parser import STJParser

class STJScraper:
  BASE_URL = "https://processo.stj.jus.br/processo/pesquisa/"

  def __init__(self):
    self.client = HttpClient()
    self.parser = STJParser()

  def search_process(self, numero):
    url = self._build_url(str(numero).strip())
    html = self.client.get(url)
    data = self.parser.parse(html)
    return data

  def _build_url(self, numero):
    clean_input = re.sub(r'[.\-/]', '', numero)

    # Número Único XXXXXXX-XX.XXXX.X.XX.XXXX
    if re.fullmatch(r'\d{20}', clean_input):
      return f"{self.BASE_URL}?aplicacao=processos.ea&tipoPesquisa=tipoPesquisaNumeroUnico&termo={clean_input}"

    # Número do Processo REsp 123456, HC 271165, AG 435459
    if re.search(r'[a-zA-Z]', clean_input):
      return f"{self.BASE_URL}?aplicacao=processos.ea&num_processo={clean_input}"

    # Número do Registro 2007/0249585-9
    if re.fullmatch(r'\d{12}', clean_input):
      return f"{self.BASE_URL}?aplicacao=processos.ea&num_registro={clean_input}"

    raise ValueError(f"Formato de número de processo não reconhecido: {numero}")
