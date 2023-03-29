from db.models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time, random



class CLI:
    def __init__(self, user_input):
        self.town = [town for town in session.query(Town)]
        self.restaurant = [restaurant for restaurant in session.query(Restaurant)]
        self.review = [review for review in session.query(Review)]
        self.name = user_input
        self.start()

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
        self.demo()

    def menu():
        print("1) ...")
        print("1) ...")
        print("1) ...")
        print("1) ...")
        print("1) ...")

    def start(self):
        print('Welcome to ')
        exit = False
        while exit == False:
            sel = input("What would you like to do?")
            self.menu()
            
            pass
            z = input("Would You Like To Continue?\n")
            if z == 'q' or z == 'Q':
                exit = True


if __name__ == '__main__':
    engine = create_engine('sqlite:///thriddb.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    user_input = input("Enter your name:")
    CLI(user_input)
    time.sleep(5)