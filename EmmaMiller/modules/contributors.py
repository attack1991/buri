import github  # pyGithub
from pyrogram import filters

from EmmaMiller.services.pyrogram import pbot as client

  
    
@client.on_message(filters.command("contributors") & ~filters.edited)
async def give_cobtribs(c, m):
    g = github.Github()
    co = ""
    n = 0
    repo = g.get_repo("BotMasterOfficial/EmmaMillerBot")
    for i in repo.get_contributors():
        n += 1
        co += f"{n}. [{i.login}](https://github.com/{i.login})\n"
    t = f"**[Emma Miller](https://t.me/EmmaMillerBot) Contributors**\n\n{co}\n\n\nA Powerful BOT to Make Your Groups Secured and Organized ! ✨"
    await m.reply(t, disable_web_page_preview=True)
    
__help__ = """
@BotMasterOfficial
Contributor
 ❍ /contributors : contributors using this bot  
"""
__mod_name__ = "☠𝐂𝐨𝐧𝐭𝐫𝐢𝐛𝐮𝐭𝐨𝐫☠"
