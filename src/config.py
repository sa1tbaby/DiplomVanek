from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_user: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_ECHO: bool

    @property
    def get_url_asyncpg(self):
        return (f'postgresql+asyncpg://'
                f'{self.DB_user}:'
                f'{self.DB_PASS}@'
                f'{self.DB_HOST}:'
                f'{self.DB_PORT}/'
                f'{self.DB_NAME}')

    @property
    def get_url_psycopg(self):
        return (f'postgresql+psycopg2://'
                f'{self.DB_user}:'
                f'{self.DB_PASS}@'
                f'{self.DB_HOST}:'
                f'{self.DB_PORT}/'
                f'{self.DB_NAME}')

    model_config = SettingsConfigDict(env_file='.env')


class LogSettings(BaseSettings):

    FILE_NAME: str = 'logs/log.txt'
    FILE_MODE: str = 'w'
    LOG_LEVEL: int = 10
    LOG_FORMAT: str = "%(asctime)s %(levelname)s :- %(message)s"



