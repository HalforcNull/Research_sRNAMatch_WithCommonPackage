import datetime
import psutil

class Log:
    logfile = None
    def __init__(self, logFileName, loger, mode = 'a'):
        if logFileName is None or logFileName == '':
            self.logfile = open('log.txt', mode)
        else:
            self.logfile = open(logFileName, mode)
        
        self.logfile.write('===============  ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        self.logfile.write('===============  New Log Start by ' + loger)
        self.logfile.write('===============  log mode: ' + mode)
        return 
    
    def write(self, message):
        log = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
        log += ': ' + message
        self.logfile.write(log)
        return
    
    def reportMemoryUsage(self):
        a = psutil.virtual_memory()
        log = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
        log += ': ' + str(a.percent) + ' of ' + str(a.total/1024/1024) +'MB memory is used'
        self.logfile.write(log)
        return
    
    
        
            