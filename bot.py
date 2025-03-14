import discord
import requests
import json
import os
import datetime
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
DISCORD_CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))

CHANNELS = {
    "Vro" : os.getenv("CHANNEL_ID_ONE"),
    "Knight" : os.getenv("CHANNEL_ID_TWO"),
    "Splash" : os.getenv("CHANNEL_ID_THREE")
}

class Client(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}")

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(DISCORD_TOKEN)