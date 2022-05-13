from ctypes import sizeof
from math import ceil
import discord
from discord.ext import commands
from blizzapi import card_search
import asyncio
import Card
from Card import json_to_cards

bot = commands.Bot(command_prefix='>')

botToken = open("discord-bot-token").read()


async def main():
    res = await card_search("Kazakus")
    lis = json_to_cards(res)
    for card in lis:
        print(card.text)

@bot.command()
async def card(ctx, *, content:str):
    res = await card_search(content)
    lis = json_to_cards(res)
    length = len(lis)
    if length == 0:
        await ctx.send("No cards found! Check your spelling.")
    elif length <=4:
        await ctx.send(str(length) + " cards found.")
        for card in lis:
            await ctx.send(card.image)
    elif length < 100:
        await ctx.send(str(length) + " cards found.")
        counter = 1
        await ctx.send("```Page " + str(counter) + "/" + str(ceil((length/4))) + "```")
        for card in lis:
            await ctx.send(card.image)
    #else:
        #await ctx.send("Woah! Too many cards!")    would use this, but they already cap searches to 40 results 
        #await ctx.send("Please narrow your search down a bit.")



@bot.command()
async def test(ctx, *, content:str):
    res = await card_search(content)
    lis = json_to_cards(res)
    for card in lis:
        await ctx.send(str(vars(card)))
bot.run(botToken)