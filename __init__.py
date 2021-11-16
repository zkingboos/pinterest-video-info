from os import getenv
from discord.ext import commands
from discord.ext.commands import Context

from youtube_dl import YoutubeDL
from dotenv import load_dotenv

load_dotenv()  # Loads the environment variables from .env file


class EnviromentVariable(object):

    TOKEN: str = getenv("DISCORD_TOKEN")
    CHANNEL_ID: int = getenv("CHANNEL_ID")


class DiscordPinterestInfo(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=".")

        @self.command()
        async def info(context: Context, url: str):
            info = YoutubeDL({}).extract_info(url=url, download=False)
            # print(json.dumps(info))
            target_url_video = (
                info
                if info["url"].endswith(".mp4")
                else (
                    list(
                        filter(
                            lambda tuple: tuple["url"].endswith(".mp4"), info["formats"]
                        )
                    )
                )[0]
            )["url"]
            await context.send(target_url_video)

    async def on_ready(self):
        print(f"Logged as {self.user.name}")


client = DiscordPinterestInfo()
client.run(EnviromentVariable.TOKEN)
