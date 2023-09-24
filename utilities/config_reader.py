import configparser
import os

ROOT_DIR = os.path.abspath('./..')
universal_path = os.path.join(ROOT_DIR, 'configurations', 'app_config.ini')
print(universal_path)

config = configparser.RawConfigParser()
config.read(universal_path)


class ReadConfig:
    @staticmethod
    def get_app_base_url():
        return config.get('app_data', 'base_url')

    @staticmethod
    def get_browser_id():
        return config.get('browser_data', 'browser_id')
