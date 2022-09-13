from app.core.config import settings
from sqlalchemy_utils import create_database, database_exists


def init_db() -> None:

    if not database_exists(settings.SQLALCHEMY_DATABASE_URI):
        create_database(settings.SQLALCHEMY_DATABASE_URI)


if __name__ == "__main__":
    init_db()
