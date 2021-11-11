import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {1396584367}
SESSION_NAME = getenv("SESSION_NAME", "BQDA-c0sIDKgjR1Tgl8Ofgwu8vuHrGZ4L8TA6ZvRmmc3a3j8WQxpzjRAuX0ZDp0sZoYbTy3YJzh_0SmJ6Q47whRAVhHY_5CEwxJLksar09V5W5CxEFBoj56-jkCpXlSLfWgrk8QLGJJrJfIu2JtqOQciF20GYI6V_1Npvbsu66JqIBtx4dtOX6OejuMAstnDol5uYUJENqCLDbg6nRDv9Zp0cuQaHXwjZ3sDJVNCG88HOsmx6Px27Tr9E8xBQ0ZthaVITUZdsdTcTDKzHPiMGw-a3KU4Z0n7hhMIDbmMfKBE6RddUJflvn3fcW7P4pInCocod8DeWY189ghDBEpiIJubUz4vrwA")
BOT_TOKEN = getenv("BOT_TOKEN","2100256126:AAFRzq_X2qtUwoX2mJvSlxDYuMuX-UDUHCM")
BOT_NAME = getenv("BOT_NAME", "VK RADIO BOT")
API_ID = int(getenv("API_ID","16080598")
API_HASH = getenv("API_HASH","2137943281:AAFC64yw_AG0psSr5aUWAf61FHAuyhFZ0go")
OWNER_NAME = getenv("OWNER_NAME", "single4mingle")
ALIVE_NAME = getenv("ALIVE_NAME", "VK RADIO BOT")
BOT_USERNAME = getenv("BOT_USERNAME", "VK_RADIO_BOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "vknetworkmob")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "https://t.me/joinchat/X9LMWhAfCAQyMjI1")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "tamil_movies_series1")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
