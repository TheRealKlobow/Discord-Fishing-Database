Fish Catch Registration Discord Bot
This Discord bot lets users easily register their fishing catches directly in your server using slash commands. It stores the data in a SQLite database and posts detailed catch info in dedicated fish-type channels.

🔧 How to use the system
Use the slash command:

/catch

You will be asked to provide:

Type: The type of fish (see valid types below)

Kg: The weight of the catch in kilograms

Cm: The length of the catch in centimeters

Image: You must attach a picture of the catch!

🎣 Valid fish types
Perch

Pike

Carp

Zander

Roach

Tench

Eel

Other

📝 Important
Write the fish type exactly as listed above — otherwise, the command will not work!

Features
Saves catch data (user, fish type, weight, length, image) in a SQLite database

Posts a formatted embed message with catch details and image in the appropriate fish channel (e.g. #database-pike)

Updates bot status to show total number of registered catches

Provides immediate confirmation to the user

Requirements
Python 3.8+

discord.py library

aiosqlite for database handling

A Discord server with channels named like database-pike, database-carp, etc.

Setup
Clone the repository

Install dependencies:
pip install discord.py aiosqlite

Create the appropriate fish channels on your Discord server (e.g., database-pike)

Set your bot token as an environment variable BOT_TOKEN

Run the bot script

🚀 Deploying with Railway
You can deploy this bot easily using Railway:

Create a new project on Railway and link your GitHub repository.

Add your environment variable BOT_TOKEN in Railway’s dashboard under the project settings.

Railway will automatically install dependencies based on your requirements.txt or via pip install commands.

Railway will run your bot script and keep it online 24/7.

Railway provides a hassle-free way to host your Discord bot without managing your own server.

Optional: Create a requirements.txt file
To make deployment easier, create a requirements.txt file in your project folder with these lines:

discord.py
aiosqlite

Feel free to customize fish types or improve functionality as needed!

If you want help with Docker or advanced deployment setups, just ask!
