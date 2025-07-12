import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import json
import random
import os

load_dotenv()
### LOGIC FOR GET PHRASE
def get_random_phrase():
    with open("phrases.json", "r", encoding="utf-8") as f:
        phrases = json.load(f)
    return random.choice(phrases)

### Logic for DISCORD MESSAGE
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID")) 

print("starting Script Discord....")
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f"We are ready to go in, {client.user.name}")


@client.event
async def on_ready():
    print(f'Bot conectado como {client.user}')
    channel = client.get_channel(CHANNEL_ID)
    if channel:
            phrase = get_random_phrase()
            mensaje = f'**"{phrase["title"]}"**\n— *{phrase["author"]}*'
            await channel.send(mensaje)
    await client.close()

client.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)