# Competitive Scraper

Sistema automatizado de monitoramento de preços de concorrentes, desenvolvido em Python.

O projeto realiza scraping de produtos, armazena preços e histórico em banco de dados, identifica variações de preço e dispara alertas quando uma redução atinge o limite configurado.

Além do alerta no terminal, o sistema também envia notificações por e-mail utilizando SMTP do Gmail.

---

## 🎯 Objetivo

Construir uma solução capaz de acompanhar preços de produtos de um site, manter um histórico das coletas e identificar automaticamente alterações relevantes.

O fluxo principal do sistema é:

```text
Website
   ↓
Selenium
   ↓
BeautifulSoup
   ↓
Extração dos produtos
   ↓
SQLite + SQLAlchemy
   ↓
Histórico de preços
   ↓
Comparação de preços
   ↓
Identificação da variação
   ↓
Alerta de preço
   ↓
E-mail
```

---

## 🚀 Funcionalidades

- Acesso automatizado ao site utilizando Selenium
- Extração de dados com BeautifulSoup
- Coleta de:
  - Nome do produto
  - Preço
  - URL
- Conversão e tratamento dos preços
- Persistência dos produtos em SQLite
- Modelagem do banco utilizando SQLAlchemy
- Histórico de preços por produto
- Identificação do preço anterior e atual
- Cálculo percentual da variação
- Classificação da variação:
  - Alta
  - Queda
  - Sem alteração
- Geração de alerta quando o preço cai **10% ou mais**
- Exibição do alerta no terminal
- Envio automático do alerta por e-mail
- Variáveis sensíveis armazenadas em `.env`

---

## 🛠️ Tecnologias utilizadas

- **Python 3**
- **Selenium**
- **BeautifulSoup**
- **SQLAlchemy**
- **SQLite**
- **python-dotenv**
- **SMTP / Gmail**

---

## 📁 Estrutura do projeto

```text
competitive-scraper/
│
├── app/
│   ├── __init__.py
│   ├── alerts.py
│   ├── database.py
│   ├── email_sender.py
│   ├── models.py
│   ├── monitor.py
│   └── scraper.py
│
├── screenshots/
│   ├── alerta-terminal.png
│   └── alerta-email.png
│
├── tests/
│   └── tests_database.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

O banco SQLite e o arquivo `.env` são mantidos fora do versionamento por questões de segurança e organização.

---

## ⚙️ Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/davidfangio/competitive-scraper.git
cd competitive-scraper
```

### 2. Criar o ambiente virtual

```bash
python3 -m venv .venv
```

### 3. Ativar o ambiente virtual

macOS / Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuração do e-mail

O envio dos alertas utiliza SMTP do Gmail.

Crie um arquivo `.env` na raiz do projeto:

```env
EMAIL_REMETENTE=seu_email@gmail.com
EMAIL_SENHA_APP=sua_senha_de_app
```

A senha utilizada deve ser uma **Google App Password**, e não a senha normal da conta.

O arquivo `.env` está incluído no `.gitignore` e não deve ser enviado para o GitHub.

---

## ▶️ Executando o scraper

Com o ambiente virtual ativado:

```bash
python -m app.scraper
```

O sistema irá:

1. Abrir o navegador automaticamente.
2. Acessar o site.
3. Coletar os produtos.
4. Consultar os produtos existentes no banco.
5. Registrar o histórico de preços.
6. Comparar o preço atual com o anterior.
7. Identificar possíveis quedas.
8. Gerar um alerta quando a queda atingir o limite configurado.
9. Enviar o alerta por e-mail.

---

## 🚨 Regra de alerta

O sistema considera uma queda relevante quando a variação é igual ou inferior a **-10%**.

Exemplo:

```text
Preço anterior: £51.77
Preço atual:    £45.00

Variação: -13.09%
```

Como a queda é superior a 10%, o sistema gera o alerta.

---

## 📸 Demonstração

### Alerta gerado no terminal

![Alerta de preço no terminal](screenshots/alerta-terminal.png)

### Alerta recebido por e-mail

![Alerta de preço recebido por e-mail](screenshots/alerta-email.png)

---

## 🗄️ Banco de dados

O projeto utiliza SQLite para armazenar os dados localmente.

A estrutura principal possui duas entidades:

### Products

Armazena os produtos monitorados.

```text
id
name
url
```

### PriceHistory

Armazena cada coleta de preço.

```text
id
product_id
price
collected_at
```

Essa estrutura permite manter um histórico das alterações de preço ao longo do tempo.

---

## 🧠 Monitoramento de preços

A variação percentual é calculada utilizando:

```text
((preço_atual - preço_anterior) / preço_anterior) × 100
```

Exemplo:

```text
((45.00 - 51.77) / 51.77) × 100
= -13.09%
```

O resultado é então classificado como:

```text
< 0   → queda
> 0   → alta
= 0   → sem alteração
```

---

## 🧪 Testes

O projeto possui testes e validações para as principais partes da aplicação, incluindo:

- Persistência de produtos
- Histórico de preços
- Cálculo de variação
- Classificação de variações
- Regra de alerta
- Geração de mensagens
- Integração do alerta com o envio de e-mail

Também foram realizados testes controlados para validar o comportamento do sistema diante de uma queda de preço de mais de 10%.

---

## 🌐 Fonte dos dados

Para fins de desenvolvimento e demonstração, o scraper utiliza o site **Books to Scrape**, disponibilizado especificamente para testes de scraping.

Como os preços do ambiente de demonstração podem permanecer estáticos, a funcionalidade de alerta também foi validada utilizando cenários controlados de alteração de preço.

---

## 🔒 Segurança

Informações sensíveis não fazem parte do código-fonte.

O projeto utiliza variáveis de ambiente para armazenar as credenciais do serviço de e-mail:

```text
.env
```

Esse arquivo está protegido pelo `.gitignore`.

Nenhuma senha ou App Password deve ser adicionada diretamente ao código ou ao repositório.

---

## 📌 Possíveis evoluções

O projeto pode ser expandido para:

- Monitorar múltiplos sites
- Monitorar produtos específicos
- Adicionar dashboards
- Criar relatórios de variação
- Implementar diferentes níveis de alerta
- Utilizar agendamento automático das coletas
- Adicionar outros canais de notificação
- Utilizar PostgreSQL ou outro banco de dados
- Implementar uma API para consulta dos preços
- Adicionar testes automatizados mais abrangentes

---

## 👨‍💻 Projeto

Desenvolvido por **David Assunção Lopes** como projeto de portfólio para demonstrar conhecimentos em:

**Python • Web Scraping • Selenium • BeautifulSoup • SQLAlchemy • SQLite • Automação • Monitoramento • Integração com e-mail**