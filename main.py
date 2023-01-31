import discord
from discord import Option
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

bot = discord.Bot(debug_guilds=["GUILD_ID"])


class BookBot(discord.Bot):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


    @bot.event
    async def on_ready(self):
        print(f"{bot.user} is logged in and reporting for duty!)")




client = BookBot()


client.run(os.geetenv("TOKEN"))
