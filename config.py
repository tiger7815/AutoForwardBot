from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "3506d8474ad1f4f5e79b7c52a5c3e88d")
      API_ID = int(getenv("API_ID", "22609670"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "6502851708:AAEqGci9nnyLMHaYk6SxkvRgtp1DO_rBZa0")
      session_strings = getenv("session_strings","")
      session_string = getenv("session_string", "")
      LOG_CHANNEL = getenv("BIN_CHANNEL", "")
      PELAI_ID = getenv("PELAI_ID", "")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002139132511:-1002022426966").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
