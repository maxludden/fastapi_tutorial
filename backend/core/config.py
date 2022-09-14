import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "Job Board"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER: str = str(os.getenv("POSTGRES_USER", "maxludden"))
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "1Industries")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = str(
        os.getenv("POSTGRES_PORT", 5432)
    )  # default postgres port is 5432
    POSTGRES_DB: str = str(os.getenv("POSTGRES_DB", "job_db"))
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    SECRET_KEY :str = os.getenv("SECRET_KEY", str(os.environ.get("SECRET_KEY")))   #new
    ALGORITHM = "HS256"                         #new
    ACCESS_TOKEN_EXPIRE_MINUTES = 30  #in mins  #new
settings = Settings()
