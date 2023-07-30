import os
import lightbulb
import pandas as pd

cwd = os.path.dirname(os.path.realpath(__file__))

# data = pd.read_csv(os.path.join(cwd, 'datasets/supermarket_sales.csv'))


bot = lightbulb.BotApp(
    token = open(os.path.join(cwd, 'tokens/token_ds.txt'), 'r').read(),
    default_enabled_guilds = int(open(os.path.join(cwd, 'tokens/ds_channel_id.txt'), 'r').read())
)

# ========== SAUDAÇÃO ========== #
@bot.command
@lightbulb.command(
    name = 'msg_asmv',
    description = 'Saudacao Asimov Academy'
)
@lightbulb.implements(lightbulb.SlashCommand)
async def hello(ctx):
    await ctx.respond('Olá, comunidade Asimov Academy!')

# ========== PIADA ========== #
import random as rd

piadas = [
    "O que o pato disse para a pata \nR.: Vem Quá!",
    "Porque o menino estava falando ao telefone deitado? \nR.: Para não cair a ligação.",
    "Qual é a fórmula da água benta? \nR.: H Deus O!",
    "Qual é a cidade brasileira que não tem táxi? \nR.: Uberlândia",
    "Qual é a fruta que anda de trem? \nR.: O kiwiiiii.",
    "O que é um pontinho preto no avião? \nR.: Uma aeromosca.",
    "Como o Batman faz para entrar na Bat-caverna? \nR.: Ele bat-palma.",
    "Por que o pão não entende a batata? \nR.: Porque o pão é francês e a batata é inglesa",
    "O que o zero disse para o oito? \nR.: Belo cinto!",
    "Por que os elétrons nunca são convidados para festas? \nR.: Porque eles são muito negativos."
]

@bot.command
@lightbulb.command(
    name = 'piada',
    description = 'Receba uma piada'
)
@lightbulb.implements(lightbulb.SlashCommand)
async def joke(ctx):
    n = rd.randint(0, len(piadas))
    await ctx.respond(f'{piadas[n]}')



# ========== CALCULADORA ========== #
@bot.command
@lightbulb.command(
    name = 'calculadora',
    description = 'Calcula uma operação de 2 valores'
)
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def calc(ctx):
    pass

#Adição
@calc.child
@lightbulb.option(name='n2', description='Segundo número', type=float)
@lightbulb.option(name='n1', description='Primeiro número', type=float)
@lightbulb.command(name='soma', description='Adição')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def soma(ctx):
    s = ctx.options.n1 + ctx.options.n2
    await ctx.respond(f'*{ctx.options.n1} + {ctx.options.n2} =* **{s}**')

# Subtração
@calc.child
@lightbulb.option(name='n2', description='Segundo número', type=float)
@lightbulb.option(name='n1', description='Primeiro número', type=float)
@lightbulb.command(name='sub', description='Subtração')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def sub(ctx):
    s = ctx.options.n1 - ctx.options.n2
    await ctx.respond(f'*{ctx.options.n1} - {ctx.options.n2} =* **{s}**')

# Multiplicação
@calc.child
@lightbulb.option(name='n2', description='Segundo número', type=float)
@lightbulb.option(name='n1', description='Primeiro número', type=float)
@lightbulb.command(name='multi', description='Multiplicação')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def multi(ctx):
    m = ctx.options.n1 * ctx.options.n2
    await ctx.respond(f'*{ctx.options.n1} x {ctx.options.n2} =* **{m}**')

# Divisão
@calc.child
@lightbulb.option(name='n2', description='Denominador', type=float)
@lightbulb.option(name='n1', description='Numerador', type=float)
@lightbulb.command(name='div', description='Divisão')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def div(ctx):
    if ctx.options.n2 != 0:
        d = ctx.options.n1 / ctx.options.n2
    else:
        d = 'indeterminação'
    await ctx.respond(f'*{ctx.options.n1} / {ctx.options.n2} =* **{d}**')    



# ========== OpenWeather ========== #
import requests
import string

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = open(os.path.join(cwd, 'tokens/openweather_key.txt'), 'r').read()

@bot.command
@lightbulb.option(name = 'pais', description = 'País', type=str)
@lightbulb.option(name = 'cidade', description = 'Cidade', type=str)
@lightbulb.command(
    name = 'weather',
    description = 'Informe uma país e uma cidade para saber o clima atual'
)
@lightbulb.implements(lightbulb.SlashCommand)
async def weather(ctx):
    country = ctx.options.pais
    city = string.capwords(ctx.options.cidade) + ',' + country[0:2].lower()
    url = BASE_URL + 'q=' + city + '&APPID=' + API_KEY
    response = requests.get(url).json()
    temp = round(response['main']['temp'] - 273.15)

    await ctx.respond(f"```A temperatura em {string.capwords(ctx.options.cidade)} é de {temp}ºC\numidade do ar: {response['main']['humidity']}%\nVento: {response['wind']['speed']} m/s```")

bot.run()