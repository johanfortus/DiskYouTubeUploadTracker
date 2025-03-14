import discord
import requests
import json
import os
from datetime import date
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
        get_latest_videos(CHANNELS["Knight"])

intents = discord.Intents.default()
intents.message_content = True

def get_latest_videos(channel_id):

    today = date.today()
    print(f"Today: {today}")
    today = "2025-03-13"

    channel_url = f'https://www.googleapis.com/youtube/v3/channels?part=contentDetails&id={channel_id}&key={YOUTUBE_API_KEY}'
    res = requests.get(channel_url).json()
    uploads_playlist_id = res["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    playlist_url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={uploads_playlist_id}&maxResults=50&key={YOUTUBE_API_KEY}"
    res = requests.get(playlist_url).json()

    for item in res["items"]:
        video_upload_date = item["snippet"]["publishedAt"][0:10]
        video_title = item["snippet"]["title"]
        video_id = item["snippet"]["resourceId"]["videoId"]

        if today == video_upload_date:
            print(f"Title: {video_title}, ID: {video_id}, Upload Date: {video_upload_date}")






client = Client(intents=intents)
client.run(DISCORD_TOKEN)