from db.models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time, random



class CLI:
    def __init__(self, z):
        print(z)
        self.init()

    def init(self):
        print("Starting CLI Interface...\n")
        time.sleep(.5)
        print(' . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .')
        time.sleep(.5)
        print('.                                                                    .')
        time.sleep(.5)
        print('.                        MARK COATS                                  .')
        time.sleep(.5)
        print('.                        RAYMOND AN                                  .')
        time.sleep(.5)
        print(".                        KYLE O'NEILL                                .")
        time.sleep(.5)
        print('.                                                                    .')
        time.sleep(.5)
        print(' . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .')
        for _ in range(4):
            print('.                                                                    .')
            time.sleep(1)
        print('\n')
        print("finish start")
        self.start()

    def start(self):
        exit = False
        while exit == False:
            pass
            z = input("Would You Like To Continue?\n")
            if z == 'q' or z == 'Q':
                exit = True





if __name__ == '__main__':
    engine = create_engine('sqlite:///thriddb.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    print("Test Out\n")
    z = input("Enter some shit\n")
    CLI(z)
    time.sleep(5)