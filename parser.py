from selectolax.parser import HTMLParser

class STJParser:
  def parse(self, html):
    tree = HTMLParser(html)

    nprocesso = (
      tree.css_first(
        '#idProcessoDetalhesBloco1 a[href*="tipoPesquisaNumeroUnico"]'
      )
    )

    subject = tree.css(
      '#idProcessoDetalheAssuntos span[class*="Item"], #idProcessoDetalheAssuntosComplementares span[class*="Item"]'
    )

    clear_text = [span.text(strip=True) for span in subject if span.text(strip=True)]
    subject_text = " ".join(clear_text) if clear_text else None

    return {
      "Número do processo: ": nprocesso.text(strip=True) if nprocesso else None,
      "Classe e/ou assunto: ": subject_text
    }
