import discord

from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):  # $hello
    await ctx.send(f'Привет! Я бот {bot.user})')


@bot.command()
async def random(ctx): 
    await ctx.send(gen_pass(20))

@bot.command()
async def heh(ctx, count_heh = 5): # $heh 10
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)
  
@bot.command()
async def info(ctx):
    server = ctx.guild
    await ctx.send(f'Server name: {server.name}\nTotal members: {server.member_count}')
                   
bot.run("")
