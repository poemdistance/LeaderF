
class Logger(object):
    def __init__(self):
        self.logpath = '/var/log/leaderf.log'
        self.log = open(self.logpath, 'a+', encoding='utf8')

    def write(self, *arg, **kwargs):
        self.log.write(*arg, **kwargs)
        self.log.flush()

    def __del__(self):
        self.log.close()

logger = Logger()
