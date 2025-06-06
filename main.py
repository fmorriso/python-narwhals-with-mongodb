import sys
from importlib.metadata import version


from logging_utility import LoggingUtility
from program_settings import ProgramSettings

logger = LoggingUtility.start_logging()

def get_python_version() -> str:
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"


def get_package_version(package_name: str) -> str:
    return version(package_name)

def main():
    pass

if __name__ == '__main__':
    msg = f'Python version: {get_python_version()}'
    logger.info(msg)
    logger.debug(msg)

    msg = f'PyMongo version: {get_package_version("PyMongo")}'
    logger.info(msg)
    logger.debug(msg)

    main()

