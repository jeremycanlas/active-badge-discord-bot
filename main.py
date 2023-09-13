# In order to get bot token from .env file so that bot token isn't exposed
import os
from dotenv import load_dotenv

# Library for python discord
from nextcord.ext import commands
import nextcord

load_dotenv()

intents = nextcord.Intents.all()
intents.members = True

# change type and name to change the activity of your bot
activity = nextcord.Activity(type= nextcord.ActivityType.listening, name='you')

# load in cogs for your bot to recognize
bot = commands.Bot(command_prefix='$', activity=activity, intents = intents)
for folder in os.listdir("modules"):
    if os.path.exists(os.path.join("modules", folder, "cog.py")):
        bot.load_extension(f"modules.{folder}.cog")

### Discord Events ###
### Function that prints a phrase when your discord bot goes online
@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))
  ### uncomment if you want your bot to show how many servers it's in
#   await bot.change_presence(activity=nextcord.Game(name="on " + str(len(bot.guilds)) + " Servers", type=0))

#Message based events
@bot.event
async def on_message(message):
    # prints out in console whenever someone chats in a channel
    await bot.process_commands(message)
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)
    print(f"{username} said: '{user_message}' ({channel})")
    message.content = message.content.lower()
    if message.author == bot.user:
        return
    if message.author.bot:
        return

bot.run(os.environ["token"])