from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    ASTEROIDS_BUCKET = os.getenv("ASTEROIDS_BUCKET")
    OUTPUT_PATH = os.getenv("OUTPUT_PATH")

settings = Settings()