#!/usr/bin/python
import logging
from const import Constant


class LogMessage:

    const = ''

    def __init__(self):
        self.const = Constant()

    def log(self, data):
        if self.const.ENABLE_LOG:
            logFileName = self.const.LOG_PATH + 'message.log'
            logging.basicConfig(filename=logFileName,level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
            logging.info(data)
        else:
            print data

    def logBySection(self, data, sectionName):
        if self.const.ENABLE_LOG_BY_SECTION:
            logFileName = self.const.LOG_PATH + str(sectionName) + '.log'
            logging.basicConfig(filename=logFileName,level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
            logging.info(data)
        else:
            print data

