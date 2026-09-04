# assistant_code_python
Intelligent chatbot powered by AI to provide instant support for Python coding questions.

# IA CODE COPILOT 🤖🐍

O **IA CODE COPILOT** é um assistente virtual interativo desenvolvido com **Streamlit** e alimentado pelos modelos de linguagem de altíssima velocidade da **Groq API**. Ele foi projetado especialmente para ajudar estudantes e desenvolvedores iniciantes com dúvidas sobre programação e a linguagem **Python**.

---

## 🚀 Funcionalidades

- **Respostas Estruturadas e Didáticas**:
  - 💡 **Explicação Conceitual**: Explicações claras e diretas sobre o tópico pesquisado.
  - 💻 **Exemplos de Código**: Código em Python formatado e comentado.
  - 🔍 **Detalhamento do Código**: Explicação passo a passo da lógica e funções utilizadas.
  - 📚 **Documentação Oficial**: Links diretos de referência para a documentação oficial da linguagem ou biblioteca.
- **Interface Web Simples e Intuitiva**: Desenvolvida com Streamlit para uma navegação fluida.
- **Histórico de Conversa**: Mantém o contexto das perguntas durante a sessão.

---

## 🔑 Pré-requisito Obrigatório: Chave de API Groq

Para utilizar o assistente, é **obrigatório** possuir uma chave de API (API Key) gratuita da Groq.

1. Acesse o **[Groq Console](https://console.groq.com/home?utm_source=website&utm_medium=outbound_link&utm_campaign=dev_console_click)**.
2. Crie uma conta ou faça login.
3. No menu lateral, navegue até **API Keys** (ou accesse [https://console.groq.com/keys](https://console.groq.com/keys)).
4. Clique em **Create API Key**, copie a chave gerada e guarde-a em um local seguro.

> ⚠️ **Nota:** A chave de API deverá ser inserida na barra lateral da aplicação web sempre que iniciar o sistema.

---

## 🛠️ Como Executar o Projeto Localmente

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Criar e Ativar um Ambiente Virtual (Recomendado)

- **Linux / macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- **Windows:**
  ```cmd
  python -m venv venv
  venv\Scripts\activate
  ```

### 3. Instalar as Dependências

Com o ambiente virtual ativo, instale os pacotes necessários listados no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Executar a Aplicação Streamlit

Rode o comando abaixo para iniciar a interface web:

```bash
streamlit run assistente.py
```

A aplicação abrirá automaticamente no seu navegador no endereço `http://localhost:8501`.

---

## 💡 Como Usar

1. Ao abrir a aplicação, vá até a **barra lateral (Sidebar)** à esquerda.
2. Cole sua chave de API da Groq no campo **"insira sua chave de API Groq"**.
3. Digite sua dúvida de programação no campo de chat na parte inferior da tela e pressione `Enter`.
4. O assistente analisará sua pergunta e retornará a explicação conceitual, o exemplo de código e a documentação de referência.

---

## 🧰 Tecnologias Utilizadas

- **[Python](https://www.python.org/)**: Linguagem principal do projeto.
- **[Streamlit](https://streamlit.io/)**: Framework para criação de interfaces web.
- **[Groq Cloud SDK](https://groq.com/)**: Processamento e geração das respostas com modelos de linguagem de alta performance.

---

## 👨‍💻 Desenvolvedor

Desenvolvido por **Joelson Correa**  
Estudante de Engenharia da Computação 
