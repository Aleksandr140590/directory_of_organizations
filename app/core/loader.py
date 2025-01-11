from dotenv import load_dotenv
from os import getenv


load_dotenv()

DB_USER = getenv("POSTGRES_USER")  # имя пользователя БД
DB_PASSWORD = getenv("POSTGRES_PASSWORD")  # пароль пользователя БД
DB_NAME = getenv("POSTGRES_NAME")  # название БД
DB_HOST = getenv("POSTGRES_HOST")  # хост БД
DB_PORT = getenv("POSTGRES_PORT")  # порт БД

# ссылка для доступа к БД
DATABASE_URL = f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
