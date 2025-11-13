from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    django_debug: bool
    django_secret_key: str

    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
