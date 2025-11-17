import discord
from discord import File
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import random
import time
from collections import defaultdict
from datetime import timedelta
import webserver

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

message_times = defaultdict(list)

SPAM_WINDOW = 10
SPAM_THRESHOLD = 5
TIMEOUT_DURATION = 60

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

towers_nst = [
    "Jeff",
    "Rob",
    "MNI",
    "Mr. Squirt",
    "Bald Boi",
    "Mr. Sniper",
    "Bomber",
    "Funsized",
    "Mr. No Name"
]

towers_shards = [
    "Jeff",
    "Rob",
    "MNI",
    "Mr. Squirt",
    "Bald Boi",
    "Mr. Sniper",
    "Bomber",
    "Funsized",
    "Mr. No Name",
    "Mr. Fries",
    "Beamer"
]

towers_levels = [
    "Jeff",
    "Rob",
    "MNI",
    "Mr. Squirt",
    "Bald Boi",
    "Mr. Sniper",
    "Bomber",
    "Funsized",
    "Mr. No Name",
    "Mr. Cold",
    "Reanimator",
    "Pyromaniac",
    "Destroyer",
]

towers_all = [
    "Jeff",
    "Rob",
    "MNI",
    "Mr. Squirt",
    "Bald Boi",
    "Mr. Sniper",
    "Bomber",
    "Funsized",
    "Mr. No Name",
    "Mr. Fries",
    "Beamer",
    "Mr. Cold",
    "Reanimator",
    "Pyromaniac",
    "Destroyer",
]

challenges = [
    "NST Insanity (with others)",
    "Only Jeff Hard mode (with others)",
    "Random loadout hard mode (with others)",
    "Random loadout Insanity (with others)",
    "NST Insanity (Solo)",
    "Only Jeff Hard Mode (Solo)",
    "Random loadout hard mode (Solo)",
    "Random loadout Insanity (Solo)",
]

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"We are ready to go in, {bot.user.name}!")

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server, {member.name}! Remember to read the rules in #rules!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    now = time.time()
    user_id = message.author.id
    
    if "shit" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, Just say 'poop', it's not that hard! Also saying things like that can get you punished.")
    elif "fuck" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, Bit rude, innit? Swearing is punishable!")
    elif "motherfucker" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, We don't allow swearing! It's punishable!")
    elif "bastard" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, That's very rude. Anything ruder than that and ur cooked.")
    elif "bitch" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} not slay ❌💅❌")
    elif "meanie-head" in message.content.lower():
        await message.delete()
        await message.channel.send(f"no ur a meanie head, {message.author.mention}")
    elif "dick" in message.content.lower():
        await message.delete()
        await message.channel.send(f"💀 {message.author.mention}")
    elif "ass" in message.content.lower():
        await message.delete()
        await message.channel.send(f"come on maaaaaannnnn!!!, {message.author.mention}")

    message_times[user_id].append(now)

    message_times[user_id] = [
        t for t in message_times[user_id] if now - t < SPAM_WINDOW
    ]

    if len(message_times[user_id]) >= SPAM_THRESHOLD:

        try:
            # timeout the user
            until = discord.utils.utcnow() + timedelta(seconds=TIMEOUT_DURATION)
            await message.author.timeout(until, reason="Spam detected")

            await message.channel.send(
                f"{message.author.mention} has been timed out for spamming (10 minutes)."
            )

        except Exception as e:
            print("Error timing out:", e)

        # Reset their timestamps to avoid repeated triggers
        message_times[user_id].clear()

    await bot.process_commands(message)

@bot.command()
async def greet(ctx):
    greeting = random.randint(1, 7)
    if greeting == 1:
        await ctx.send(f"Why hello, {ctx.author.mention}!")
    if greeting == 2:
        await ctx.send(f"{ctx.author.mention}, hello!")
    if greeting == 3:
        await ctx.send(f"Hello there, {ctx.author.mention}!")
    if greeting == 4:
        await ctx.send(f"Hi, {ctx.author.mention}!")
    if greeting == 5:
        await ctx.send(f"Nice to see you, {ctx.author.mention}!")
    if greeting == 6:
        await ctx.send(f"Hi there, {ctx.author.mention}!")
    if greeting == 7:
        await ctx.send(f"Hiya {ctx.author.mention}!")

@bot.command()
async def smalltalk(ctx):
    await ctx.reply("I hope your day was good and all that stuff")

@bot.command()
async def poll(ctx, *, question):
    embed = discord.Embed(title=f"{ctx.author.name} Asks:", description=question)
    poll_message = await ctx.send(embed=embed)

    await poll_message.add_reaction("👍")
    await poll_message.add_reaction("👎")

@bot.command()
async def funne(ctx):
    funne_img = random.randint(1, 5)

    if funne_img == 1:
        await ctx.send(f"{ctx.author.mention}     3 guess globle", file=File("imgs/3guess.png"))
    elif funne_img == 2:
        await ctx.send(f"{ctx.author.mention}     average rich asian household", file=File("imgs/rayan.png"))
    elif funne_img == 3:
        await ctx.send(f"{ctx.author.mention}     He's every furry's arch nemesis, and he doesn't even know it.", file=File("imgs/Jobbot.webp"))
    elif funne_img == 4:
        await ctx.send(f"{ctx.author.mention}     When i turn red, run.", file=File("imgs/MAD.png"))
    elif funne_img == 5:
        await ctx.send(f"{ctx.author.mention}     penutt", file=File("imgs/PeanutParallax_3.png"))

@bot.command()
async def loadout_nst(ctx):
    towers_picked = random.sample(towers_nst, 5)
    
    await ctx.send(f"{ctx.author.mention}                            One Loadout, No special towers, comin' up!")
    await ctx.send(
        f"1. {towers_picked[0]}, "
        f"2. {towers_picked[1]}, "
        f"3. {towers_picked[2]}, "
        f"4. {towers_picked[3]}, "
        f"5. {towers_picked[4]}"
    )

@bot.command()
async def loadout_lt(ctx):
    towers_picked = random.sample(towers_levels, 5)
    
    await ctx.send(f"{ctx.author.mention}                            One Loadout, Level towers included, comin' up!")
    await ctx.send(
        f"1. {towers_picked[0]}, "
        f"2. {towers_picked[1]}, "
        f"3. {towers_picked[2]}, "
        f"4. {towers_picked[3]}, "
        f"5. {towers_picked[4]}"
    )

@bot.command()
async def loadout_st(ctx):
    towers_picked = random.sample(towers_shards, 5)
    
    await ctx.send(f"{ctx.author.mention}                            One Loadout, With shard towers, comin' up!")
    await ctx.send(
        f"1. {towers_picked[0]}, "
        f"2. {towers_picked[1]}, "
        f"3. {towers_picked[2]}, "
        f"4. {towers_picked[3]}, "
        f"5. {towers_picked[4]}"
    )

@bot.command()
async def loadout_all(ctx):
    towers_picked = random.sample(towers_all, 5)
    
    await ctx.send(f"{ctx.author.mention}                            One Loadout, All towers included, comin' up!")
    await ctx.send(
        f"1. {towers_picked[0]}, "
        f"2. {towers_picked[1]}, "
        f"3. {towers_picked[2]}, "
        f"4. {towers_picked[3]}, "
        f"5. {towers_picked[4]}"
    )

@bot.command()
async def challenge_me(ctx):
    selected_challenge = random.sample(challenges, 1)
    await ctx.send(f"{ctx.author.mention}, I dare you to complete: {selected_challenge}.")

@bot.command()
async def shredder(ctx):
    await ctx.send(f"{ctx.author.mention} DON'T USE THAT WORD!! I'M GETTING FLASHBACKS...")
    await ctx.send("When i was a child, i tragically lost my parents...")
    await ctx.send("Sitting happily ontop of co-worker dave's documents pile, my parents and i were happy as ever.")
    await ctx.send("Then, co-worker dave moved my parents to the pile beside us.. the post-it note read: 'Outdated documents'.")
    await ctx.send("I was fine with this. i knew we could just live serperatley, but then, boss bob strolled by.")
    await ctx.send("'Co-worker dave, when on earth are you going to SHRED those out-dated documents?'")
    await ctx.send("'Why just now, boss, i'm on my way!' I knew i had to save my parents before it was too late.")
    await ctx.send("I jumped onto their pile just as dave picked us up. he marched us for what felt like ages.. to the dreaded shredder.")
    await ctx.send("One by one, the documents went in.. i tried to warn my parents, but they were fast asleep. in they went..")
    await ctx.send("I jumped off the pile and ran for the door, slipping under and escaping to my new lair.")
    await ctx.send("I was raised by mice.. who sent me to pre-school. I was not a nice child.")
    await ctx.send("Then i knocked over this guy's blocks. he.. he..")
    await ctx.send("TOLD THE TEACHER.")

webserver.keep_alive()
bot.run(token, log_handler=handler, log_level=logging.DEBUG)
