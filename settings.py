"""Store all centralized settings here."""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Settings base class."""

    yolov8_model_path: str
    height: int = 1080
    width: int = 1920

    class Config:
        """Configuration for fetching the settings."""

        env_file = ".env"
        env_file_encoding = "utf-8"
