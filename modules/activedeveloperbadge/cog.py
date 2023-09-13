from nextcord.ext import commands
from nextcord import Embed, Colour
import nextcord
import datetime

class ActiveDeveloperBadge(commands.Cog, name="ActiveDeveloperBadge"):
    """Receives active badge related commands"""

    def __int__(self, bot: commands.Bot):
        # self.is_playing = {}
        self.bot = bot

    @nextcord.slash_command(name='badge')
    async def badge(self, interaction: nextcord.Interaction):
        """Link to the discord developer page for the active developer badge"""
        message_date = interaction.created_at
        last_slash_command_date = datetime.datetime.strftime(message_date,"%m/%d/%Y")
        
        message_date_30 = message_date + datetime.timedelta(days=30)
        eligible_until_date = datetime.datetime.strftime(message_date_30,"%m/%d/%Y")
        
        em = Embed(title=f"Check your badge status here:", description="https://discord.com/developers/active-developer", color = Colour.random())
        em.add_field(name='**Last slash command ran:**', value=f'{last_slash_command_date}', inline=True)
        em.add_field(name='**Eligible until:**', value=f'{eligible_until_date}', inline=True)
        em.set_footer(text = interaction.user.name, icon_url = interaction.user.display_avatar)
        await interaction.send(embed=em)

def setup(bot: commands.Bot):
    bot.add_cog(ActiveDeveloperBadge(bot))