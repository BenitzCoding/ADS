import discord
from utils import default
from discord.utils import get
from discord.ext import commands

class ADS_Plugin(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.config = default.get("./config.json")
		print('"ADS_Plugin" cog loaded')

	@commands.Cog.listener()
	async def on_ready():
		print("Running ADS Script.")
		blocked_users = self.config.users
		for guild in bot.guilds:
			if guild.owner_id in blocked_users:
				await guild.leave()
				ss = get(bot.guilds, id=self.config.serverid)
				log = get(ss.text_channels, id=self.config.log)
				await log.send(f":no_entry_sign: Blocked Server by **Anti-Dummy Server** Module, **Server_Name:** {guild.name}, **Server_ID:** {guild.id}")
		print("ADS Script Ended after on_ready.")

	@commands.Cog.listener()
	async def on_guild_join(self, guild):
		if guild.owner_id in self.config.users:
			await guild.leave()
			ss = get(self.bot.guilds, id=self.config.serverid)
			log = get(ss.text_channels, id=self.config.log)
			await log.send(f":no_entry_sign: Blocked Server by **Anti-Dummy Server** Module, **Server_Name:** {guild.name}, **Server_ID:** {guild.id}")
		else:
			return

	@commands.command()
	@commands.is_owner()
	async def run_ads(self, ctx):
		await ctx.send("Running ADS Script.")
		blocked_users = self.config.users
		for guild in self.bot.guilds:
			if guild.owner_id in blocked_users:
				await guild.leave()
				ss = get(self.bot.guilds, id=self.config.serverid)
				log = get(ss.text_channels, id=self.config.log)
				await log.send(f":no_entry_sign: Blocked Server by **Anti-Dummy Server** Module, **Server_Name:** {guild.name}, **Server_ID:** {guild.id}")
		await ctx.send("ADS Script Ended.")

def setup(bot):
	bot.add_cog(ADS_Plugin(bot))