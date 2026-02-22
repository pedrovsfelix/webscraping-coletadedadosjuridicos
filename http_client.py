import requests
from tenacity import retry, stop_after_attempt, wait_exponential

class HttpClient:
  url = "https://processo.stj.jus.br/processo/pesquisa/?aplicacao=processos.ea"
  def __init__(self):
    self.session = requests.Session()
    self.session.headers.update({
      "User-Agent": "Mozilla/5.0"
    })

  @retry(stop=stop_after_attempt(3), wait=wait_exponential())
  def get(self, url):
    print('Acessando o sistema do STJ: {url}')
    response = self.session.get(url, timeout=30)
    response.raise_for_status()
    print('Sistema acessado!')
    return response.text
