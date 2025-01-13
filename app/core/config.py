from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_title: str = "Справочник организаций"
    app_description: str = (
        f"REST API приложения для справочника Организаций, Зданий, "
        f"Деятельности"
    )
    api_key: str

    class Config:
        extra = "ignore"
        env_file = ".env"


settings = Settings()
