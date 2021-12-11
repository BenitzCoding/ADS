# If you want to execute ADS just once, you can run this script.
# You still need to fill in everything in config.json
import discord
from utils import default
from cool_utils import Terminal
from discord.utils import get
from discord.ext import commands

config = default.get('./config')

bot = commands.Bot(command_prefix="ADS!")

@bot.event('on_ready')
async def startup_scan():
	Terminal.display("Running Startup ADS Script.")
	blocked_users = config.users
	for guild in bot.guilds:
		blocked_users = config.users
		if guild.owner_id in blocked_users:
			ss = get(bot.guilds, id=config.serverid)
			log = get(ss.text_channels, id=config.log)
			owner = await bot.fetch_user(guild.owner_id)
			await log.send(f":no_entry_sign: Blocked Server by **Anti-Dummy Server** Module, **Server:** {guild.name}(`{guild.id}`), **Owner:** `{owner.name}#{owner.discriminator}`(`{owner.id}`)")
			await guild.leave()
	Terminal.display("ADS Script has been executed successfully.")

bot.run(config.token)
