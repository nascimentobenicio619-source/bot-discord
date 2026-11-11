import discord  # Biblioteca para trabalhar com a API do Discord
from discord.ext import commands  # Módulo para criação de comandos do bot
import requests  # Biblioteca para realizar requisições HTTP
import pyttsx3  # Biblioteca para síntese de fala

# Inicializa o sintetizador de voz
engine = pyttsx3.init()  # Cria um objeto para síntese de fala

# Inicializa o objeto do bot
intents = discord.Intents.default()  # Configura as permissões do bot
intents.message_content = True  # Permite que o bot leia o conteúdo das mensagens
bot = commands.Bot(command_prefix="!", intents=intents)  # Cria o bot com o prefixo especificado

# Função para obter um fato aleatório por meio da API
def get_fact() -> str:
    """
    Obtém um fato aleatório da API.

    Retorna:
        str: O texto do fato ou uma mensagem de erro.
    """
    base_url = "https://uselessfacts.jsph.pl/random.json?language=en"  # URL para obter um fato aleatório
    response = requests.get(base_url)  # Realiza uma requisição GET à API

    if response.status_code == 200:  # Se a requisição for bem-sucedida (código 200)
        data = response.json()  # Converte a resposta para o formato JSON
        return data.get("text", "Não foi possível obter um fato interessante.")  # Retorna o texto do fato
    else:
        return "Não foi possível obter os dados. Tente novamente mais tarde."  # Retorna uma mensagem de erro

# Função para síntese de fala
def speak(text: str):
    """
    Converte o texto fornecido em fala usando a biblioteca pyttsx3.

    Parâmetros:
        text (str): Texto que será lido em voz alta.
    """
    engine.say(text)  # Envia o texto para o sintetizador
    engine.runAndWait()  # Executa a síntese de fala e aguarda a conclusão

# Comando para obter um fato interessante
@bot.command()
async def fact(ctx):
    """
    Comando para obter um fato aleatório e reproduzi-lo em voz alta.

    Parâmetros:
        ctx: Contexto do comando (informações sobre sua execução).
    """
    random_fact = get_fact()  # Obtém um fato aleatório
    await ctx.send(f"Um fato interessante: {random_fact}")  # Envia o fato para o canal do Discord
    speak(random_fact)  # Lê o fato em voz alta

# Inicia o bot
bot.run("MTU3MDE4MDMyOTUxMDAxNTA2Ng.Gd5i12.-qWv7AsTsU_VZFvLrThY6uSmKZADg0il6VRL30")  # Inicia o bot com o token especificado