import logging
import os
import time
import datetime

from numpy import true_divide

class SimpleFeature():

    def __init__(self, featurename, numberattrib, logger=None):
        '''
            logger - caller supplied logging, if not supplied local one will be created
        '''
        if logger != None:
            self.log = logger
        else:
            self.log, self.apppath = self.setup_logger()
        self.name = featurename
        self.attribute = numberattrib 


    def setup_logger(self):
        '''Constructor for vr_logging'''
        scriptname = os.path.splitext(os.path.basename(__file__))[0]
        appPath = os.path.dirname(os.path.realpath(__file__))
        logpath = os.path.join(appPath, 'logs')
        if not os.path.exists(logpath):
            os.mkdir(logpath)
        today = datetime.datetime.now().strftime('%d%m%y')
        logfile = os.path.join(logpath, scriptname + '_' + today + '.log')
        if logfile is not None:
            logging.basicConfig(filename=logfile, format='%(asctime)s %(funcName)s - %(message)s', level=logging.DEBUG, datefmt='%d/%m/%Y %H:%M:%S -')
        else:
            logging.basicConfig(format='%(asctime)s - %(funcName)s %(message)s', level=logging.DEBUG, datefmt='%m/%d/%Y %H:%M:%S -')
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        logging.getLogger('').addHandler(console)
        return logging, appPath

    def __str__(self) -> str:
        return f"{self.name} - {self.attribute}"

    def isbigger(self, other):
        if self.attribute >= other.attribute:
            return True
        else:
            return False

    def trylogging(self):
        self.log.debug('Start trylogging')
        start = 0
        try:
            start = time.perf_counter()
            # Insert Fuctionality here
            for x in range(1000):
                time.sleep(1)
                
        except Exception as e:
            self.log.exception(e, exc_info=True)
        end = time.perf_counter()
        total = end - start
        outmsg = 'trylogging, completed in {0} Seconds'.format(round(total, 2))
        self.log.debug(outmsg)
        return 


def main():
    x = SimpleFeature("first feature", 120)
    y = SimpleFeature("second feature", 100)

    print(x)
    print(y)
    print(x.isbigger(y))
    print(y.isbigger(x))

 
if __name__ == '__main__':
    main()