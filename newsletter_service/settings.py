from pydantic_settings import BaseSettings, SettingsConfigDict


class Base(BaseSettings):
    model_config = SettingsConfigDict(
        extra='allow', env_file='.env', env_file_encoding='utf-8'
    )

    DATABASE_URI: str = 'sqlite:///:memory:'
    API_COLECTOR_URL: str = 'http://localhost:8001/api/v1'
    NEWSLETTER_INTERVAL_SECONDS: int = 60 * 30  # 30 minutes
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_SERVER: str
    MAIL_PORT: int


Settings = Base()
