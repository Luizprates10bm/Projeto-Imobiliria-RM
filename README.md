# Sistema de Orçamentos - Imobiliária R.M

Este projeto é uma aplicação em Python desenvolvida para automatizar o cálculo de orçamentos de aluguel, aplicando regras de negócio específicas para diferentes tipos de imóveis.

# Funcionalidades
- **Cálculo de Aluguel:** Define valores base para Apartamentos, Casas e Estúdios.
- **Regras de Negócio:** - Adicionais por quartos e vagas de garagem.
  - Desconto de 5% para apartamentos (sem crianças).
  - Regra especial de garagem para Estúdios.
- **Taxa de Contrato:** Parcelamento de R$ 2.000,00 em até 5x.
- **Exportação:** Gera um relatório anual detalhado em formato `.csv`.

# Tecnologias e Conceitos
- **Linguagem:** Python 3.
- **Paradigma:** Orientação a Objetos (POO).
- **Biblioteca:** `csv` (nativa do Python).
- **Versionamento:** Git e GitHub.

# Como Executar
1- Garante que tem o Python instalado.
2- Faz o download do arquivo `imobiliaria.py`.
3- No terminal, executa: `python imobiliaria.py`.
4- Segue as instruções no ecrã e consulta o arquivo `orcamento_anual.csv` gerado no final.
