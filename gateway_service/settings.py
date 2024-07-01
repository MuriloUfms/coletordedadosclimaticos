from pydantic_settings import BaseSettings, SettingsConfigDict


class Base(BaseSettings):
    model_config = SettingsConfigDict(
        extra='allow', env_file='.env', env_file_encoding='utf-8'
    )

    API_NEWSLETTER_URL: str = 'http://localhost:8002/api/v1'
    API_COLECTOR_URL: str = 'http://localhost:8001/api/v1'


Settings = Base()
