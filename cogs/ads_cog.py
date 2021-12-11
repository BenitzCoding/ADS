import discord
from utils import default
from cool_utils import Terminal
from discord.utils import get
from discord.ext import commands

class ADS_Plugin(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.config = default.get("./config.json")
		print('"ADS_Plugin" cog loaded')

	@commands.Cog.listener('on_ready')
	async def startup_scan(self):
		Terminal.display("Running Startup ADS Script.")
		blocked_users = self.config.users
		for guild in self.bot.guilds:
			if guild.owner_id in blocked_users:
				ss = get(self.bot.guilds, id=self.config.serverid)
				log = get(ss.text_channels, id=self.config.log)
				owner = await self.bot.fetch_user(guild.owner_id)
				await log.send(f":no_entry_sign: Blocked Server by **Anti-Dummy Server** Module, **Server:** {guild.name}(`{guild.id}`), **Owner:** `{owner.name}#{owner.discriminator}`(`{owner.id}`)")
				await guild.leave()
		Terminal.display("ADS Script has been executed successfully.")

	@commands.Cog.listener('on_guild_join')
	async def scan_new_guilds(self, guild):
		if guild.owner_id in self.config.users:
			ss = get(self.bot.guilds, id=self.config.serverid)
			log = get(ss.text_channels, id=self.config.log)
			owner = await self.bot.fetch_user(guild.owner_id)
			await log.send(f":no_entry_sign: Blocked Server by **Anti-Dummy Server** Module, **Server:** {guild.name}(`{guild.id}`), **Owner:** `{owner.name}#{owner.discriminator}`(`{owner.id}`)")
			await guild.leave()
		else:
			return

	@commands.command()
	@commands.is_owner()
	async def scan(self, ctx):
		message = await ctx.send(f"Scanning Guilds (0/{len(self.bot.guilds)})")
		blocked_users = self.config.users
		count = 0
		for guild in self.bot.guilds:
			count = count + 1
			await message.edit(f"Scanning Guilds ({count}/{len(self.bot.guilds)})")
			if guild.owner_id in blocked_users:
				ss = get(self.bot.guilds, id=self.config.serverid)
				log = get(ss.text_channels, id=self.config.log)
				owner = await self.bot.fetch_user(guild.owner_id)
				await log.send(f":no_entry_sign: Blocked Server by **Anti-Dummy Server** Module, **Server:** {guild.name}(`{guild.id}`), **Owner:** `{owner.name}#{owner.discriminator}`(`{owner.id}`)")
				await guild.leave()
		await message.edit(f"Scanned all guilds.")

def setup(bot):
	bot.add_cog(ADS_Plugin(bot))