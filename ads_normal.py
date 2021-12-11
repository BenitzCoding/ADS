import discord
from utils import default
from cool_utils import Terminal
from discord.utils import get
from discord.ext import commands

config = default.get("./config.json")
bot = commands.Bot(command_prefix="ads!")

@bot.listen('on_ready')
async def startup_scan():
	Terminal.display("Running Startup ADS Script.")
	blocked_users = config.ads
	for guild in bot.guilds:
		blocked_users = config.users
		if guild.owner_id in blocked_users:
			ss = get(bot.guilds, id=config.serverid)
			log = get(ss.text_channels, id=config.log)
			owner = await bot.fetch_user(guild.owner_id)
			await log.send(f":no_entry_sign: Blocked Server by **Anti-Dummy Server** Module, **Server:** {guild.name}(`{guild.id}`), **Owner:** `{owner.name}#{owner.discriminator}`(`{owner.id}`)")
			await guild.leave()
	Terminal.display("ADS Script has been executed successfully.")

@bot.listen('on_guild_join')
async def scan_new_guilds(guild):
	if guild.owner_id in config.users:
			ss = get(bot.guilds, id=config.serverid)
			log = get(ss.text_channels, id=config.log)
			owner = await bot.fetch_user(guild.owner_id)
			await log.send(f":no_entry_sign: Blocked Server by **Anti-Dummy Server** Module, **Server:** {guild.name}(`{guild.id}`), **Owner:** `{owner.name}#{owner.discriminator}`(`{owner.id}`)")
			await guild.leave()
	else:
		return

@bot.command()
@commands.is_owner()
async def scan(ctx):
	message = await ctx.send(f"Scanning Guilds (0/{len(bot.guilds)})")
	blocked_users = config.users
	count = 0
	for guild in bot.guilds:
		count = count + 1
		await message.edit(f"Scanning Guilds ({count}/{len(bot.guilds)})")
		if guild.owner_id in blocked_users:
			ss = get(bot.guilds, id=config.serverid)
			log = get(ss.text_channels, id=config.log)
			owner = await bot.fetch_user(guild.owner_id)
			await log.send(f":no_entry_sign: Blocked Server by **Anti-Dummy Server** Module, **Server:** {guild.name}(`{guild.id}`), **Owner:** `{owner.name}#{owner.discriminator}`(`{owner.id}`)")
			await guild.leave()
	await message.edit(f"Scanned all guilds.")

bot.run(config.token)