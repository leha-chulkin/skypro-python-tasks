import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    def __init__(self):

        self.myuser = os.getenv("myuser")
        self.mypassword = os.getenv("mypassword")
        self.localhost = os.getenv("localhost")
        self.mydatabase = os.getenv("mydatabase")

    def db_connection_string(self):
        return f"postgresql://{self.myuser}:{self.mypassword}@{self.localhost}:5432/{self.mydatabase}"


config = Config()
