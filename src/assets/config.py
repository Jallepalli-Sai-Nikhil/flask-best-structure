from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parents[2]
TEMPLATES_DIR = BASE_DIR / "src"/"templates"


class Config:
    SECRET_KEY=os.getenv("SECRET_KEY", "default")
    FLASK_ENV=os.getenv("FLASK_ENV", "development")
    TEMPLATE_FOLDER = str(TEMPLATES_DIR)