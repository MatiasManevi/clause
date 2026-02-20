from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Config(BaseSettings):
    storage_provider: str = "local"
    s3_bucket: str
    s3_region: str = "us-east-1"
    db_name: str
    db_host: str = "localhost"
    db_port: int = 5432
    db_user: str
    db_password: str

    @property
    def database_url(self) -> str:
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

config = Config()
