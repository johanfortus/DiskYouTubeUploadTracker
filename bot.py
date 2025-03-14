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

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def is_short(video_id):
    url = f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&part=contentDetails&key={YOUTUBE_API_KEY}"
    res = requests.get(url).json()
    return "M" not in res["items"][0]["contentDetails"]["duration"]


def get_latest_videos(channel_id):

    longform_upload_status = "❌"
    short_upload_status = "❌"

    today = date.today()

    channel_url = f"https://www.googleapis.com/youtube/v3/channels?part=contentDetails&id={channel_id}&key={YOUTUBE_API_KEY}"
    res = requests.get(channel_url).json()
    uploads_playlist_id = res["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    playlist_url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={uploads_playlist_id}&publishedAfter={today}&key={YOUTUBE_API_KEY}"
    res = requests.get(playlist_url).json()

    for item in res["items"]:
        video_upload_date = item["snippet"]["publishedAt"][0:10]
        video_title = item["snippet"]["title"]
        video_id = item["snippet"]["resourceId"]["videoId"]

        if today == video_upload_date:
            # print(f"Title: {video_title}, ID: {video_id}, Upload Date: {video_upload_date}")
            if is_short(video_id):
                short_upload_status = "✅"
            else:
                longform_upload_status = "✅"

    message = f"- Longform {longform_upload_status} \n - Short {short_upload_status}"

    return message


async def check_uploads():
    today = date.today()
    message = f"**TMNT FREEBUILD** \n Date: {today} \n \n"
    for i in CHANNELS:
        # print(i)
        channel_id = CHANNELS[i]

        channel_url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={YOUTUBE_API_KEY}"
        res = requests.get(channel_url).json()
        subscriber_count = res["items"][0]["statistics"]["subscriberCount"]
        print(f"Subscribers: {subscriber_count}")

        message += f"**[{i}](https://www.youtube.com/{channel_id})** - {subscriber_count} subscribers \n"
        message+=get_latest_videos(channel_id)+"\n\n"

    print(message)
    channel = client.get_channel(DISCORD_CHANNEL_ID)
    await channel.send(message)

@client.event
async def on_ready():
    print(f"Logged on as {client.user}")
    await check_uploads()
    # get_latest_videos(CHANNELS["Knight"])

client.run(DISCORD_TOKEN)