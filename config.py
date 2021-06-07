from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "1BVtsOMMBu5gD0LPZKslrpG4y8tvak847jik0BA5a5Uvl0zCoS8IV0-16opM2xP6C3z3nbIMo6N9Zgu36iMariPLXmsT9SO7BCHA2nB7a5diYVPoCbdZ6cwHC3Nh443DOmZxHo5_jPMjdZOfVHJNp3-5zauK3t00Ax8t95_bLjl_mci7J37FsETXKNzybWU1-5zSVLRPi8d1umy-kVCi1PNL8giO4bYY8MSjOF-O5ZpPDxbvYS22MrPMOa-OhgMHAk3pnMqQF9JCyYwLiuBtFJluKxImCKkhEHK_yQ7iRFZUfdaetOpsQ2wShlJjUvxa-QRQmYA8qVHyu90ihnV0a-wpLv2hasjc=")
BOT_TOKEN = getenv("BOT_TOKEN", "1838517088:AAHS3lo_oWD3Sn--27Za2dhaNbHyq-c-pl0")
BOT_NAME = getenv("BOT_NAME", "cracxrobo")
admins = {}
API_ID = int(getenv("API_ID", "3898418"))
API_HASH = getenv("API_HASH", "5a82313211da04d63297bd4de436228c")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "200"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1607847356").split()))
