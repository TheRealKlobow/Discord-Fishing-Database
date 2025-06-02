# 🎣 Fish Catch Registration Discord Bot

![Made by](https://img.shields.io/badge/Made%20by-Klobow-purple)
![Status](https://img.shields.io/badge/Status-BETA-yellow)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A simple and clean Discord bot for registering fish catches during competitions or just for fun 🎉  
Built for fishing communities who want structure and automation in their Discord server.

---

## 🔧 How to Use

Use the slash command:

```
/catch
```

You will be asked to provide:

- 🎣 **Type**: The type of fish (must match the valid list below)
- ⚖️ **Kg**: Weight of the fish in kilograms
- 📏 **Cm**: Length of the fish in centimeters
- 🖼️ **Image**: Upload a photo of the catch

> ⚠️ **Important:** Type must match exactly as listed below – otherwise, the command will not work!

---

## 🐟 Valid Fish Types

- Perch  
- Pike  
- Carp  
- Zander  
- Roach  
- Tench  
- Eel  
- Other

---

## 💡 Features

✅ Stores catch data in a local **SQLite** database  
✅ Posts a **formatted embed** with catch details and image to the correct fish-type channel (e.g. `#database-pike`)  
✅ Updates bot status with **total registered catches**  
✅ Gives users an instant **confirmation message**

---

## 🧰 Requirements

- Python 3.8+
- `discord.py`
- `aiosqlite`
- A Discord server with the following channels:
  - `#database-perch`
  - `#database-pike`
  - `#database-carp`
  - `#database-zander`
  - etc.

---

## 🚀 Setup

```bash
# Clone the repository
git clone https://github.com/TheRealklobow/Discord-Fishing-Database.git
cd Discord-Fishing-Database

# Install dependencies
pip install discord.py aiosqlite

# Set your bot token as an environment variable
export BOT_TOKEN=your_discord_bot_token

# Run the bot
python bot.py
```

---

## ☁️ Deploying with Railway

1. Go to [Railway](https://railway.app) and create a new project  
2. Link your GitHub repository  
3. Add an environment variable `BOT_TOKEN`  
4. Railway auto-installs dependencies and keeps your bot online 24/7

**Optional:** Add a `requirements.txt`:

```
discord.py
aiosqlite
```

---

## 📫 Feedback

Have ideas or feedback? DM me on Discord: `Klobow`  
Let’s make **fishing in Discord** easy and fun for everyone!

---
