# If you want to execute ADS just once, you can run this script.
# You still need to fill in everything in config.json
import discord
from utils import default
from discord.utls import get
from discord.ext import discord

config = default.get('./config')

bot = commands.Bot(command_prefix="ADS!")

@bot.event
async def on_ready():
    print("Running ADS Script.")
	blocked_users = config.users
	for guild in bot.guilds:
		blocked_users = config.users
		if guild.owner_id in blocked_users:
			await guild.leave()
			ss = get(bot.guilds, id=config.serverid)
			log = get(ss.text_channels, id=config.log)
			await log.send(f":no_entry_sign: Blocked Server by **Anti-Dummy Server** Module, **Server_Name:** {guild.name}, **Server_ID:** {guild.id}")
	print("ADS Script Ended after on_ready.")

bot.run(config.token)
