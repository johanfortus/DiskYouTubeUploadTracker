import requests
from constants import DISCORD_TOKEN, YOUTUBE_API_KEY, DISCORD_CHANNEL_ID, CHANNELS


class UploadChecker:

    def __init__(self, YOUTUBE_API_KEY, CHANNELS):

        self.YOUTUBE_API_KEY = YOUTUBE_API_KEY

        self.CHANNELS = CHANNELS

        self.LAST_UPLOADS = []


    def is_short(self, video_id):
        url = f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&part=contentDetails&key={self.YOUTUBE_API_KEY}"
        res = requests.get(url).json()
        print(f"Video ID: {video_id}")
        return "M" not in res["items"][0]["contentDetails"]["duration"]

    def get_latest_videos(self, channel_id):
        pass

    async def check_uploads(self):
        pass



UploadChecker = UploadChecker(YOUTUBE_API_KEY, CHANNELS)