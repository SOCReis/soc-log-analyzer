# SOC Log Analyzer

Analisador de logs de autenticação desenvolvido em Python para praticar análise de eventos e investigação de atividades suspeitas em um ambiente SOC (Security Operations Center).

O projeto lê registros de autenticação, agrupa falhas e acessos bem-sucedidos por endereço IP e identifica possíveis atividades suspeitas. Os resultados são apresentados no terminal e podem ser integrados a um dashboard web com Flask.

## Objetivos

- Praticar a leitura e análise de logs.
- Identificar IPs com múltiplas falhas de autenticação.
- Contabilizar sucessos e falhas de login.
- Identificar endereços IP distintos.
- Registrar a primeira e a última falha de autenticação por IP.
- Identificar IPs com quantidade elevada de falhas.
- Aplicar conceitos de Python e cibersegurança em um projeto prático.

## Funcionalidades

- [x] Leitura de logs de autenticação.
- [x] Contagem de falhas por IP.
- [x] Contagem de autenticações bem-sucedidas por IP.
- [x] Contagem total de falhas e sucessos.
- [x] Contagem de endereços IP distintos, sem duplicatas.
- [x] Identificação do IP com maior número de falhas.
- [x] Exibição da primeira e da última falha do IP com mais falhas.
- [x] Exibição da quantidade de sucessos do IP com mais falhas.
- [x] Identificação de IPs com mais de 10 falhas.
- [x] Ordenação dos IPs suspeitos pela quantidade de falhas.
- [x] Exibição da quantidade de sucessos dos IPs suspeitos.

## Tecnologias

- Python
- `collections.Counter`
- `collections.defaultdict`
- Conjuntos (`set`)
- Flask
- HTML5
- CSS3
- Jinja2
- Git e GitHub
- Visual Studio Code

## Estrutura do projeto

```text
soc-log-analyzer/
├── logs/
│   └── auth.log
├── src/
│   ├── analisador.py
│   └── app.py
├── templates/
│   └── dashboard.html
├── static/
│   └── style.css
├── .gitignore
├── README.md
└── requirements.txt
```

## Como executar

### 1. Clonar o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
cd soc-log-analyzer
```

Substitua `URL_DO_SEU_REPOSITORIO` pelo endereço do seu repositório no GitHub.

### 2. Criar o ambiente virtual

```bash
python -m venv .venv
```

### 3. Ativar o ambiente virtual

No Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

No Prompt de Comando (CMD):

```cmd
.venv\Scripts\activate.bat
```

### 4. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 5. Executar o analisador

Na pasta principal do projeto, execute:

```bash
python src/analisador.py
```

O programa exibirá os totais de autenticações, a quantidade de IPs distintos e informações sobre os IPs com mais falhas.

### 6. Iniciar o dashboard web

Se o Flask estiver configurado no projeto, execute:

```bash
python src/app.py
```

Depois, abra no navegador:

http://127.0.0.1:5000

## Como funciona a análise

O analisador percorre o arquivo `logs/auth.log` e identifica o endereço IP de cada registro válido.

Os dados são organizados em contadores de falhas e sucessos. Um conjunto (`set`) armazena os IPs sem repetições, permitindo calcular a quantidade de endereços distintos.

O limite de falhas é definido pela variável `LIMITE_FALHAS`, configurada inicialmente como `10`. IPs com mais de 10 falhas são exibidos como possíveis suspeitos.

A primeira e a última falha são registradas para cada IP que apresenta falhas de autenticação.

## Próximas melhorias

- [ ] Melhorar a organização dos dados retornados pelo analisador.
- [ ] Adicionar filtros por IP e quantidade de falhas.
- [ ] Destacar possíveis atividades suspeitas no dashboard.
- [ ] Implementar paginação para grandes volumes de registros.
- [ ] Exportar relatórios em CSV e JSON.
- [ ] Criar testes automatizados.
- [ ] Melhorar a análise de padrões de autenticação.
- [ ] Registrar a primeira e a última ocorrência de todos os eventos por IP.
- [ ] Tratar erros de leitura e arquivos de log inexistentes.

## Aviso

Este projeto tem finalidade educacional. A presença de várias falhas de autenticação pode indicar uma tentativa de força bruta, mas não comprova, isoladamente, a ocorrência de um ataque.

Utilize logs de teste ou dados que você tenha autorização para analisar.

## Autor

Samuel Reis

Projeto pessoal de aprendizado em Python, análise de logs e cibersegurança.
