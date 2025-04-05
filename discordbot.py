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
        upload_checker = UploadChecker(YOUTUBE_API_KEY, channel_id)
        upload_checkers.append(upload_checker)


def track_uploads():

    new_update = False
    longform_upload_status = "❌"
    short_upload_status = "❌"

    for upload_checker in upload_checkers:

        if upload_checker.tracker() == True:
            new_update = True

        if new_update:
            print(f"Livestream: {upload_checker.get_uploaded()['livestream']}")
            print(f"Longform: {upload_checker.get_uploaded()['longform']}")
            print(f"Short: {upload_checker.get_uploaded()['short']}")




check_uploads()
track_uploads()
