#!/usr/bin/python
import gspread
import datetime
import time
import serial
import serial.tools.list_ports

from oauth2client.service_account import ServiceAccountCredentials
from const import Constant
from logmessages import LogMessage


class ReadTemperature:

    const = ''
    logMessage = ''

    def __init__(self):
        self.const = Constant()
        self.logMessage = LogMessage()

    def run(self):
        try:
            while True:
                readings = self.readDataFromUSB()
                # readings = ['  ', '', 'RH=31.4  ', '', 'T=+23.3  ', '', 'RH=31.4  ', '', 'T=-23.4  ']
                if len(readings) > 0:
                    data = self.processData(readings)
                    self.sendDataToSheet(data)
                    self.logMessage.logBySection('Data saved : ' + str(datetime.datetime.now(self.const.APPLICATION_TIMEZONE)),
                                                 self.const.LOG_SECTION_TEMPERATURE)
                time.sleep(10)
        except Exception, e:
            self.logMessage.logBySection('Error Message : ' + str(e), self.const.LOG_SECTION_TEMPERATURE)
            self.run()
            pass

    def processData(self, log):
        rows = []
        v1 = ''
        v2 = ''
        try:
            for data in log:
                reading = data.strip()
                if len(reading) > 0:
                    final = reading.split('=')
                    if len(final) > 0:
                        if final[0] == 'RH':
                            v1 = final[1]
                        elif final[0] == 'T':
                            v2 = final[1]
                        if len(v1) > 0 and len(v2) > 0:
                            rows.append([time.time(), v1, v2])
                            v1 = ''
                            v2 = ''
        except Exception, e:
            self.logMessage.logBySection('Error Message : ' + str(e), self.const.LOG_SECTION_TEMPERATURE)
            pass
        return rows

    def readDataFromUSB(self):
        data = []
        try:
            serialPort = serial.Serial('/dev/ttyUSB0', baudrate=2400, timeout=10)
            temperatureReading = serialPort.read(1024)
            if len(temperatureReading) > 0:
                data = temperatureReading.splitlines()
        except Exception, e:
            self.logMessage.logBySection('Error Message : ' + str(e), self.const.LOG_SECTION_TEMPERATURE)
            pass
        return data

    def sendDataToSheet(self, data):
        try:
            scope = [self.const.SOURCE_URL]
            creds = ServiceAccountCredentials.from_json_keyfile_name(self.const.CLIENT_KEY_FILE, scope)
            client = gspread.authorize(creds)
            sheet = client.open(self.const.SHEET_NAME).sheet1
            for reading in data:
                sheet.append_row(reading)
        except Exception, e:
            self.logMessage.logBySection('Error Message : ' + str(e), self.const.LOG_SECTION_TEMPERATURE)
            pass

obReadRemp = ReadTemperature()
obReadRemp.run()
