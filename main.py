from ctypes import sizeof
from math import ceil
import discord
from discord.ext import commands
from blizzapi import card_search
import asyncio
import Card
from Card import json_to_cards
import os

bot = commands.Bot(command_prefix='>')
#comment for heroku
botToken= os.environ["BOT_TOKEN"]

#uncomment for local
#botToken = open("discord-bot-token").read()


async def main():
    res = await card_search("Kazakus")
    lis = json_to_cards(res)
    for card in lis:
        print(card.text)

@bot.command()
async def start(ctx):
    await ctx.send('Welcome to Hearthstone Search Bot! \nAvailable commands are: image, text, and card.\nA proper search would look like this:\n```">[command] [card name]"```\nFor example: >image reno jackson')

@bot.command()
async def image(ctx, *, content:str):
    res = await card_search(content)
    lis = json_to_cards(res)
    length = len(lis)
    
    def check(m):
        return m.channel == ctx.channel and m.author == ctx.author

    if length == 0:
        await ctx.send("No cards found! Check your spelling.")

    #dont need pages for 1 page results
    elif length <=3:
        await ctx.send(str(length) + " cards found.")
        for card in lis:
            await ctx.send(card.image)


    #send cards in groups of 3 (pages). wanted to do 4, but it seems fastest in accessing 3
    elif length <= 40:
        if length == 40:
            await ctx.send(str(length) + " cards returned. (but more found! Narrow your search a bit to find what you need.).")
        else:
            await ctx.send(str(length) + " cards found.")
        page_counter = 1
        pages = (ceil((length/3)))
        await ctx.send("```(Page " + str(page_counter) + "/" + str(pages) + ") Type 'next' as your next message to view more```")
        card_counter = 0
        for card in lis:
            card_counter = card_counter + 1
            await ctx.send(card.image)
            if card_counter == 3:
                msg = await bot.wait_for("message", check=check)

                if ('next' not in msg.content.lower or '>' in msg.content):
                    return


                page_counter = page_counter + 1
                if page_counter == pages:
                    await ctx.send("```(Page " + str(page_counter) + "/" + str(pages) + ")```")
                else:
                    await ctx.send("```(Page " + str(page_counter) + "/" + str(pages) + ") Type 'next' as your next message to view more```")
                card_counter = 0
            
    else:
        await ctx.send("Woah! Too many cards!")  #would use this, but they already cap searches to 40 results 
        await ctx.send("Please narrow your search down a bit.")



@bot.command()
async def card(ctx, *, content:str):
    res = await card_search(content)
    lis = json_to_cards(res)
    length = len(lis)
    
    def check(m):
        return m.channel == ctx.channel and m.author == ctx.author

    if length == 0:
        await ctx.send("No cards found! Check your spelling.")

    #dont need pages for 1 page results
    elif length <=3:
        await ctx.send(str(length) + " cards found.")
        for card in lis:
            await ctx.send(str(vars(card)))


    #send cards in groups of 3 (pages). wanted to do 4, but it seems fastest in accessing 3
    elif length <= 40:
        if length == 40:
            await ctx.send(str(length) + " cards returned. (but more found! Narrow your search a bit to find what you need.).")
        else:
            await ctx.send(str(length) + " cards found.")
        page_counter = 1
        pages = (ceil((length/3)))
        await ctx.send("```(Page " + str(page_counter) + "/" + str(pages) + ") Type 'next' as your next message to view more```")
        card_counter = 0
        for card in lis:
            card_counter = card_counter + 1
            await ctx.send(str(vars(card)))
            if card_counter == 3:
                msg = await bot.wait_for("message", check=check)

                if ('next' not in msg.content or '>' in msg.content):
                    return


                page_counter = page_counter + 1
                if page_counter == pages:
                    await ctx.send("```(Page " + str(page_counter) + "/" + str(pages) + ")```")
                else:
                    await ctx.send("```(Page " + str(page_counter) + "/" + str(pages) + ") Type 'next' as your next message to view more```")
                card_counter = 0
            
    else:
        await ctx.send("Woah! Too many cards!")  #would use this, but they already cap searches to 40 results 
        await ctx.send("Please narrow your search down a bit.")

@bot.command()
async def text(ctx, *, content:str):
    res = await card_search(content)
    lis = json_to_cards(res)
    length = len(lis)
    
    def check(m):
        return m.channel == ctx.channel and m.author == ctx.author

    if length == 0:
        await ctx.send("No cards found! Check your spelling.")

    #dont need pages for 1 page results
    elif length <=3:
        await ctx.send(str(length) + " cards found.")
        for card in lis:
            await ctx.send("```" + card.name + ": " + card.text.replace("<b>", "").replace("</b>", "") + "```")


    #send cards in groups of 3 (pages). wanted to do 4, but it seems fastest in accessing 3
    elif length <= 40:
        if length == 40:
            await ctx.send(str(length) + " cards returned. (but more found! Narrow your search a bit to find what you need.).")
        else:
            await ctx.send(str(length) + " cards found.")
        page_counter = 1
        pages = (ceil((length/3)))
        await ctx.send("```(Page " + str(page_counter) + "/" + str(pages) + ") Type 'next' as your next message to view more```")
        card_counter = 0
        for card in lis:
            card_counter = card_counter + 1
            await ctx.send("```" + card.name + ": " + card.text.replace("<b>", "").replace("</b>", "") + "```")
            if card_counter == 3:
                msg = await bot.wait_for("message", check=check)

                if ('next' not in msg.content or '>' in msg.content):
                    return


                page_counter = page_counter + 1
                if page_counter == pages:
                    await ctx.send("```(Page " + str(page_counter) + "/" + str(pages) + ")```")
                else:
                    await ctx.send("```(Page " + str(page_counter) + "/" + str(pages) + ") Type 'next' as your next message to view more```")
                card_counter = 0
            
    else:
        await ctx.send("Woah! Too many cards!")  #would use this, but they already cap searches to 40 results 
        await ctx.send("Please narrow your search down a bit.")
    
bot.run(botToken)