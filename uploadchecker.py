import requests
import isodate
from constants import DISCORD_TOKEN, YOUTUBE_API_KEY, DISCORD_CHANNEL_ID, CHANNELS


class UploadChecker:

    def __init__(self, YOUTUBE_API_KEY, CHANNELS):

        self.YOUTUBE_API_KEY = YOUTUBE_API_KEY

        self.CHANNELS = CHANNELS

        self.LAST_UPLOADS = []


    def is_short(self, video_id):
        url = f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&part=contentDetails&key={self.YOUTUBE_API_KEY}"
        res = requests.get(url).json()

        duration = res["items"][0]["contentDetails"]["duration"]
        parsed_duration = str(isodate.parse_duration(duration)).split(":")

        hours = parsed_duration[0]
        minutes = parsed_duration[1]
        seconds = parsed_duration[2]

        print(f"Hours: {hours}")
        print(f"Minutes: {minutes}")
        print(f"Seconds: {seconds}")

        print(f"Parsed Duration: {parsed_duration}")



        return "M" not in res["items"][0]["contentDetails"]["duration"]

    def get_latest_videos(self, channel_id):
        pass

    async def check_uploads(self):
        pass



UploadChecker = UploadChecker(YOUTUBE_API_KEY, CHANNELS)