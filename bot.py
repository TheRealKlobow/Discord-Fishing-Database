import discord
from discord import app_commands
import aiosqlite
import os

intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

DATABASE = "fangster.db"

# Start database and create table if it does not exist
async def init_db():
    async with aiosqlite.connect(DATABASE) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS fangster (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            fish_type TEXT,
            kg REAL,
            cm REAL,
            image_url TEXT
        )
        """)
        await db.commit()

# Update bot status with total number of catches
async def update_status():
    async with aiosqlite.connect(DATABASE) as db:
        async with db.execute("SELECT COUNT(*) FROM fangster") as cursor:
            count = (await cursor.fetchone())[0]
    await bot.change_presence(activity=discord.Game(name=f"Total Registered Catches: {count}"))

@bot.event
async def on_ready():
    await init_db()
    await tree.sync()
    await update_status()
    print(f"Bot ready as {bot.user}")

# Slash command to register a catch
@tree.command(name="catch", description="Register a catch")
@app_commands.describe(
    type="Fish type",
    kg="Weight in kilos",
    cm="Length in cm",
    image="Image of the catch"
)
async def catch(interaction: discord.Interaction, type: str, kg: float, cm: float, image: discord.Attachment):
    # Approved fish types - channel names are #database-{fish_type}
    valid_fish = ["pike", "carp", "eel", "roach", "perch", "zander", "tench", "other"]

    fish_type = type.lower()
    if fish_type not in valid_fish:
        await interaction.response.send_message(f"Unknown fish type '{type}'. Use one of: {', '.join(valid_fish)}", ephemeral=True)
        return

    channel_name = f"database-{fish_type}"
    channel = discord.utils.get(interaction.guild.channels, name=channel_name)

    if channel is None:
        await interaction.response.send_message(f"The channel #{channel_name} does not exist on the server.", ephemeral=True)
        return

    # Save catch in database
    async with aiosqlite.connect(DATABASE) as db:
        await db.execute(
            "INSERT INTO fangster (user, fish_type, kg, cm, image_url) VALUES (?, ?, ?, ?, ?)",
            (str(interaction.user), fish_type, kg, cm, image.url)
        )
        await db.commit()

    # Update status
    await update_status()

    # Send message in the fish channel with info
    embed = discord.Embed(
        title=f"New catch: {type.capitalize()}",
        description=f"**Fisher:** {interaction.user.mention}\n**Weight:** {kg} kg\n**Length:** {cm} cm",
        color=discord.Color.blue()
    )
    embed.set_image(url=image.url)
    embed.set_footer(text=f"Registered by {interaction.user}")

    await channel.send(embed=embed)

    # Confirm to the user
    await interaction.response.send_message(f"The catch has been registered and sent to #{channel_name}!", ephemeral=True)

bot.run(os.getenv("BOT_TOKEN"))
