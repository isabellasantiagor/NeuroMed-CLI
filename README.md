# == NeuroMed CLI ==

![CI](https://github.com/isabellasantiagor/NeuroMed-CLI/actions/workflows/ci.yml/badge.svg)

O NeuroMed CLI é uma aplicação de linha de comando desenvolvida para o auxílio no monitoramento e controle de medicamentos importantes para a saúde do usuário. 

Pessoas que tomam múltiplos medicamentos diários podem enfrentar dificuldades em manter a regularidade no seu uso. Isso pode acontecer pela condição que a faz ter uma memória impactada ou até mesmo por condições de saúde ou idade. E isso ocasiona esquecimentos, atrasos ou uso incorreto, impactando diretamente a saúde e qualidade de vida.

## Qual problema estou tentando resolver? 

A falta de controle ou dificuldade para monitoramento de medicamentos diários ou não necessários para a saúde do usuário.

## Público-alvo (Quem é afetado por esse problema?)

- Pessoas neurodivergentes (TDAH, autismo, etc);
- Idosos;
- Pessoas com múltiplos medicamentos diários;

## Como a minha aplicação ajuda, mesmo que de forma simples?

O NeuroMed CLI é uma aplicação simples em Python com interface de linha de comando (CLI) que permite organizar medicamentos, horários e dosagens, ajudando o usuário a manter uma rotina mais consistente e segura.

## Funcionalidades principais

- Cadastro de medicamentos com nome, horário e dosagem
- Listagem de medicamentos cadastrados
- Remoção de medicamentos
- Validação de dados (horário, dosagem, duplicidade)
- Persistência de dados em arquivo JSON

## Tecnologias utilizadas

- Linguagem: Python 3.14;
- Dependências: Ver (requirements.txt)
- Testes automatizados: Pytest;
- Lint/ Análise estática: Ruff;
- Armazenamento de dados: JSON

> Observação: 

Os dados dos medicamentos são armazenados no arquivo `data/medications.json`.

Esse arquivo é criado automaticamente ao executar o sistema pela primeira vez.

## Instruções de instalação:

1. Pré-requisitos
- Ter o Python instalado(v3.10 ou superior);
- Ter o Git configurado;

2. Instalação e Configuração
  1. Clone o repositório

```bash
git clone https://github.com/isabellasantiagor/NeuroMed-CLI.git
cd NeuroMed-CLI
```
  2. Instale as dependências
```bash
pip install -r requirements.txt
```
## Instruções de execução:
  1. Execute o sistema com:
```bash
python -m app.main
```
## Intruções para rodar os testes:

  1. Execute:

```bash
pytest -v
```
## Instruções para rodar o lint

Execute:

```bash
ruff check .
```

## Versão atual: 1.0.0

## Autor: 
Isabella Santiago.

## Repositório

- Disponível em:

https://github.com/isabellasantiagor/NeuroMed-CLI



