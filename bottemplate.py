#
# Name : Dawid Nalepa
# ID : 2209302
#
import random
import sys
from config import config

# Define the random number generator
def generate_random_numbers(minNumber, maxNumber, howMany):
  return [random.randint(minNumber, maxNumber) for _ in range(howMany)]

# Insert your bot token here
discordToken = config.get("bot_token")
# Insert your bot name here
name = config.get("bot_name")

# Check if Token is empty
if (discordToken == ""): sys.exit("ERROR: Please set the discord token.")
# Check if Name is empty
if (name == ""): sys.exit("ERROR: Please set the name of the bot.")

# Import discord
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  if message.author == client.user: return # We don't want to reply to ourselves

  # RULE: To not flood the channel with responses from multiple bots,
  # we only respond to messages that start with our name

  if message.content.startswith(name):
    print(f"{message.author} says: {message.content}")

    msg = message.content[len(name):].strip()
    print(f"msg contains: {msg}")
    list = msg.split(" ")

    # DELETE THE PHRASE KEEPING ONLY PARAMATERS IN THE LIST
    command = list[0]
    del list[0]
    print(list)

    # IF MESSAGE STARTS WITH : HELLO
    if message.content.startswith(f'{name} hello'):
      await message.channel.send('Hello! I am ALIVE?')

    # IF MESSAGE STARTS WITH : RANDOM 
    elif message.content.startswith(f'{name} random'):
      # If list contains more than 3 parameters
      if len(list) > 3:
        await message.channel.send('Exterminate! Too many parameters!')
      # If list contains less than 3 parameters
      elif len(list) < 3:
        await message.channel.send('Exterminate! Too many parameters!')
      # Otherwise print the numbers
      else:
        if not list[0].isdigit() or not list[1].isdigit() or not list[2].isdigit():
          await message.channel.send('Exterminate! Only digits are allowed!')
        # Convert Strings to Integers
        else:
          min : int = int(list[0])
          max : int = int(list[1])
          quantity : int = int(list[2])
          await message.channel.send(f'Random numbers {generate_random_numbers(min,max,quantity)}')

    # IF MESSAGE STARTS WITH : SUM
    elif message.content.startswith(f'{name} sum'):
      # If list contains more than 3 parameters
      if len(list) > 2:
        await message.channel.send('Exterminate! Too many parameters!')
      # If list contains less than 3 parameters
      elif len(list) < 2:
        await message.channel.send('Exterminate! Too few parameters!')
      # Otherwise print the sum
      else:
        # Checks if the list contains numbers or strings
        if not list[0].isdigit() or not list[1].isdigit():
          await message.channel.send('Exterminate! Only digits are allowed!')
        # Convert Strings to Integers
        else:
          sum : int = int(list[0]) + int(list[1])
          await message.channel.send(f'Sum of numbers is: {sum}')

    # IF MESSAGE STARTS WITH : HELP
    elif message.content.startswith(f'{name} help'):
      await message.channel.send('**Here are some of the commands you can use**\n' +
                                 '**=========================================**\n' +
                                 '**-> random**\n' +
                                 '    **->** When asking the chatbot random <minNumber> <maxNumber> <howMany>,\n' + 
                                 '     it should give a random number between the two numbers and how many random\n' +
                                 '     numbers it generates.\n' +
                                 '    **->** So, for example, random 0 20 2 gives back 2 random numbers. The output should\n' + 
                                 '     be something like this: Random numbers 13 & 4.\n\n'
                                 '**-> sum**\n' +
                                 '    **->** When asking the chatbot sum <number1> <number2> it should sum up the numbers.\n' +
                                 '    **->** So, for example, sum 160 20  should return back 180.\n\n' +
                                 '**-> hello**\n' +
                                 '  **->** Be nice to the bot, say hello :grin:')

client.run(discordToken)