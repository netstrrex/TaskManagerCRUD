from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from config import settings
from infrastructure.database.postgres import PostgresDatabase
from infrastructure.logger.root import configure_root_logging
from infrastructure.server.gunicorn import GunicornApplication


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    database = PostgresDatabase(settings.postgres.dsn)
    await database.create_pool()
    await database.create_schema_if_not_exist()
    app.state.database = database
    yield
    await database.close_pool()


configure_root_logging()
fastapi_app = FastAPI(lifespan=lifespan)

if __name__ == "__main__":
    GunicornApplication(fastapi_app).run()
