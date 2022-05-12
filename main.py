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
    if length > 4:
        await ctx.send("```Page 1/" + str(ceil((length/4))) + "```")
    for card in lis:
        await ctx.send(card.image)

bot.run(botToken)