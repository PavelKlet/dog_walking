from pathlib import Path
from pydantic_settings import BaseSettings


BASE_DIRECTORY = Path(__file__).absolute().parent.parent


class Settings(BaseSettings):
    db_user: str
    db_pass: str
    db_host: str
    db_port: int
    db_name: str

    @property
    def postgresql_url(self) -> str:

        return (
            f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@"
            f"{self.db_host}:{self.db_port}/{self.db_name}"
        )

    class Config:
        env_file = f"{BASE_DIRECTORY}/.env"


settings = Settings()
