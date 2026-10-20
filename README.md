# 🔐 SOC Log Analyzer

Analisador de logs de autenticação desenvolvido em Python, com o objetivo de simular tarefas iniciais de um analista de Security Operations Center (SOC).

O projeto processa registros de autenticação, identifica padrões de falhas de login e apresenta informações relevantes para auxiliar na investigação de atividades potencialmente suspeitas.

Atualmente, o projeto também possui um dashboard web desenvolvido com Flask, HTML e Jinja.

## 🎯 Objetivos

- Praticar análise de logs de autenticação.
- Identificar endereços IP com múltiplas falhas de login.
- Organizar eventos de segurança por endereço IP.
- Desenvolver uma interface para visualizar resultados.
- Aprender conceitos utilizados em investigações SOC.

## ⚙️ Funcionalidades

- [x] Leitura de logs de autenticação.
- [x] Contagem de falhas de login por IP.
- [x] Contagem de autenticações bem-sucedidas por IP.
- [x] Contabilização de falhas e sucessos.
- [x] Registro da primeira e última ocorrência por IP.
- [x] Identificação do IP com maior número de falhas.
- [x] Identificação de IPs acima do limite configurado de falhas.
- [x] Integração inicial com Flask.
- [x] Exibição de informações em HTML usando Jinja.

## 🛠️ Tecnologias

- Python
- Flask
- HTML
- Jinja
- Git e GitHub
- Visual Studio Code

## 📁 Estrutura do projeto

```text
soc-log-analyzer/
├── logs/
│   └── auth.log
├── src/
│   ├── analisador.py
│   └── app.py
├── templates/
│   └── dashboard.html
├── .gitignore
├── README.md
└── requirements.txt
```

## 🚀 Como executar

### 1. Clonar o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
cd soc-log-analyzer
```

Substitua `URL_DO_SEU_REPOSITORIO` pelo endereço real do seu repositório GitHub.

### 2. Criar um ambiente virtual

```bash
python -m venv .venv
```

### 3. Ativar o ambiente virtual no Windows

No CMD:

```cmd
.venv\Scripts\activate
```

### 4. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 5. Iniciar o dashboard

Execute a partir da pasta principal do projeto:

```bash
python src/app.py
```

Depois, abra no navegador o endereço local informado pelo Flask, normalmente:

http://127.0.0.1:5000

## 🔎 Exemplo de investigação

O analisador pode encontrar um endereço IP com um número elevado de falhas de autenticação.

Esse comportamento pode indicar uma tentativa de força bruta, mas precisa ser investigado antes de ser classificado como ataque confirmado.

## 🗺️ Próximas implementações

- [ ] Corrigir e validar a contagem de IPs distintos.
- [ ] Melhorar a organização dos dados retornados pelo analisador.
- [ ] Criar uma tabela de IPs com falhas e sucessos.
- [ ] Exibir os períodos de atividade por IP.
- [ ] Destacar alertas de possíveis ataques no dashboard.
- [ ] Adicionar filtros por IP e quantidade de falhas.
- [ ] Exportar relatórios em CSV e JSON.
- [ ] Criar testes automatizados.
- [ ] Melhorar o visual do dashboard.

## ⚠️ Aviso

Este projeto tem finalidade educacional e utiliza logs para estudar análise de eventos de segurança. Os alertas representam possíveis atividades suspeitas e não comprovam, isoladamente, a ocorrência de um ataque.

## 👨‍💻 Autor

Samuel Reis

Projeto pessoal de aprendizado em Python, análise de logs e cibersegurança.
