import discord
from discord.ext import commands
from config import TOKEN
from career_data import CAREER_DATA

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")

@bot.command()
async def career(ctx, interest=None):
    if interest is None:
        await ctx.send(
            "Please specify an interest area.\n"
            "Example: `!career software`, `!career design`, `!career game`"
        )
        return

    interest = interest.lower()

    if interest not in CAREER_DATA:
        await ctx.send("No data found for this interest area.")
        return

    career = CAREER_DATA[interest]

    message = (
        f"🎯 **{career['title']}**\n"
        f"📌 {career['description']}\n"
        f"🛠 Required Skills: {', '.join(career['skills'])}\n"
        f"🛤 Career Path: {career['career_path']}"
    )

    await ctx.send(message)

bot.run(TOKEN)
