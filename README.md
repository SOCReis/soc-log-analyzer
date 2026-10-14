# SOC Log Analyzer 🔐

Projeto educacional desenvolvido em Python para praticar conceitos de análise de logs e cibersegurança, com foco nas atividades de um analista SOC (*Security Operations Center*).

## 🎯 Objetivo

Desenvolver uma ferramenta capaz de analisar registros de autenticação, contabilizar falhas de login e identificar endereços IP que apresentam atividades potencialmente suspeitas.

## 🚀 Funcionalidades

- [x] Ler registros de autenticação a partir de um arquivo.
- [x] Percorrer os registros linha por linha.
- [x] Identificar tentativas de autenticação malsucedidas.
- [x] Contabilizar o total de falhas de autenticação.
- [x] Contar automaticamente as falhas por endereço IP.
- [x] Identificar o IP com a maior quantidade de falhas.
- [x] Exibir as estatísticas no terminal.
- [ ] Identificar possíveis padrões de força bruta (*brute force*).
- [ ] Gerar relatórios de análise em arquivos `.txt`.
- [ ] Melhorar o tratamento de erros e a validação dos registros.

## 🛠️ Tecnologias

- **Python 3** — lógica e análise dos registros.
- **Git** — controle de versão.
- **GitHub** — hospedagem e documentação do projeto.
- **Visual Studio Code** — ambiente de desenvolvimento.

## 📁 Estrutura do projeto

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

## ▶️ Como executar

1. Instale o Python 3.
2. Clone este repositório.
3. Abra a pasta do projeto no Visual Studio Code.
4. Verifique se o arquivo `logs/auth.log` existe e contém registros de teste.
5. Abra o terminal na pasta principal do projeto.
6. Execute:

```bash
python src/analisador.py
```

O programa exibirá o total de falhas de autenticação, a quantidade de falhas por IP e o endereço IP com o maior número de falhas.

## 🧠 Conceitos praticados

- Variáveis e contadores.
- Estruturas condicionais (`if`).
- Laços de repetição (`for`).
- Leitura de arquivos com `open()`.
- Manipulação de strings com `split()` e `replace()`.
- Dicionários (`dict`) e o método `.get()`.
- Funções nativas como `max()`.
- Formatação de mensagens com f-strings.
- Fundamentos de análise de logs e investigação de atividades suspeitas.

## 🔐 Aplicação em cibersegurança

A ferramenta simula uma tarefa inicial de um analista SOC: examinar registros de autenticação e identificar endereços IP com um volume elevado de falhas.

Muitas tentativas malsucedidas podem indicar uma possível tentativa de força bruta, mas não comprovam, isoladamente, que houve um ataque. É necessário analisar outros eventos e informações de contexto.

## ⚠️ Aviso

Este projeto tem finalidade exclusivamente educacional. Utilize registros fictícios ou dados que você tenha autorização para analisar. Os resultados são indicadores para investigação, não provas definitivas de comprometimento.

## 👨‍💻 Autor

**Samuel Reis**

Projeto desenvolvido como parte dos estudos de Python e cibersegurança, com foco na preparação para a área de análise SOC.