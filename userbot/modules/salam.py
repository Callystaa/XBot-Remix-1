from time import sleep
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Hallo Semua Saya {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("`Assalamualaikum.....`")
# Owner @wahyutry._


@register(outgoing=True, pattern='^p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Hallo Semua Saya {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("`Assalamualaikum.....`")
# Owner @wahyutry._


@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Waallaikum.....`")
    sleep(1)
    await typew.edit("`Waallaikumsalam......`")
# Owner @wahyutry._


@register(outgoing=True, pattern='^l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Waallaikum.....`")
    sleep(1)
    await typew.edit("`Waallaikumsalam.....`")
# Owner @wahyutry._


CMD_HELP.update({
    "salam":
    "`P`\
\nUsage: Untuk Salam.\
\n\n`L`\
\nUsage: Untuk Jawab Salam."
})
