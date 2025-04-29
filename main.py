import discord
import requests
import os
from datetime import date
from dotenv import load_dotenv
from discord.ext import tasks

def main():

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

if __name__ == "__main__":
    main()