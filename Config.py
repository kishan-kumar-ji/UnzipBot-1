import os


class Config:
    API_ID = int(os.environ.get("API_ID", 25252648))  # Change 12345 to your API_ID
    API_HASH = os.environ.get("API_HASH", '17a1e3c7f59dd46196f0570f9df34955')  # Change None to your API_HASH
    BOT_TOKEN = os.environ.get("BOT_TOKEN", '7199477809:AAHP3l7vMe_U2LiwQNc657mzqLo4f5re-f0')  # Change None to your BOT_TOKEN
    OWNER_ID = int(os.environ.get("OWNER_ID",'6986912824'))  # Change 0 to your OWNER_ID
    OWNER_NAME = os.environ.get("OWNER_NAME", 'alien')  # Change None to your OWNER_NAME

    # For Local Deploys edit above 5 lines.
    # Put your API_ID and OWNER_ID (without comma) and API_HASH,BOT_TOKEN n OWNER_NAME (with commas) below.
