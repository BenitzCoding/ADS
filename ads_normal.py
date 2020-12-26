import discord
from utils import default
from discord.utils import get
from discord.ext import commands

config = default.get("./config.json")

@bot.event
async def on_ready():
	print("Running ADS Script.")
	blocked_users = config.ads
	for guild in bot.guilds:
		blocked_users = config.users
		if guild.owner_id in blocked_users:
			await guild.leave()
			ss = get(bot.guilds, id=config.serverid)
			log = get(ss.text_channels, id=config.log)
			await log.send(f":no_entry_sign: Blocked Server by **Anti-Dummy Server** Module, **Server_Name:** {guild.name}, **Server_ID:** {guild.id}")
	print("ADS Script Ended after on_ready.")

@bot.event
async def on_guild_join(guild):
	if guild.owner_id in config.users:
		await guild.leave()
		ss = get(bot.guilds, id=config.serverid)
		log = get(ss.text_channels, id=config.log)
		await log.send(f":no_entry_sign: Blocked Server by **Anti-Dummy Server** Module, **Server_Name:** {guild.name}, **Server_ID:** {guild.id}")
	else:
		return

@bot.command()
@commands.is_owner()
async def run_ads(ctx):
	await ctx.send("Running ADS Script.")
	blocked_users = config.users
	for guild in bot.guilds:
		if guild.owner_id in blocked_users:
			await guild.leave()
			ss = get(bot.guilds, id=config.serverid)
			log = get(ss.text_channels, id=config.log)
			await log.send(f":no_entry_sign: Blocked Server by **Anti-Dummy Server** Module, **Server_Name:** {guild.name}, **Server_ID:** {guild.id}")
	await ctx.send("ADS Script Ended.")

bot.run(config.token)