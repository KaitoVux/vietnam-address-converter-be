from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BACKEND_PORT: int = 8000
    FRONTEND_URL: str = "http://localhost:3000"
    PRODUCTION_FRONTEND_URL: str = "https://vietnam-address-converter-fe.pages.dev"
    ALLOWED_ORIGINS: str = "http://localhost:3000,https://vietnam-address-converter-fe.pages.dev,https://*.biubuimiunemxinhdep.io.vn"

    class Config:
        env_file = ".env"

settings = Settings()
