import discord
from discord.ext import commands
from config import settings
import json
import requests
from time import sleep
import emoji
import asyncio, os
from discord.ext import commands, tasks
from data_from_dappcom import get_info, get_price

bot = commands.Bot(command_prefix=settings['prefix'])

@bot.command()
async def info(ctx):
    channel = bot.get_channel(ctx.channel.id)
    embed = discord.Embed(color = 0xff9900, title = 'Rubic', url='https://www.dapp.com/app/rubic',
                          description=get_info()) # Создание Embed'a
    embed.set_thumbnail(
        url="https://assets.coingecko.com/coins/images/12629/large/rubic.jpg?1601297271"
    )
    await ctx.send(embed = embed) # Отправляем Embed
    message = await channel.history().find(lambda m: m.author.id == 769117103776727050)
    while True:
        newEmbed = discord.Embed(color = 0xff9900, title = 'Rubic', url='https://www.dapp.com/app/rubic', description=get_info())
        newEmbed.set_thumbnail(url="https://assets.coingecko.com/coins/images/12629/large/rubic.jpg?1601297271")
        await message.edit(embed=newEmbed, content='')
        await asyncio.sleep(10)
        await message.edit(content='', embed=newEmbed)
        await asyncio.sleep(10)

bot.run(settings['token']) # Обращаемся к словарю settings с ключом token, для получения токена
