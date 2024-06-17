from pydantic_settings import BaseSettings, SettingsConfigDict


class Base(BaseSettings):
    model_config = SettingsConfigDict(
        extra='allow', env_file='.env', env_file_encoding='utf-8'
    )

    DATABASE_URI: str = 'sqlite:///:memory:'
    OPEN_WEATHER_API_KEY: str = None
    OPEN_WEATHER_URL: str = 'https://api.openweathermap.org/data/2.5/weather'


Settings = Base()
