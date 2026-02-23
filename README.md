# Coleta de Dados Jurídicos

> Este documento visa simular uma situação real para coleta de dados jurídicos através de informações públicas a partir de sistemas externos (Ex.: Tribunais). O sistema consiste em realizar a coleta e disponibilizar o esquema de dados importante para informações de usuários.

## Desafio

Escolha **apenas um** dos sistemas abaixo:
- **Superior Tribunal de Justiça (STJ)**</br>
https://processo.stj.jus.br/processo/pesquisa/?aplicacao=processos.ea
- **Tribunal de Justiça do Estado do Rio Grande do Sul (TJRS)**</br>
https://www.tjrs.jus.br/novo/busca/?return=proc&client=wp_index#
- **Tribunal de Justiça do Estado do Pará (TJPA)**</br>
https://consulta-processual-unificada-prd.tjpa.jus.br/#/consulta

## Levantamento de Requisitos
- [x] Deve ser possível acessar o sistema escolhido;
-  Deve ser possível coletar dados de um processo jurídico:
- [x] Número do Processo;
- [x] Classe e/ou assunto;
- [x] Partes do processo;
- [x] Lista de movimentações (data + descrição);

*Recomenda-se priorizar soluções que não dependam de browser, sempre que possível

## Biblioteca Escolhida/Utilizada
- Selectolax -> Parse Otimizado, Scraping para larga escala, Baixo consumo de recursos (CPU, Memória, Threads).
- Requests -> Requisições HTTP simples, controle de headers.
- Tenacity -> Tratamento para lógicas de repetição

## Estrutura do Projeto
```
webscraping-coletadedadosjuridicos/
│
├── main.py
├── scraper.py
├── parser.py
├── http_client.py
├── .editorconfig (Arquivo para formatação/identação de texto)
├── README.md (Este documento)
└── requirements.txt
```
## Relatório e resultados

### Descrição da fonte e dos principais desafios técnicos encontrados
A fonte de dados escolhida foi o [Superior Tribunal de Justiça (STJ)](https://processo.stj.jus.br/processo/pesquisa/?aplicacao=processos.ea). A navegação do sistema ocorre por meio das páginas HTML renderizadas no servidor, o que permite a coleta de dados por meio de requisições HTTP tradicionais.

### Estratégias adotadas para realizar a coleta
Inicialmente estava pensando em utilizar BeautifulSoup(onde tenho habilidade/conhecimento), porém possuí um parsing pesado, alto consumo de memória e uma performance baixa. Comecei a estudar novas bibliotecas para efetuar a conclusão do desafio técnico, iniciei estudando a documentação da Selectolax. A biblioteca possuí uma alta performance, baixo consumo de memória e muito usada em crawles de alto volume.

A solução foi então projetada priorizando:
- simplicidade
- robustez
- facilidade em manutenções futuras
- performance

### Resultados obtidos com o protótipo
O protótipo foi capaz de coletar corretamente todos os dados:
- Número do Processo
- Classe e/ou assunto
- Partes do processo
- Lista de movimentações (data + descrição)
```
{
  "numero_processo": "XXXXXXX-XX.XXXX.X.XX.XXXX",
  "classe_assunto": "subject",
  "partes": {
    "AGRAVANTE": [...],
    "ADVOGADO": [...],
    "AGRAVADO": [...]
  },
  "movimentacoes": [...]
}
```

### Validações implementadas para garantir qualidade dos dados
Para garantir maior confiabilidade da coleta foram implementadas algumas validações.

#### Validação da entrada do usuário
O sistema verifica se o número informado corresponde a algum formato conhecido. Caso contrário, é gerada uma exceção indicando formato inválido.

#### Normalização de texto
Os textos extraídos passam por:
- remoção de espaços extras
- limpeza de caracteres
- padronização

Exemplo:
```
text(strip=True)
```

#### Estrutura consistente de saída
Os dados são retornados em formato estruturado:
```
dict / JSON
```
Podendo facilitar:
- Armazenamento
- Integração
- Processamento posterior

### Possíveis melhorias para reduzir falhas recorrentes e facilitar manutenção
Apesar do protótipo atender ao desafio, algumas melhorias podem tornar o sistema mais robusto.

#### Monitoramento de mudanças no HTML
Criar testes automatizados para validar a presença de campos essenciais e funcionamento dos seletores.

#### Sistemas de retries e tratamentos de erros
Adicionar lógica para novas tentativas e tratamento de erros inesperados.
- retry exponencial
- timeout ajustável
- tratamento de erros HTTP

*Podendo evitar falhas causadas por instabilidade do servidor.

#### Logging estruturado
Registrar eventos:
- Falha de coleta
- Campos não encontrados
- Respostas inesperadas

*Facilitando debugging e manutenção.

## Pré-requisitos
Antes de começar, verifique se você atendeu aos seguintes requisitos:
- Possuir o Ambiente de Desenvolvimento `<Visual Studio Code ou outra IDE>`.
- Python3 `<Python3 instalado em sua máquina>`
- Instalar Requerimentos `<Bibliotecas listadas no requeriments.txt pip install -r requirements.txt>`
- Requisitos do Sistema `<4 GB+ RAM, 1 GB of available disk space minimum`

## Desenvolvedor
Email: contato@pfelix.com.br</br>
LinkedIn: [Pedro Félix](https://www.linkedin.com/in/pedrovsfelix/)

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/pedrovsfelix" title="Aluno">
        <img src="https://avatars.githubusercontent.com/u/93714667?v=4" width="100px;" alt="Pedro Félix"/><br>
        <sub>
          <b>Pedro Félix</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
