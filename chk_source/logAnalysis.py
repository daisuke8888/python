#! python3
# config: utf-8

from datetime import datetime
import os
import re
import scenarios
import shutil
import sys

class logAnalysis:
    def __init__(self):
        self.logDir = ''
        self.logFile = ''

    def getLogDir(self):
        return self.logDir

    def getLogFile(self):
        return self.logFile

    def getLogFilePath(self):
        return os.path.join(self.getLogDir(), self.getLogFile())

    def getLogResult(self):
        return os.path.join(self.getLogDir(), 'result.log')

    def setLogDir(self, scenario):
        d = datetime.today()
        dirTime = str(d.year) + str(d.month) + str(d.day)    + str(d.hour) \
                                             + str(d.minute) + str(d.second)
        self.logDir = os.path.join(scenario['scenarioName'], dirTime)

    def mkLogDir(self, logDir):
        if os.path.exists(logDir) is False:
            os.mkdir(logDir)
        elif os.path.isdir(logDir) is False:
            raise Exception('A file with the same name as the log directory '
                            'name already exists. \n-->{0}'.format(logDir))

    def mkLogDirName(self, scenario):
        self.mkLogDir(scenario['scenarioName'])

    def mkLogDirTime(self):
        self.mkLogDir(self.getLogDir())

    def setLogFile(self, scenario):
        self.logFile = os.path.basename(scenario['scenarioLog'])

    def scenarioPreStart(self, scenario):
        self.setLogDir(scenario)
        self.mkLogDirName(scenario)
        self.mkLogDirTime()
        self.setLogFile(scenario)

    def collectLogFile(self, scenario):
        logPath = os.path.join(scenario['scenarioLog'])
        shutil.move(logPath, self.getLogDir())

    def createNewLogFile(self, scenario):
        with open(scenario['scenarioLog'], 'w') as f:
            pass

    def readLogFile(self):
        with open(self.getLogFilePath(), 'r') as f:
            return f.read()

    def writeResult(self, log, result):
        with open(self.getLogResult(), 'a') as f:
            f.write(result + ': ' + log + '\n')

    def writeResultOK(self, log):
        self.writeResult(log, 'OK')

    def writeResultNG(self, log):
        self.writeResult(log, 'NG')

    def logAnalysis(self, checkLog):
        regex = re.compile(r'.*' + checkLog + r'.*')
        mo = regex.search(self.readLogFile())
        if mo is None or mo.group() is None:
            self.writeResultNG(checkLog)
        else:
            self.writeResultOK(mo.group())

    def logAnalysisAll(self, scenario):
        for checkLog in scenario['checkLogs']:
            self.logAnalysis(checkLog)

    def runLogAnalysis(self):
        for scenario in scenarios.testall:
            try:
                self.scenarioPreStart(scenario)
                self.collectLogFile(scenario)
                self.createNewLogFile(scenario)
                self.logAnalysisAll(scenario)
            except Exception as err:
                print('ERROR: ' + str(err))
                sys.exit(1)

if __name__ == '__main__' :
    l = logAnalysis()
    l.runLogAnalysis()

