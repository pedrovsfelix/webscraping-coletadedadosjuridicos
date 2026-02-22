from selectolax.parser import HTMLParser

class STJParser:
  def parse(self, html):
    tree = HTMLParser(html)

    nprocesso = (
      tree.css_first('#idProcessoDetalhesBloco1 a[href*="tipoPesquisaNumeroUnico"]')
    )

    return {
      "numero_processo": nprocesso.text(strip=True) if nprocesso else None
    }
