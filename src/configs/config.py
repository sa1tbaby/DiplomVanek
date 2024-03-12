from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_user: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    @property
    def get_url_asyncpg(self):
        return (f'postgresql+asyncpg://'
                f'{self._config.username}:'
                f'{self._config.password}@'
                f'{self._config.host}:'
                f'{self._config.port}/'
                f'{self._config.database}')

    @property
    def get_url_psycopg(self):
        return (f'postgresql+psycopg2://'
                f'{self._config.username}:'
                f'{self._config.password}@'
                f'{self._config.host}:'
                f'{self._config.port}/'
                f'{self._config.database}')

    model_config = SettingsConfigDict(env_file='.env')
