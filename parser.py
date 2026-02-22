from selectolax.parser import HTMLParser

class STJParser:
  def parse(self, html):
    tree = HTMLParser(html)
    data = {}

    # Número do Processo
    case_number = (
      tree.css_first(
        '#idProcessoDetalhesBloco1 a[href*="tipoPesquisaNumeroUnico"]'
      )
    )
    data["Número do processo"] = case_number.text(strip=True) if case_number else None

    # Classe e/ou assunto
    subject = tree.css(
      '#idProcessoDetalheAssuntos span[class*="Item"], #idProcessoDetalheAssuntosComplementares span[class*="Item"]'
    )
    clear_text = [span.text(strip=True) for span in subject if span.text(strip=True)]
    data["Classe e/ou assunto"] = " ".join(clear_text) if clear_text else None

    # Partes do Processo
    parts = {}
    block_parts = tree.css_first('#idDetalhesPartesAdvogadosProcuradores')

    if block_parts:
      line_parts = block_parts.css('.classDivLinhaDetalhes')
      for line in line_parts:
        label_node = line.css_first('.classSpanDetalhesLabel')
        text_node = line.css_first('.classSpanDetalhesTexto a')

        if label_node and text_node:
          paper = label_node.text(strip=True).replace(':', '')
          name = text_node.text(strip=True)

          if paper not in parts:
            parts[paper] = []

          parts[paper].append(name)

    data["Partes"] = parts

    return data
