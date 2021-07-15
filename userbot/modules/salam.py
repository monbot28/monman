from platform import uname

from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.p(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Assalamualaikum Dulu Dari Mon**")


@register(outgoing=True, pattern=r"^\.pe(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Punten, bismillah ada pap nyasar**")


@register(outgoing=True, pattern="^.P(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Punten, bismillah nyantol cewe satu...**")


@register(outgoing=True, pattern=r"^\.l(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Wa'alaikumsalam dari mon**")


@register(outgoing=True, pattern="^.m(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Punten, bismillah dapet sleepcall**")


@register(outgoing=True, pattern="^.cw(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Punten, bismillah nyantol cewe satu**")

@register(outgoing=True, pattern="^.ba(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Punten, bismillah admin**")


@register(outgoing=True, pattern="^.bad(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Bismillah admin**")


@register(outgoing=True, pattern="^.bd(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Bismillah aja dulu**")


@register(outgoing=True, pattern="^.bt(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Punten, bismillah dapet pap tangtop**")


@register(outgoing=True, pattern="^.po(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Bismillah dapet pap tangtop sekalian orangnya**")


@register(outgoing=True, pattern="^.pt(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Bismillah dapet pap tangtop**")


@register(outgoing=True, pattern="^.bs(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Bismillah dapet sleepcall**")


@register(outgoing=True, pattern="^.tn(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Bismillah dapet pap tangtop nyasar**")


CMD_HELP.update(
    {
        "salam": "**Plugin : **`salam`\
        \n\n  •  **Syntax :** `.p`\
        \n  •  **Function : **Assalamualaikum Dulu Biar Sopan..\
        \n\n  •  **Syntax :** `.pe`\
        \n  •  **Function : **salam Kenal dan salam\
        \n\n  •  **Syntax :** `.l`\
        \n  •  **Function : **Untuk Menjawab salam\
        \n\n  •  **Syntax :** `.ass`\
        \n  •  **Function : **Salam Bahas arab\
        \n\n  •  **Syntax :** `.semangat`\
        \n  •  **Function : **Memberikan Semangat.\
        \n\n  •  **Syntax :** `.ywc`\
        \n  •  **Function : **nMenampilkan Sama sama\
        \n\n  •  **Syntax :** `.sayang`\
        \n  •  **Function : **Kata I Love You.\
        \n\n  •  **Syntax :** `.k`\
        \n  •  **Function : **LU SEMUA NGENTOT 🔥\
        \n\n  •  **Syntax :** `.j`\
        \n  •  **Function : **NIMBRUNG GOBLOKK!!!🔥\
    "
    }
)
