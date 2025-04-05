

class UploadChecker:

    def __init__(self, YOUTUBE_API_KEY, DISCORD_CHANNEL_ID, CHANNELS):

        self.YOUTUBE_API_KEY = YOUTUBE_API_KEY
        self.DISCORD_CHANNEL_ID = DISCORD_CHANNEL_ID

        self.CHANNELS = CHANNELS

        self.LAST_UPLOADS = []

    def is_short(self, video_id):
        pass

    def get_latest_videos(self, channel_id):
        pass

    async def check_uploads(self):
        pass

