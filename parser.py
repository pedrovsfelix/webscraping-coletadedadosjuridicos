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
    data["numero_processo"] = case_number.text(strip=True) if case_number else None

    # Classe e/ou assunto
    subject = tree.css(
      '#idProcessoDetalheAssuntos span[class*="Item"], #idProcessoDetalheAssuntosComplementares span[class*="Item"]'
    )
    clear_text = [span.text(strip=True) for span in subject if span.text(strip=True)]
    data["classe_assunto"] = " ".join(clear_text) if clear_text else None

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

    data["partes"] = parts

    # Lista de Movimentações (data + descrição)
    list_transaction = []
    line_phase = tree.css('.classDivFaseLinha')

    for line in line_phase:
      date_node = line.css_first('.classSpanFaseData')
      hour_node = line.css_first('.classSpanFaseHora')
      text_node = line.css_first('.classSpanFaseTexto')

      if date_node and text_node:
        date = date_node.text(strip=True)
        hour = hour_node.text(strip=True) if hour_node else ""
        description = text_node.text(strip=True)

        list_transaction.append({
          "data": date,
          "hora": hour,
          "descrição": description
        })

    data["movimentacoes"] = list_transaction

    return data
