import time

class Timer(object):

    def __init__(self, verbose=False):
        self.verbose = verbose

    def startTime(self):
        self.start = time.time()
        return self

    def endTimer(self):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs  # millisecs
        res = round(self.msecs,3)
        print (res,"sec" )