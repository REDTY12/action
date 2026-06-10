import requests
import os

GITHUB_USERNAME = "REDTY12"
DISCORD_APP_ID = "1514357681240932474"  
DISCORD_USER_ID = "992332343115268146"
BOT_TOKEN = os.environ["BOT_TOKEN"]  

# === 1. Берём кол-во репозиториев с GitHub ===
gh_response = requests.get(f"https://api.github.com/users/{GITHUB_USERNAME}")
repos_count = gh_response.json()["public_repos"]

payload = {
    "username": "ТвойНик",
    "data": {
        "dynamic": [
            { "type": 1, "name": "nickname", "value": "ТвойНик" },
            { "type": 1, "name": "title", "value": "Junior Developer" },
            { "type": 2, "name": "age", "value": 14 },
            { "type": 2, "name": "repos", "value": repos_count },
            { "type": 1, "name": "website", "value": "твой-сайт.com" },
            { "type": 1, "name": "language", "value": "Python" }
        ]
    }
}

url = f"https://discord.com/api/v9/applications/{DISCORD_APP_ID}/users/{DISCORD_USER_ID}/identities/0/profile"
headers = {
    "Authorization": f"Bot {BOT_TOKEN}",
    "Content-Type": "application/json",
    "User-Agent": "DiscordBot (https://github.com/discord/discord-api-docs, 1.0.0)"
}

response = requests.patch(url, json=payload, headers=headers)
print(f"Статус: {response.status_code}")
print(response.text)
