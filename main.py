import discord
import json
import os
import requests
from discord.ext import tasks
from datetime import datetime
from stayonline import keep_alive

data = open('bdays.json')
check = (json.load(data))




intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('Logged in as {0.user}', format(client))
    send_message.start()

#date and loop part start here:
@tasks.loop(hours=3)
async def send_message():
    now = datetime.now()
    tdate = now.strftime("%d-%m")

    for i in range(0, 39):
        if check[i]['Bday'] == tdate:
            channel = client.get_channel(1014507327497437267)
            await channel.send(
                f"@everyone Its {check[i]['Name']} ,{check[i]['Roll']}'s Birthday"
            )


#chat part start here:
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author != client.user:
        if str(message.content) == "hello":
            print(str(message))
            await message.channel.send("works")
            return
        if str(message.content) == "/json":
          await message.channel.send(check)
          return
        if str(message.content) == "/joke" or "tell me a joke":
          req = requests.get("https://v2.jokeapi.dev/joke/Programming")
          joke = req.json()
          if joke['type'] == 'twopart':
            await message.channel.send(joke['setup'])
            await message.channel.send(joke['delivery'])
          else:
            await message.channel.send(joke['joke'])
keep_alive()
token = os.environ.get('code')
client.run(token)
