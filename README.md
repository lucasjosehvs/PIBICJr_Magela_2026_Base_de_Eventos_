# Projeto Magela

Pipeline em Python para extração, limpeza, normalização e deduplicação de
**registros de eventos acadêmicos** a partir de currículos Lattes (CNPq),
produzindo um dataset consolidado para análise — incluindo contagens de
frequência por nome de evento e por ano.

Escala de referência: **~9 milhões de currículos** em formato ZIP.

---
## Pipeline

### Fase 1 — Extração de XML 

```bash
python extratorEventosPrimeiraLeitura.py   # AO — primeira leitura
python extratorEventosFinal.py             # AU — leitura final
python pegarAlgumasLinhas.py               # AO — amostragem (usa pandas)
python pegararquivos.py                    # AU — amostragem (usa pandas)
```

### Fase 1.5 — Limpeza estrutural pós-extração

Aplicada em sequência sobre o CSV bruto de eventos:

1. `removerEventosSemNome.py` — remove eventos sem nome / com dados vazios
2. `limpezaCidadeEventos.py` — normaliza `CIDADE-DO-EVENTO` (mantém apenas o
   texto antes de sinais de pontuação)
3. `normalizacaoGeral.py` — normalização geral (minúsculas, remoção de
   acentos, pontuação, algarismos e espaços extras)
4. `geradorConjuntos.py` — gera os "Conjuntos" (granularidade para
   deduplicação)
5. `removerDuplicatas.py` — remoção de duplicatas
6. `lerLinhas.py` — inspeção/amostragem de linhas

Os **Conjuntos** representam níveis crescentes de granularidade de chave:

| Conjunto | Chave de deduplicação |
|---|---|
| 1 | `NOME-DO-EVENTO` |
| 2 | `NOME-DO-EVENTO \| ANO-DO-EVENTO` |
| 3 | `NOME-DO-EVENTO \| ANO-DO-EVENTO \| PAIS-DO-EVENTO` |
| 4 | `NOME-DO-EVENTO \| ANO-DO-EVENTO \| PAIS-DO-EVENTO \| CIDADE-DO-EVENTO` |

`Conjunto4` é o dataset deduplicado mais completo (~26M linhas / ~2GB),
gerado a partir de um CSV normalizado de ~80M linhas / ~10GB.

---

## Antes de rodar qualquer script

Não há gerenciador de pacotes, build step, testes automatizados nem
linter configurado. Os scripts são standalone e **os caminhos são
hardcoded no topo de cada arquivo**:

```
pastaCurriculos, saidaCSV, base_dir, curriculos,
result_dir, caminhoEntrada, caminhoSaida
```

Edite esses valores conforme o layout local dos dados antes de executar.

Recomendação do projeto: **valide todo script novo contra uma amostra real**
antes de rodar contra o corpus completo (~9M currículos) — evita horas de
processamento desperdiçadas em caso de bug.

---

## Formato dos dados

**Entrada:** currículos Lattes em ZIP, um XML por ZIP, nomeado por
identificador, em subpastas de dois dígitos:
`pastaCurriculos/{00-99}/{identificador}.zip`

**Colunas do CSV de eventos:**
`IDENTIFICADOR, TIPO-REGISTRO, NOME-DO-EVENTO, TIPO-DE-EVENTO,
CLASSIFICACAO-DO-EVENTO, ANO-DO-EVENTO, PAIS-DO-EVENTO, CIDADE-DO-EVENTO,
LOCAL-DO-EVENTO, CODIGO-INSTITUICAO-PROMOTORA, INSTITUICAO-PROMOTORA,
DURACAO-EM-SEMANAS`

**Colunas do CSV de artigos** (`extrator_preprint.py`): `TITULO-DO-ARTIGO,
ANO, NATUREZA, LOCAL-NATUREZA, MEIO-DE-DIVULGACAO, ...` (24 colunas)

**`exemploConjunto4.csv`:** `NOME-DO-EVENTO|ANO-DO-EVENTO|PAIS-DO-EVENTO|CIDADE-DO-EVENTO`
(delimitado por `|`)

**`nomeEstado.csv`:** `NOME-DO-EVENTO;ESTADO;STATUS-MAPEAMENTO`
(delimitado por `;`)

**`contagemPor*.csv`:** `OCORRENCIAS;NOME-DO-EVENTO[;CIDADE-DO-EVENTO|ESTADO]`
(delimitado por `;`, ordenado de forma decrescente)

> **Atenção aos delimitadores.** Eles diferem por tipo de arquivo:
> `;` nos scripts de eventos, `,` em `extrator_preprint.py`, `|` em
> `exemploConjunto4.csv`. Misturar delimitadores corrompe o parsing
> silenciosamente (o `csv.DictReader` trata o cabeçalho inteiro como uma
> única chave e gera `KeyError`s difíceis de rastrear).

---

## Dependências

- Python 3.10+ (usa type hints como `tuple[str, str]`)
- `pandas` — apenas em `pegarAlgumasLinhas.py` / `pegararquivos.py`
- `nltk` — stopwords em português e inglês (usado em `normalizacaoGeral.py`)
- Todo o resto é biblioteca padrão: `csv`, `os`, `io`, `time`, `zipfile`,
  `xml.etree.ElementTree`, `glob`, `json`, `unicodedata`, `hashlib`,
  `sqlite3`, `urllib.request`, `collections.defaultdict`
- Base de referência de municípios do IBGE:
  [`kelvins/municipios-brasileiros`](https://github.com/kelvins/municipios-brasileiros)

---

## Convenções de código

- Nomes de variáveis e funções em português (`escritor_eventos`,
  `abridorDosZIP`, `lerOsXML`)
- `csv.reader` / `csv.writer` com acesso **posicional** (não
  `DictReader`/`DictWriter`), por performance em escala
- Processamento **linha a linha** (streaming), sem carregar o dataset
  inteiro em memória
- Marcador `##f` no topo dos arquivos de saída
- Colunas sobrescritas *in place* durante normalização (sem duplicar em
  colunas `-NORM`)
- Todas as colunas — inclusive `IDENTIFICADOR` e `TIPO-REGISTRO` — são
  preservadas para fins de auditoria
- Constantes de controle recorrentes: `LIMITE_TESTE` (amostragem),
  `INTERVALO_LOG` e `INTERVALO_FLUSH` (progresso/flush periódico)

---

## Problemas conhecidos / cuidados

- **`ORGANIZACAO-DE-EVENTO` sem `NOME-DO-EVENTO`** — nesse bloco do schema
  Lattes o título vem em `TITULO`, não em `NOME-DO-EVENTO`. Corrigido em
  `extratorEventosFinal.py` (AU) com `db.get('TITULO', '')`. Exige
  reprocessamento completo do corpus para valer para dados já extraídos.
- **Descompasso de schema entre `geradorConjuntos.py` e
  `removerDuplicatas.py`** — o primeiro escreve saída de uma coluna
  delimitada por `|`; o segundo espera 12 colunas delimitadas por `;`.
  A geração real do `Conjunto4` provavelmente usou uma variante ainda não
  localizada, com deduplicação via `set()` sobre linhas cruas — pendente de
  confirmação.
- **Remoção de stopwords em colunas de nome próprio** — `nltk` aplicado sem
  distinção de coluna em `normalizacaoGeral.py` corrompe nomes de cidade e
  instituição (ex.: "São José dos Campos" perde o "dos"). Existe apenas uma
  proteção parcial (`.discard('sao')`).
- **Cidades ambíguas no mapeamento de UF** — ~4,5% dos nomes distintos de
  cidade existem em mais de uma UF; são marcados como `AMBIGUO` em vez de
  resolvidos por heurística, para preservar integridade dos dados.

---

## Sobre este repositório

Dataset e scripts fazem parte de um projeto de mapeamento de eventos
acadêmicos a partir da base pública de currículos Lattes/CNPq. Contribuições
e revisões de schema são bem-vindas — abra uma *issue* descrevendo o
problema encontrado e, se possível, a amostra de dado que reproduz o caso.
