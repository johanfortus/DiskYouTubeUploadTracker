import requests
import isodate
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

        # print(f"Hours: {hours}")
        # print(f"Minutes: {min}")
        # print(f"Seconds: {sec}")
        #
        # print(f"Parsed Duration: {parsed_duration}")
        #
        # return "M" not in res["items"][0]["contentDetails"]["duration"]

    def get_latest_videos(self, channel_id):
        pass

    async def check_uploads(self):
        pass



UploadChecker = UploadChecker(YOUTUBE_API_KEY, CHANNELS)