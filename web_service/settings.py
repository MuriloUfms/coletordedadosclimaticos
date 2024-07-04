from pydantic_settings import BaseSettings, SettingsConfigDict


class Base(BaseSettings):
    model_config = SettingsConfigDict(
        extra='allow', env_file='.env', env_file_encoding='utf-8'
    )

    BACKEND_URL: str = 'http://localhost'


Settings = Base()
