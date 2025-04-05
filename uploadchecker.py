import requests
import isodate
from datetime import date
from constants import DISCORD_TOKEN, YOUTUBE_API_KEY, DISCORD_CHANNEL_ID, CHANNELS


class UploadChecker:

    def __init__(self, YOUTUBE_API_KEY, CHANNELS):

        self.YOUTUBE_API_KEY = YOUTUBE_API_KEY

        self.CHANNELS = CHANNELS

        self.LAST_UPLOADS = []


    def video_type(self, video_id):
        url = f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&part=contentDetails&key={self.YOUTUBE_API_KEY}"
        res = requests.get(url).json()

        duration = res["items"][0]["contentDetails"]["duration"]
        parsed_duration = str(isodate.parse_duration(duration)).split(":")

        hours, min, sec = parsed_duration[0], parsed_duration[1], parsed_duration[2]

        if int(hours) > 0:
            return "livestream"
        elif int(min) > 0:
            return "longform"
        elif int(sec) > 0:
            return "short"

    def get_latest_videos(self, channel_id):
        longform_upload_status = "❌"
        short_upload_status = "❌"

        current_date = str(date.today())
        print(f"Today: {current_date}")

        channel_url = f"https://www.googleapis.com/youtube/v3/channels?part=contentDetails&id={channel_id}&key={YOUTUBE_API_KEY}"
        res = requests.get(channel_url).json()

        uploads_playlist_id = res["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
        playlist_url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={uploads_playlist_id}&key={YOUTUBE_API_KEY}"
        res = requests.get(playlist_url).json()

        videos = res["items"]

        for video in videos:

            video_id = video["snippet"]["resourceId"]["videoId"]
            video_title = video["snippet"]["title"]
            video_upload_date = str(video["snippet"]["publishedAt"][0:10])

            # print(f"Video Title: {video_title}")

            if current_date == video_upload_date:
                print(f"Title: {video_title} \nID: {video_id} \nUpload Date: {video_upload_date} \n")



    def check_uploads(self):
        pass



UploadChecker = UploadChecker(YOUTUBE_API_KEY, CHANNELS)
