import sys
from importlib.metadata import version
#
from pymongo import MongoClient
#
from logging_utility import LoggingUtility as lu
from program_settings import ProgramSettings

logger = lu.start_logging()


def get_python_version() -> str:
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"


def get_package_version(package_name: str) -> str:
    return version(package_name)


def get_connection_string() -> str:
    """
    Get a connection string for MongoDB using the key/values stored in the .env file.
    :return: a string containing the connection string.
    """
    template: str = ProgramSettings.get_setting('MONGODB_CONNECTION_TEMPLATE')
    uid: str = ProgramSettings.get_setting('MONGODB_UID')
    pwd: str = ProgramSettings.get_setting('MONGODB_PWD')

    conn_string = f'mongodb+srv://{uid}:{pwd}@{template}'

    msg = f'{conn_string=}'
    logger.info(msg)
    logger.debug(msg)

    return conn_string


def get_mongodb_client() -> MongoClient:
    """
    Get a MongoClient instance using the connection string
    :return: MongoClient
    """
    return MongoClient(get_connection_string())


def display_available_databases() -> None:
    """
    Display available databases.
    """
    # Connect to MongoDB
    client: MongoClient = get_mongodb_client()

    databases: list[str] = client.list_database_names()
    msg = "Available Databases:"
    lu.log_info_and_debug(msg)
    for database in databases:
        msg = f'\t{database}'
        lu.log_info_and_debug(msg)


def main():
    display_available_databases()


if __name__ == '__main__':
    msg = f'Python version: {get_python_version()}'
    logger.info(msg)
    logger.debug(msg)

    msg = f'PyMongo version: {get_package_version("PyMongo")}'
    logger.info(msg)
    logger.debug(msg)

    main()
