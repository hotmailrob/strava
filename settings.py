from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    CLIENT_ID: str = Field(default=...)
    CLIENT_SECRET: str = Field(default=...)
    REFRESH_TOKEN: str = Field(default=...)
    CODE: str = Field(default=...)

