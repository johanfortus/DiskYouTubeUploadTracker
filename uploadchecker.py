import requests
import isodate
from datetime import date
from constants import DISCORD_TOKEN, YOUTUBE_API_KEY, DISCORD_CHANNEL_ID, CHANNELS


class UploadChecker:

    def __init__(self, YOUTUBE_API_KEY, CHANNEL_ID):

        self.YOUTUBE_API_KEY = YOUTUBE_API_KEY
        self.CHANNEL_ID = CHANNEL_ID
        self.LAST_UPLOADS = []

        self.video_formats = {
            "livestream" : False,
            "longform" : False,
            "short" : False
        }

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

    def get_latest_videos(self):

        channel_url = f"https://www.googleapis.com/youtube/v3/channels?part=contentDetails&id={self.CHANNEL_ID}&key={YOUTUBE_API_KEY}"
        res = requests.get(channel_url).json()

        uploads_playlist_id = res["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
        playlist_url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={uploads_playlist_id}&key={YOUTUBE_API_KEY}"
        res = requests.get(playlist_url).json()

        videos = res["items"]
        return videos


    def check_uploads(self):

        new_upload = False
        current_date = str(date.today())
        videos = self.get_latest_videos()

        for video in videos:

            video_id = video["snippet"]["resourceId"]["videoId"]
            video_title = video["snippet"]["title"]
            video_upload_date = str(video["snippet"]["publishedAt"][0:10])

            if current_date == video_upload_date:

                if video_id not in self.LAST_UPLOADS:
                    self.LAST_UPLOADS.append(video_id)
                    new_upload = True

                print(f"Title: {video_title} \nID: {video_id} \nUpload Date: {video_upload_date} \n")

                match self.video_type(video_id):
                    case "livestream":
                        self.video_formats["livestream"] = True
                    case "longform":
                        self.video_formats["longform"] = True
                    case "short":
                        self.video_formats["short"] = True

        return new_upload




print(UploadChecker.check_uploads())