# SOC Log Analyzer

Analisador de logs de autenticação desenvolvido em Python para praticar conceitos de análise de eventos e investigação de atividades suspeitas em um ambiente SOC (Security Operations Center).

O projeto lê registros de autenticação, organiza os eventos por endereço IP e apresenta informações sobre falhas e acessos bem-sucedidos. Os resultados podem ser visualizados em um dashboard web desenvolvido com Flask, HTML e CSS.

## Objetivos

- Praticar a leitura e análise de logs.
- Identificar IPs com múltiplas falhas de autenticação.
- Contabilizar sucessos e falhas de login.
- Organizar eventos por endereço IP.
- Registrar a primeira e a última ocorrência de cada IP.
- Desenvolver um dashboard para facilitar a visualização dos resultados.
- Aplicar conceitos de Python e desenvolvimento web em um projeto prático.

## Funcionalidades

- [x] Leitura de logs de autenticação.
- [x] Contagem de falhas por IP.
- [x] Contagem de autenticações bem-sucedidas por IP.
- [x] Contagem total de sucessos e falhas.
- [x] Registro da primeira e última ocorrência por IP.
- [x] Identificação do IP com maior número de falhas.
- [x] Identificação de IPs acima do limite configurado de falhas.
- [x] Integração com Flask.
- [x] Dashboard web com HTML e Jinja2.
- [x] Estilização da interface com CSS.
- [x] Exibição de listas e tabelas com rolagem para facilitar a visualização de muitos registros.

## Tecnologias

- Python
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

### 5. Iniciar o dashboard

Na pasta principal do projeto, execute:

```bash
python src/app.py
```

Abra no navegador o endereço informado pelo Flask, normalmente:

http://127.0.0.1:5000

## Exemplo de investigação

O analisador pode identificar endereços IP com várias falhas de autenticação.

Esse comportamento pode indicar uma tentativa de força bruta, mas também pode ocorrer por erros legítimos de digitação ou configurações incorretas. Por isso, os resultados precisam ser investigados antes de classificar uma atividade como ataque.

## Próximas melhorias

- [ ] Validar a contagem de endereços IP distintos.
- [ ] Melhorar a organização dos dados retornados pelo analisador.
- [ ] Adicionar filtros por IP e quantidade de falhas.
- [ ] Ordenar os IPs pelo número de falhas.
- [ ] Destacar possíveis atividades suspeitas no dashboard.
- [ ] Implementar paginação para grandes volumes de registros.
- [ ] Exportar relatórios em CSV e JSON.
- [ ] Criar testes automatizados.
- [ ] Melhorar a análise de padrões de autenticação.

## Aviso

Este projeto tem finalidade educacional. Os resultados indicam possíveis atividades suspeitas e não comprovam, isoladamente, a ocorrência de um ataque.

Utilize logs de teste ou dados que você tenha autorização para analisar.

## Autor

Samuel Reis

Projeto pessoal de aprendizado em Python, análise de logs e cibersegurança.