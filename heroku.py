import asyncio
import math
import os
import heroku3
import requests
import urllib3
import sys
from os import execl
from time import sleep

from . import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY


@bot.on(kryo_cmd(pattern="restart$"))
@bot.on(sudo_cmd(pattern="restart$", allow_sudo=True))
async def re(kryo):
    if kryo.fwd_from:
        return
    event = await eor(kryo, "Restarting Dynos ...")
    await event.edit("✅ **Restarted Dynos** \n**Type** `.ping` **after 1 minute to check if I am working!**")
    await bot.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@bot.on(kryo_cmd(pattern="shutdown$"))
@bot.on(sudo_cmd(pattern="shutdown$", allow_sudo=True))
async def down(kryo):
    if kryo.fwd_from:
        return
    await kryo.edit("**[ ! ]** Turning off ₭ⱤɎ0.฿Ø₮ Dynos... Manually turn me on later ಠ_ಠ")
    if HEROKU_APP is not None:
        HEROKU_APP.process_formation()["userbot"].scale(0)
    else:
        sys.exit(0)


@bot.on(kryo_cmd(pattern="(set|get|del) var(?: |$)(.*)(?: |$)([\s\S]*)", outgoing=True))
@bot.on(sudo_cmd(pattern="(set|get|del) var(?: |$)(.*)(?: |$)([\s\S]*)", allow_sudo=True))
async def variable(kryo):
    if kryo.fwd_from:
        return
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        return await kryo.edit("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")
    exe = kryo.pattern_match.group(1)
    heroku_var = app.config()
    if exe == "get":
        await kryo.edit("Getting Variable Info...")
        await asyncio.sleep(1.5)
        try:
            variable = kryo.pattern_match.group(2).split()[0]
            if variable in heroku_var:
                return await kryo.edit(
                    "**Heroku Var** :" f"\n\n`{variable}` = `{heroku_var[variable]}`\n"
                )
            else:
                return await kryo.edit(
                    "**Heroku Var** :" f"\n\n__Error:__\n-> I doubt `{variable}` exists!"
                )
        except IndexError:
            configs = prettyjson(heroku_var.to_dict(), indent=2)
            with open("configs.json", "w") as fp:
                fp.write(configs)
            with open("configs.json", "r") as fp:
                result = fp.read()
                if len(result) >= 4096:
                    await kryo.client.send_file(
                        kryo.chat_id,
                        "configs.json",
                        reply_to=kryo.id,
                        caption="`Output too large, sending it as a file`",
                    )
                else:
                    await kryo.edit(
                        "**Heroku Var :**\n\n"
                        "================================"
                        f"\n```{result}```\n"
                        "================================"
                    )
            os.remove("configs.json")
            return
    elif exe == "set":
        await kryo.edit("Setting Heroku Variable...")
        variable = kryo.pattern_match.group(2)
        if not variable:
            return await kryo.edit(f"`{hl}set var <Var Name> <Value>`")
        value = kryo.pattern_match.group(3)
        if not value:
            variable = variable.split()[0]
            try:
                value = kryo.pattern_match.group(2).split()[1]
            except IndexError:
                return await kryo.edit(f"`{hl}set var <Var Name> <Value>`")
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await kryo.edit(
                f"`{variable}` **successfully changed to**  ->  `{value}`"
            )
        else:
            await kryo.edit(
                f"`{variable}` **successfully added with value**  ->  `{value}`"
            )
        heroku_var[variable] = value
    elif exe == "del":
        await kryo.edit("Getting info to delete Variable")
        try:
            variable = kryo.pattern_match.group(2).split()[0]
        except IndexError:
            return await kryo.edit("`Please specify ConfigVars you want to delete`")
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await kryo.edit(f"**Successfully Deleted** \n`{variable}")
            del heroku_var[variable]
        else:
            return await kryo.edit(f"`{variable}`  **does not exists**")


@bot.on(kryo_cmd(pattern="usage(?: |$)", outgoing=True))
@bot.on(sudo_cmd(pattern="usage(?: |$)", allow_sudo=True))
async def dyno_usage(kryo):
    if kryo.fwd_from:
        return
    await edit_or_reply(kryo, "`Processing...`")
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    user_id = Heroku.account().id
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {Config.HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + user_id + "/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await kryo.edit(
            "`Error: something bad happened`\n\n" f">.`{r.reason}`\n"
        )
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]

    """ - Used - """
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)

    """ - Current - """
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)

    await asyncio.sleep(1.5)

    return await kryo.edit(
        "⚡ **Dyno Usage** ⚡:\n\n"
        f" ➠ __Dyno usage for__ • **{Config.HEROKU_APP_NAME}** • :\n"
        f"     ★  `{AppHours}`**h**  `{AppMinutes}`**m**  "
        f"**|**  `{AppPercentage}`**%**"
        "\n\n"
        " ➠ __Dyno hours remaining this month__ :\n"
        f"     ★  `{hours}`**h**  `{minutes}`**m**  "
        f"**|**  `{percentage}`**%**"
        f"\n\n**Owner :** {kryo_mention}"
    )


@bot.on(kryo_cmd(pattern="logs$", outgoing=True))
@bot.on(sudo_cmd(pattern="logs$", allow_sudo=True))
async def erlog(kryo):
    if kryo.fwd_from:
        return
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        app = Heroku.app(HEROKU_APP_NAME)
        thumb = kryo_logo
    except:
        return await kryo.reply(
           f"Make Sure Your Heroku AppName & API Key are filled correct. Visit {kryo_grp} for help.", link_preview=False
        )
    kryo_data = app.get_log()
    kryo_key = (
        requests.post("https://nekobin.com/api/documents", json={"content": kryo_data})
        .json()
        .get("result")
        .get("key")
    )
    kryo_url = f"⚡ Also Pasted to [NekoBin](https://nekobin.com/{kryo_key}) && [RAW PAGE](https://nekobin.com/raw/{kryo_key}) ⚡"
    await kryo.edit("Getting Logs....")
    with open("logs.txt", "w") as log:
        log.write(app.get_log())
    await kryo.edit("Uploading Logs...")
    await kryo.client.send_file(
        kryo.chat_id,
        "logs.txt",
        reply_to=kryo.id,
        thumb=thumb,
        caption=kryo_url,
    )
    await asyncio.sleep(2)
    await kryo.delete()
    return os.remove("logs.txt")


def prettyjson(obj, indent=2, maxlinelength=80):
    """Renders JSON content with indentation and line splits/concatenations to fit maxlinelength.
    Only dicts, lists and basic types are supported"""

    items, _ = getsubitems(
        obj,
        itemkey="",
        islast=True,
        maxlinelength=maxlinelength - indent,
        indent=indent,
    )
    return indentitems(items, indent, level=0)


CmdHelp("power").add_command(
  "restart", None, "Restarts your userbot. Redtarting Bot may result in better functioning of bot when its laggy"
).add_command(
  "shutdown", None, "Turns off Dynos of Userbot. Userbot will stop working unless you manually turn it on from heroku"
).add_info(
  "Power Switch For Bot"
).add_warning(
  "✅ Harmless Module"
).add()

CmdHelp("heroku").add_command(
  "usage", None, "Check your heroku dyno hours status."
).add_command(
  "set var", "<Var Name> <value>", "Add new variable or update existing value/variable\nAfter setting a variable bot will restart so stay calm for 1 minute."
).add_command(
  "get var", "<Var Name", "Gets the variable and its value (if any) from heroku."
).add_command(
  "del var", "<Var Name", "Deletes the variable from heroku. Bot will restart after deleting the variable. So be calm for a minute 😃"
).add_command(
  "logs", None, "Gets the app log of 100 lines of your bot directly from heroku."
).add_info(
  "Heroku Stuffs"
).add_warning(
  "✅ Harmless Module"
).add()