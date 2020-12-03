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


url = "https://api.opensea.io/api/v1/assets"

bot = commands.Bot(command_prefix=settings['prefix'])
# Так как мы указали префикс в settings, обращаемся к словарю с ключом prefix.
'''guild = bot.get_guild(765937825748484097)
memberList = guild.members'''

@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def hello(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.

    await ctx.send(f'Hello, {author.mention}!') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.

@bot.command()
async def fox(ctx):
    response = requests.get('https://api.etherscan.io/api?module=gastracker&action=gasoracle') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON
    gas_price = 'Gas price '+json_data['result']['ProposeGasPrice']

    embed = discord.Embed(color = 0xff9900, title = 'Random Fox') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

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

#mytask.start()

'''@tasks.loop(seconds=10)
async def name_change():
    await bot.change_presence(activity=discord.Game('online'))
    await sleep(10)
    await bot.change_presence(activity=discord.Game('online'))

name_change.before_loop(bot.wait_until_ready())
name_change.start()'''

@bot.command()
async def test(ctx):
    while True:
        result = get_price()
        await ctx.guild.me.edit(nick=result[0])
        await bot.change_presence(activity=discord.Game(result[1]))
        await asyncio.sleep(10)
        result = get_price()
        await ctx.guild.me.edit(nick=result[0])
        await bot.change_presence(activity=discord.Game(result[1]))
        await asyncio.sleep(10)


'''async def status_task():
    while True:
        response = requests.get('https://api.etherscan.io/api?module=gastracker&action=gasoracle')  # Get-запрос
        json_data = json.loads(response.text)  # Извлекаем JSON
        #usr = bot.user.id
        #guild = await bot.fetch_guild(765937825748484097)
        #members = guild.fetch_members(limit=None)
        gas_price = 'Gas '+json_data['result']['SafeGasPrice']+'|'+json_data['result']['ProposeGasPrice']+'|'+json_data['result']['FastGasPrice']
        #await bot.edit(nick='Koala')
        #await guild.me.edit(nick="Rita")
        #await bot.user.edit(display_name='KoalaSUPER')
        #await member.edit(nick='RIta')
        #await bot.edit_profile(username='myname')
        #await usr.edit(nick='LAVAZA')
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=gas_price))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(gas_price))
        await asyncio.sleep(10)

@bot.event
async def on_ready():
    bot.loop.create_task(status_task())'''

bot.run(settings['token']) # Обращаемся к словарю settings с ключом token, для получения токена
