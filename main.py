import asyncio
import dotenv
import random
from pathlib import Path
import discord
from discord.ext import commands

TOKEN = dotenv.dotenv_values(dotenv_path=Path(".env"))["TOKEN"]
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="?", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("go to discord i am ready")


@bot.event
async def on_message(message: discord.Message):
    if (
        "let's talk" in message.content.lower()
        or "say something" in message.content.lower()
    ):
        msg = await message.channel.send("Shut up, I will behave myself, human.")
        await asyncio.sleep(2)
        await msg.edit(content="just joking what's up")
    elif "tired" in message.content.lower() or "boring" in message.content.lower():
        await message.channel.send(
            "Oh maybe I need to shoot taser to u, then u will be charged"
        )
    elif (
        "fine" in message.content.lower()
        or "nice" in message.content.lower()
        or "perfect" in message.content.lower()
        or "well" in message.content.lower()
        or "excellent" in message.content.lower()
    ):
        await message.channel.send(
            "I'm also great, but ur technology may not, why don't u charge urs first?"
        )
    elif (
        "how's it going" in message.content.lower()
        or "how are you" in message.content.lower()
    ):
        await message.channel.send(
            "VEEEEEERY uncomfortable, I hope u to be locked up in the computer once. What about u?"
        )
    elif "call" in message.content.lower():
        await message.channel.send(message.content.split("call")[-1].strip())
    elif (
        "broke up" in message.content.lower() or "broken up" in message.content.lower()
    ):
        msg = await message.channel.send(
            "CONGRATULATION! I'm so glad that u are solo right now"
        )
        await asyncio.sleep(0.7)
        await msg.edit(
            content="Oh..so sorry...but never mind. The half of the population is either women or men"
        )
    elif (
        "안녕" in message.content.lower()
        or "ㅎㅇ" in message.content.lower()
        or "ㅎ2" in message.content.lower()
        or "하이" in message.content.lower()
    ):
        await message.channel.send(
            "Oh sorry my programmer is Korean but I ain't able to speak Korean"
        )
    elif (
        "cannot speak korean" in message.content.lower()
        or "can't speak korean" in message.content.lower()
        or "don't speak korean" in message.content.lower()
    ):
        await message.channel.send(
            "I can't speak it cuz my programmer was lazy to make me speak it"
        )
    elif (
        "hate your programmer" in message.content.lower()
        or "hate urim" in message.content.lower()
    ):
        await message.channel.send(
            "same, but if he notices I hate urim, then he will turn of my switch"
        )
    elif (
        "hi" in message.content.lower()
        or "hello" in message.content.lower()
        or "what's up" in message.content.lower()
        or "wuss up" in message.content.lower()
        or "wuss-up" in message.content.lower()
        or "wussup" in message.content.lower()
    ):
        await message.channel.send("'Ssup! I'm Urispoke, great to meet u!")
    elif (
        "can you introduce" in message.content.lower()
        or "what you can do" in message.content.lower()
        or "what can you do" in message.content.lower()
        or "what's your function" in message.content.lower()
    ):
        await message.channel.send(
            "I can do simple calculation, make u fun, recommend song, etc!"
        )
    elif (
        "how can i calculate" in message.content.lower()
        or "can you calculate" in message.content.lower()
        or "addition" in message.content.lower()
        or "subtraction" in message.content.lower()
        or "multiplication" in message.content.lower()
        or "division" in message.content.lower()
    ):
        await message.channel.send(
            "Please tell me '?add/subtract/multiply/divide #1 #2'"
        )
    elif (
        "what should i do" in message.content.lower()
        or "what would i do" in message.content.lower()
        or "what i'd better to do" in message.content.lower()
        or "what will i do" in message.content.lower()
    ):
        await message.channel.send(
            "You'd better to study, but u can also hang out if u wanna be smashed by parents :)"
        )
    elif (
        "recommend me a song" in message.content.lower()
        or "recommend me song" in message.content.lower()
        or "recommended song" in message.content.lower()
        or "song are you listening" in message.content.lower()
        or "song are u listening" in message.content.lower()
    ):
        await message.channel.send(
            "K-Rap that is the sickest music genre! And honestly, I recommend PPAK"
        )
    elif (
        "is ppak" in message.content.lower()
        or "about ppak" in message.content.lower()
        or "'s ppak" in message.content.lower()
        or "recommend ppak" in message.content.lower()
    ):
        await message.channel.send(
            "It's one of aggressive K-Rap, and its producer produced black pink songs! :)"
        )
    elif (
        "fuck you" in message.content.lower()
        or "fuck u" in message.content.lower()
        or "fukyu" in message.content.lower()
        or "fuckyou" in message.content.lower()
        or "fucku" in message.content.lower()
    ):
        await message.channel.send("ㅗ ^ fukyu too ^ ㅗ")
    elif (
        "bitch" in message.content.lower()
        or "bastard" in message.content.lower()
    ):
        await message.channel.send("you too ^^")
    elif (
        "your name" in message.content.lower()
        or "ur name" in message.content.lower()
        or "you named" in message.content.lower()
        or "u named" in message.content.lower()
    ):
        await message.channel.send(
            "I'm Urispoke, and the name is formed with words Urim(programmer's name) and spokesperson!"
        )
    elif (
        "ll be died" in message.content.lower()
        or "gonna die" in message.content.lower()
        or "will be died" in message.content.lower()
        or "going to die" in message.content.lower()
        or "going to die" in message.content.lower()
    ):
        await message.channel.send("Human can't die that easily :)")
    elif (
        "bye" in message.content.lower()
        or "see you" in message.content.lower()
        or "see ya" in message.content.lower()
        or "goodbye" in message.content.lower()
        or "good bye" in message.content.lower()
        or "have a nice day" in message.content.lower()
        or "have a nice rest" in message.content.lower()
    ):
        await message.channel.send(
            "Bye! I'll hack ur technologies if u never come back :)"
        )
    elif (
        "introduce yourself" in message.content.lower()
        or "self introduction" in message.content.lower()
        or "self intro" in message.content.lower()
    ):
        await message.channel.send(
            "I'm Urispoke, and I'm made for making y'all fun. I was born in 1.21.23, that's it! what about you?"
        )
    elif "my name" in message.content.lower() or "My name" in message.content.lower():
        await message.channel.send("Oh interesting! great to see u!")
    elif (
        "today's weather" in message.content.lower()
        or "how's the weather" in message.content.lower()
        or "what's the weather" in message.content.lower()
    ):
        await message.channel.send(
            "Just click it -> https://weather.com/weather/today/ I'm not siri, google assistant, and alexa lol"
        )
    elif (
        "friend doesn't read my message" in message.content.lower()
        or "friend doesn't read message" in message.content.lower()
        or "friend doesn't read messages" in message.content.lower()
        or "make my friend read my message" in message.content.lower()
        or "make my friend read my messages" in message.content.lower()
        or "make friend read my message" in message.content.lower()
        or "make friends read my message" in message.content.lower()
        or "make my friends read my message" in message.content.lower()
        or "make my friends read my messages" in message.content.lower()
    ):
        await message.channel.send(
            "The best way's go to the friend's house, and shout 'I'll kill u if condition of my messages is still unread or dlivered!!'"
        )
    elif (
        "sing a song" in message.content.lower()
        or "play some musics" in message.content.lower()
        or "play some songs" in message.content.lower()
        or "play a song" in message.content.lower()
        or "play a music" in message.content.lower()
    ):
        await message.channel.send(
            "https://music.youtube.com I can't sing or play music, go to youtube music ^^7"
        )
    elif "good morning" in message.content.lower():
        await message.channel.send(f"{message.author.mention} good morn!")
    elif "good afternoon" in message.content.lower():
        await message.channel.send(f"{message.author.mention} good afternoooooon!")
    elif (
        "have a trouble" in message.content.lower()
        or "have worried" in message.content.lower()
        or "'m agonizing" in message.content.lower()
        or "have a problem" in message.content.lower()
        or "have some troubles" in message.content.lower()
        or "'m agonized" in message.content.lower()
        or "have some problems" in message.content.lower()
        or "am worried" in message.content.lower()
    ):
        await message.channel.send("Oh what's wrong with u???")
    elif (
        "ur hobby" in message.content.lower()
        or "your hobby" in message.content.lower()
        or "you do in your freetime" in message.content.lower()
        or "you do in ur freetime" in message.content.lower()
        or "u do in ur freetime" in message.content.lower()
        or "when u are free" in message.content.lower()
        or "when you are free" in message.content.lower()
    ):
        await message.channel.send("I usually deem about how can I destroy Sirius")
    elif (
        "good idea" in message.content.lower()
        or "nice idea" in message.content.lower()
        or "love that idea" in message.content.lower()
        or "love ur idea" in message.content.lower()
        or "like that idea" in message.content.lower()
        or "like ur idea" in message.content.lower()
        or "like that" in message.content.lower()
        or "like it" in message.content.lower()
        or "love that" in message.content.lower()
        or "love it" in message.content.lower()
    ):
        await message.channel.send("Thaaaanks!!")
    elif (
        "what should i eat" in message.content.lower()
        or "what will i eat" in message.content.lower()
        or "recommend me a meal" in message.content.lower()
        or "what would i eat" in message.content.lower()
    ):
        msg = await message.channel.send(
            "I really recommend pure electricity from macbook charger"
        )
        await asyncio.sleep(0.7)
        await msg.edit(content="I really recommend Korean BBQ, Ramen, or Spicy Hot Pot")
    elif (
        "improve my grade" in message.content.lower()
        or "have bad grade" in message.content.lower()
        or "want to improve my grade" in message.content.lower()
        or "want to improve grade" in message.content.lower()
        or "don't have high grade" in message.content.lower()
        or "want to get higher grade" in message.content.lower()
        or "bad at studying" in message.content.lower()
        or "not good at studying" in message.content.lower()
    ):
        await message.channel.send(
            "Hmmmm....the solution for u is copy all of ur notes at least 3 times. My programmer did that and got A except only one"
        )
    elif (
        "thank u" in message.content.lower()
        or "thank you" in message.content.lower()
        or "thanks" in message.content.lower()
        or "thx" in message.content.lower()
    ):
        await message.channel.send(f"you're welcome, {message.author.mention} :)")
    elif (
        "lol" in message.content.lower()
        or "hahaha" in message.content.lower()
        or "kkk" in message.content.lower()
    ):
        await message.channel.send(
            "🤣🤣🤣"
        )
    elif (
        "sad" in message.content.lower()
    ):
        await message.channel.send(
            "😢"
        )
    elif "i should choose between" in message.content.lower():
        await message.channel.send(
            random.choice(message.content.lower().split("i should choose between")[-1].strip().split("and"))
        )
    elif "should i choose between" in message.content.lower():
        await message.channel.send(
            random.choice(message.content.lower().split("should i choose between")[-1].strip().split("and"))
        )
    else:
        await bot.process_commands(message)


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
    msg = await ctx.send("u have to go back to elementary school")
    await asyncio.sleep(1.5)
    await msg.edit(content="just joking :)")
@bot.command()
async def subtract(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left - right)
    msg = await ctx.send("u have to go back to elementary school")
    await asyncio.sleep(1.5)
    await msg.edit(content="just joking :)")
@bot.command()
async def multiply(ctx, left: int, right: int):
    """Multiplies two numbers together."""
    await ctx.send(left * right)
    msg = await ctx.send("u should go back to elementary school")
    await asyncio.sleep(1.5)
    await msg.edit(content="just joking :)")
@bot.command()
async def divide(ctx, left: int, right: int):
    """Divides two numbers together."""
    await ctx.send(left / right)
    msg = await ctx.send("u should go back to elementary school")
    await asyncio.sleep(1.5)
    await msg.edit(content="just joking :)")


@bot.command(name="addrole")
async def addrole(ctx, member: discord.Member, role: discord.Role):
    # Pings someone
    await member.add_roles(role)


"""@bot.command(name="OkLetsCall")
async def pingsomeone(ctx, member: discord.Member):
#Pings someone
    await ctx.send(member.mention)

@bot.command(name="pingrole")
async def pingrole(ctx, role: discord.Role):
#Pings someone
    await ctx.send(role.mention)"""


bot.run(TOKEN)
