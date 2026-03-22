import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME = "ESHA-Gatekeeper-Dispatcher"
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    PORT = int(os.getenv("PORT", 8080))
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

    # Optional for current phase
    API_KEY = os.getenv("API_KEY")
    DATABASE_URL = os.getenv("DATABASE_URL")

    def validate_required(self) -> None:
        if not self.API_KEY:
            raise ValueError("CRITICAL: 'API_KEY' is missing but required for this feature.")


settings = Settings()
