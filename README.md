# SOC Log Analyzer 🔐

Analisador de logs de autenticação desenvolvido em Python para identificar atividades suspeitas, contabilizar tentativas de login e gerar alertas com base em regras simples de segurança.

## 🎯 Objetivo

Este projeto tem como objetivo praticar conceitos de Python e análise de logs utilizados na rotina de um Analista SOC (Security Operations Center).

## ⚙️ Funcionalidades

- Leitura de arquivos de log de autenticação.
- Contagem de falhas e sucessos de login.
- Contabilização de tentativas por endereço IP.
- Identificação do IP com maior número de falhas.
- Registro da primeira e da última falha por IP.
- Identificação de IPs que ultrapassam o limite configurado de falhas.
- Ordenação dos IPs suspeitos pelo número de falhas.
- Exibição da quantidade de logins bem-sucedidos por IP.
- Tratamento de linhas malformadas e ausência de falhas registradas.

## 🛠️ Tecnologias utilizadas

- Python 3
- Git
- GitHub
- Visual Studio Code

## 📂 Estrutura do projeto

```text
soc-log-analyzer/
├── logs/
│   └── auth.log
├── reports/
├── src/
│   └── analisador.py
├── .gitignore
└── README.md
```

## 🚀 Como executar

1. Instale o Python 3.
2. Clone o repositório:

```bash
git clone https://github.com/SOCReis/soc-log-analyzer.git
```

3. Entre na pasta do projeto:

```bash
cd soc-log-analyzer
```

4. Execute o analisador:

```bash
python src/analisador.py
```

## 🚨 Regra de detecção

O projeto utiliza um limite configurável para identificar endereços IP com muitas falhas de autenticação.

```python
LIMITE_FALHAS = 10
```

IPs com mais de 10 falhas são exibidos como suspeitos, ordenados pela quantidade de tentativas.

**Importante:** ultrapassar esse limite não confirma um ataque. Os resultados devem ser investigados considerando o contexto e outros registros de segurança.

## 📚 Conceitos praticados

- Manipulação de arquivos com `open()`.
- Estruturas de dados: dicionários, listas e tuplas.
- Contadores com `Counter`.
- Valores padrão com `defaultdict`.
- Laços `for` e condições `if`.
- List comprehension.
- Ordenação com `sorted()` e `lambda`.
- Análise e correlação básica de eventos de autenticação.

## 🔮 Próximas melhorias

- Detectar sequências de falhas seguidas de login bem-sucedido.
- Identificar tentativas de força bruta dentro de intervalos de tempo.
- Gerar relatórios em arquivos.
- Adicionar testes automatizados.
- Melhorar a classificação dos eventos suspeitos.

## ⚠️ Aviso

Projeto educacional desenvolvido para praticar análise de logs e fundamentos de cibersegurança. Utilize logs fictícios ou dados que você tenha autorização para analisar.

---

**Autor:** Samuel Reis

**Área de estudo:** Cibersegurança | Análise SOC