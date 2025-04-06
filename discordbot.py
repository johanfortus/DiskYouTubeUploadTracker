import discord
import requests
import os
from datetime import date
from dotenv import load_dotenv
from discord.ext import tasks
from constants import DISCORD_TOKEN, DISCORD_CHANNEL_ID, YOUTUBE_API_KEY, CHANNELS
from uploadchecker import UploadChecker

upload_checkers = []

def check_uploads():
    for i in CHANNELS:
        channel_id = CHANNELS[i]
        upload_checker = UploadChecker(YOUTUBE_API_KEY, channel_id, i)
        upload_checkers.append(upload_checker)


def track_uploads():

    new_update = False
    livestream_upload_status = "❌"
    longform_upload_status = "❌"
    short_upload_status = "❌"

    for upload_checker in upload_checkers:

        if upload_checker.tracker() == True:
            new_update = True

    if new_update:

        for upload_checker in upload_checkers:
            if upload_checker.get_uploaded()['livestream']:
                livestream_upload_status = "✅"
            if upload_checker.get_uploaded()['longform']:
                longform_upload_status = "✅"
            if upload_checker.get_uploaded()['short']:
                short_upload_status = "✅"

            print(f"Channel: {upload_checker.get_channel_name()}")
            print(f"Livestream: {livestream_upload_status}")
            print(f"Longform: {longform_upload_status}")
            print(f"Short: {short_upload_status}")



check_uploads()
track_uploads()
