from db.models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time, random, os



class CLI:
    def __init__(self, z="hello"):
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
            time.sleep(.5)
        print('\n')
        print("finish start")
        self.start()

    def menu(self):
        print("1) ...")
        print("2) ...")
        print("3) ...")
        print("4) ...")
        print("5) Quit")

    def start(self):
        exit = False
        while exit == False:
            self.menu()
            sel = input("What would you like to do?")

            if sel == 1:
                pass

            elif sel == 2:
                pass

            elif sel == 3:
                pass

            elif sel == 4:
                pass

            elif sel == 5:
                exit = True
            
            else:
                print("Invalid Input!")
                print ("Restarting")
                for _ in range(4):
                    print('.', end=' ')
                    time.sleep(.5)
                print('\n')
                os.system('cls' if os.name == 'nt' else 'clear')
                self.init()
            # z = input("Would You Like To Continue?\n")
            # if z == 'q' or z == 'Q':
            #     exit = True


if __name__ == '__main__':
    engine = create_engine('sqlite:///thriddb.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    CLI()
    time.sleep(5)