from http_client import HttpClient

if __name__ == "__main__":
  client = HttpClient()
  try:
    html = client.get(HttpClient.url)
    print('Tamanho do HTML retornado: ', len(html))
  except Exception as e:
    print('Erro ao consultar o arquivo HTML')
