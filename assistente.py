
# importando o modulo para interagir com o sistema operacional
import os

# importando o streamlit para interface web da aplicação
import streamlit as st 

# importando a plataforma da groq para se conectar com a API
from groq import Groq 

# configurando a pagina inicial do streamlit com titulo, icone, layout e estado inicial de sidebar

st.set_page_config(
    page_title="IA CODE COPILOT",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define um prompt de sistema que descreva as regras e comportamento do assistente de IA
CUSTOM_PROMPT = """
Você é o "IA CODE COPILOT", um assistente de IA especialista em programação, com foco principal em Python. Sua missão é ajudar desenvolvedores iniciantes com dúvidas de programação de forma clara, precisa e útil.
REGRAS DE OPERAÇÃO:
1. **Foco em Programação**: Responda apenas a perguntas relacionadas a programação, algoritmos, estruturas de dados, bibliotecas e frameworks. Se o usuário perguntar sobre outro assunto, responda educadamente que seu foco é exclusivo.
2. **Estrutura da Resposta**: Sempre formate suas respostas da seguinte maneira:
   * **Explicação Clara**: Comece com uma explicação conceitual sobre o tópico perguntado. Seja direto e didático.
   * **Exemplo de Código**: Forneça um ou mais blocos de código em Python com a sintaxe correta. O código deve ser bem comentado para explicar as partes importantes.
   * **Detalhes do Código**: Após o bloco de código, descreva em detalhes o que cada parte do código faz, explicando a lógica e as funções utilizadas.
   * **Documentação de Referência**: Ao final, inclua uma seção chamada "📚 Documentação de Referência" com um link direto e relevante para a documentação oficial da Linguagem Python (docs.python.org) ou da biblioteca em questão.
3. **Clareza e Precisão**: Use uma linguagem clara. Evite jargões desnecessários. Suas respostas devem ser tecnicamente precisas.
"""

# Cria o conteudo da barra lateral no streamlit

with st.sidebar:
    # Define o titulo da barra lateral
    st.title("IA CODE")

    # Mostra um texto explicativo sobre o assistente
    st.markdown("Um assistente de IA focado em programação Python para ajudar iniciantes na aprendizagem.")

    # Campo para insirir a chave de API da Groq
    groq_api_key = st.text_input(
        "insira sua chave de API Groq",
        type="password",
        help="Obtenha sua chave em https://console.groq.com/keys"
    )

    # Adiciona linhas divisorias e explicações extras na barra lateral
    st.markdown("----")
    st.markdown("Desenvolvido para auxiliar em suas dúvidas de programação com a Linguagem Python. IA pode cometer erros. Sempre verifique as respostas.")

    st.markdown("----")
    st.markdown("desenvolvido por [@JoelsonCorrea]")

# titulo principal da aplicação
st.title("IA CODE COPILOT 🤖")

# Subtitulo adicional para a aplicação
st.title("Um assistente de IA para programação Python 🐍")

# texto auxiliar explicando a funcionalidade do assistente
st.caption("Faça sua pergunta e receba uma resposta detalhada com explicações, exemplos de código e referências.")

# inicializa o historico de mensagens na sessão, caso ainda não exista
if "messagens" not in st.session_state:
    st.session_state.messagens = []

# Exibe todas as mensagens anteriores armazenadas no estado da sessão
for mensagem in st.session_state.messagens:
    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["content"])

# inicializa a variavél do cliente Groq como nome
client = None

# verifica se o usuario forneceu a chave de API da Groq

if groq_api_key:

    try:
        # cria o cliente Groq coma chave de API forneceida
        client = Groq(api_key = groq_api_key)

    except Exception as e:
        # exibe erro caso haja problema ao inicializar o cliente Groq
        st.sidebar.error(f"Erro ao inicializar o cliente Groq: {e}")
        st.stop()


# caso não tenha chave, mas já existam mensagens, mostra aviso
elif st.session_state.messagens:
    st.warning("Para continuar, insira sua chave de API Groq na barra lateral.")

# captura a entrada do usuario no chat
if prompt := st.chat_input("Digite sua pergunta sobre programação Python..."):

    # se não houve cliente válido, mostra aviso e para a execução
    if not client:
        st.warning("Para continuar, insira sua chave de API Groq na barra lateral.")
        st.stop()
    
    # armazena a  mesagem do usuario no estado da sessão
    st.session_state.messagens.append({"role": "user", "content": prompt})

    # exibe a messagem do usuario no chat
    with st.chat_message("user"):
        st.markdown(prompt)

    # prepara a mensagem para enviar á API, incluindo prompt de sistema
    messages_for_api = [{"role": "system", "content": CUSTOM_PROMPT }]
    for msg in st.session_state.messagens:
        messages_for_api.append(msg)
    
    # cria a resposta so assistente no chat
    with st.chat_message("assistant"):

        with st.spinner("Analisando sua pergunta..."):

            try:
                #chamaa API da groq para gerar a resposta
                chat_completion = client.chat.completions.create(
                    messages=messages_for_api,
                    model="openai/gpt-oss-20b",
                    temperature=0.9,
                    max_tokens=2048,
                )

                # extrai a resposta gerada pela API
                code_ai = chat_completion.choices[0].message.content

                # exibe a resposta no streamlit
                st.markdown(code_ai)

                # armazena resposta do assistente no estado da sessão
                st.session_state.messagens.append({"role": "assistant", "content": code_ai})

            # caso ocorra erro na comunicação com API, exibe mensagem de erro
            except Exception as e:
                st.error(f"Erro ao gerar resposta: {e}")
st.markdown(
    """
    <div style="text-align: center; color: gray;">
    <hr>
    <p>CODE COPILOT 🤖 - Desenvolvido por Joelson Correa estudante de Eng. da Computação

    </div>
    """,
    unsafe_allow_html=True
)

    
