import os
from pytz import timezone


class Constant:

    LOG_PATH = ''
    PY_SCRIPT_PATH = ''

    ENABLE_LOG = False
    ENABLE_LOG_BY_SECTION = False

    APPLICATION_TIMEZONE = ''

    LOG_SECTION_TEMPERATURE = 'temperature'

    AWS_URL = 'http://52.32.114.119:8128/sensor'

    SOURCE_URL = 'https://spreadsheets.google.com/feeds'
    SHEET_NAME = 'Livolt-Temperature-Readings'

    CLIENT_KEY_FILE = 'client_secret.json'
    DATE_TIME_FORMAT = 'Y-m-d H:i:s'

    LIVE = True

    def __init__(self):
        self.PY_SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__)) + '/'
        self.LOG_PATH = self.PY_SCRIPT_PATH + 'log/'
        self.APPLICATION_TIMEZONE = timezone('UTC')

        if self.PY_SCRIPT_PATH == "/home/web/Python/iot/livolt/":
            self.LIVE = False
