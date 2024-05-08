from motor import motor_asyncio
import os
import sys
from pymongo.server_api import ServerApi


class ConnectDB:
    def __init__(self):
        self.DB_URL = os.getenv("MONGO_DB_URI")
        self.DB_NAME = os.getenv("DB_NAME")
        self.client = motor_asyncio.AsyncIOMotorClient(self.DB_URL, server_api=ServerApi("1.0"))

    def get_db(self):
        return self.client[self.DB_NAME]

    async def ping(self):
        try:
            await self.client.admin.command("ping")
        except Exception as e:
            sys.exit(1)
        return True

    async def close(self):
        self.client.close()


connect_db = ConnectDB()
