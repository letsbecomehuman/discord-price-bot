import discord
import requests

from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

# instantiate a discord client
client = discord.Client()

# status background task update kawa price
async def status_task():
    while True:
        coingecko = 'https://api.coingecko.com/api/v3/simple/price?ids=kawakami&vs_currencies=usd&include_market_cap=true'

        # getting data from coingecko
        r = requests.get(url=coingecko)

        # converting data to json
        data = r.json()

        # Store the price in a variable
        price = data['kawakami']['usd']

        # Convert the scientific notation to a float with 12 decimal places
        price = format(price, '.8f')
        #await client.change_presence(activity=discord.Game(name=f'$KAWA: {price}'))
        #                activity=discord.Activity(type=discord.ActivityType.watching, name=f'$KAWA: {price}')
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f': {price}'))
        print(f'Updating Price')
        await asyncio.sleep(90)# 30 as in 30seconds


@client.event
async def on_ready():
    print(f'You have logged in as {client}')
    client.loop.create_task(status_task())

# game = discord.Game("with the API")
# await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=game))

# called whether there is a message in the chat
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    # if the message starts with "!crypto"
    if message.content.lower().startswith('!price kawa'):

        # Generating the URL
        coingecko = 'https://api.coingecko.com/api/v3/simple/price?ids=kawakami&vs_currencies=usd&include_market_cap=true'

        # getting data from coingecko
        r = requests.get(url=coingecko)

        # converting data to json
        data = r.json()

        # Store the price in a variable
        price = data['kawakami']['usd']

        # Convert the scientific notation to a float with 12 decimal places
        price = format(price, '.8f')

        #if int(float(price)) > 0:
            # sending the price to the chat
        await message.channel.send(f'{price} USD')
        #elif int(float(price)) == 0:
            #await message.channel.send(f'The price is: ↑ {price} USD')

        #else:
            #await message.channel.send(f'The price is: ↓ {price} USD')

           # Generating the URL

    elif message.content.lower().startswith(('!mc kawa', '!kawa')):
        coingecko = 'https://api.coingecko.com/api/v3/simple/price?ids=kawakami&vs_currencies=usd&include_market_cap=true&include_24hr_change=true'

        # getting data from coingecko
        r = requests.get(url=coingecko)

        # converting data to json
        data = r.json()

        # Store the price in a variable
        market_cap = data['kawakami']['usd_market_cap']
        price = data['kawakami']['usd']
        change = data['kawakami']['usd_24h_change']
        # Convert the scientific notation to a float with 12 decimal places
        # market_cap = format(market_cap, '.0f')
        # market_cap = int(market_cap[:-5]) //10
        market_cap = int(market_cap) / 1000000.00
        market_cap = format(market_cap, '.1f')
        price = format(price, '.8f')
        change = format(change, '.2f')
        # client.user.setActivity(price)

        #if int(float(change)) > 0:
        # sending the price to the chat
        await message.channel.send(f'Price: {price} USD \r\nMarket cap: {market_cap} M \r\nChange: {change}%')
        #else:
        #    await message.channel.send(f'{price} USD \r\n{market_cap} M \r\n{change}%')

# PUT YOUR TOKEN HERE
BOT_TOKEN = ''
client.run(BOT_TOKEN)
