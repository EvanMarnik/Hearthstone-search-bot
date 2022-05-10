import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='>')

botToken = open("discord-bot-token").read()

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.event
async def on_ready():
    print("Everything's all ready to go~")

@bot.event
async def on_message(message):
    #print("The message's content was", message.content)
    await bot.process_commands(message)


@bot.command()
async def yo(ctx):
    await ctx.send('oy')

@bot.command()
async def echo(ctx, *, content:str):
    if "meme" in content:
        await ctx.send(("https://media.discordapp.net/attachments/956216570848370720/973559800560484382/unknown-51.png"))
        return
    await ctx.send(content)

bot.run(botToken)