from asciimatics.widgets import *
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import NextScene, StopApplication
from db.models import Town, Restaurant, Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time, random


class Model(object):
    def __init__(self):
        self.towns = [town for town in session.query(Town)]
        self.restaurants = [restaurant for restaurant in session.query(Restaurant)]
        self.reviews = [review for review in session.query(Review)]
        self.all =[("towns",self.towns), ("restaurants",self.restaurants), ("reviews",self.reviews)]
    
    def get_all(self):
        return(self.all)
    
    def get_towns(self):
        ret = session.query(Town)
        print(return_list)
        return [return_list]





class MainScreen(Frame):

    def __init__(self, screen, database):
        super(MainScreen, self).__init__(screen,
                                          screen.height ,
                                          screen.width ,
                                          hover_focus=True,
                                          can_scroll=False,
                                          #data=database,
                                          title="PlatePals",
                                          reduce_cpu=True)
        layout = Layout([1], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Divider(height=5))
        layout.add_widget(Label("PlatePals Main Screen", align='^'))
        layout.add_widget(Label("--PlatePals--", align='^'))
        layout.add_widget(Label("Interactive Restaurant UI", align='^'))
        layout.add_widget(Label("'Find a restaurant near you!'", align='^'))
        layout2 = Layout([1,1,1,1])
        self.add_layout(layout2)
        layout2.add_widget(Button("Retrieve Data", self._retrieve),0)
        layout2.add_widget(Button("Relationships", self._relative),1)
        layout2.add_widget(Button("Add", self._add),2)
        layout2.add_widget(Button("Quit", self._quit),3)
        self.fix()
        
    def _ok(self):
        self.save()
        raise NextScene("Retrieve")

    def _retrieve(self):
        self.save()
        raise NextScene("Retrieve")

    def _relative(self):
        self.save()
        raise NextScene("Relative")

    def _add(self):
        self.save()
        raise NextScene("Add")
    
    @staticmethod
    def _quit():
        raise StopApplication("Successful Exit")
    
class RetrieveScreen(Frame):
    def __init__(self, screen, database):
        super(RetrieveScreen, self).__init__(screen,
                                          screen.height ,
                                          screen.width ,
                                          hover_focus=True,
                                          can_scroll=False,
                                          title="Retrieve Data",
                                          reduce_cpu=True)
        self.database = database
        self._list_view = ListBox(
            Widget.FILL_FRAME,
            database.get_towns(),
            name="towns",
            add_scroll_bar=True,
            on_change=self._ok,
            on_select=self._ok
        )
        self.mainlay = Layout([1], fill_frame=True)
        self.add_layout(self.mainlay)
        self.mainlay.add_widget(Divider(height=3))
        self.mainlay.add_widget(self._list_view)
        buttonlay = Layout([1,1,1,1])
        self.add_layout(buttonlay)
        buttonlay.add_widget(Button("Retrieve Town Data", self._town_data),0)
        buttonlay.add_widget(Button("Retrieve Restauraunt Data", self._ok),1)
        buttonlay.add_widget(Button("Retrieve Review Data", self._ok),2)
        buttonlay.add_widget(Button("Cancel", self._quit),3)
        self.fix()

    def _town_data(self):
         self.mainlay.add_widget(TextBox(5, "Text Box"))
         
         
         

    def _ok(self):
            pass

    @staticmethod
    def _quit():
            raise NextScene("Main")
    
class RelativeScreen(Frame):

    def __init__(self, screen):
        super(RelativeScreen, self).__init__(screen,
                                          screen.height ,
                                          screen.width ,
                                          hover_focus=True,
                                          can_scroll=False,
                                          title="View Relationships",
                                          reduce_cpu=True)
        mainlay = Layout([1], fill_frame=True)
        self.add_layout(mainlay)
        mainlay.add_widget(Divider(height=5))
        mainlay.add_widget(Label("This Is A Description", height=10, align='^'))
        mainlay.add_widget(Divider())
        buttonlay = Layout([1,1,1])
        self.add_layout(buttonlay)
        buttonlay.add_widget(Button("Restaurants in Towns", self._ok),0)
        buttonlay.add_widget(Button("Reviews for Restaurants", self._ok),1)
        buttonlay.add_widget(Button("Cancel", self._quit),2)
        self.fix()

    def _ok(self):
            pass

    @staticmethod
    def _quit():
            raise NextScene("Main")
    

class AddScreen(Frame):

    def __init__(self, screen):
        super(AddScreen, self).__init__(screen,
                                          screen.height ,
                                          screen.width ,
                                          hover_focus=True,
                                          can_scroll=False,
                                          title="Add Data",
                                          reduce_cpu=True)
        mainlay = Layout([1], fill_frame=True)
        self.add_layout(mainlay)
        mainlay.add_widget(Divider(height=5))
        mainlay.add_widget(Label("This Is A Description", height=10, align='^'))
        mainlay.add_widget(Divider())
        buttonlay = Layout([1,1,1,1])
        self.add_layout(buttonlay)
        buttonlay.add_widget(Button("Add Town", self._ok),0)
        buttonlay.add_widget(Button("Add Restaurant", self._ok),1)
        buttonlay.add_widget(Button("Add Review", self._ok),2)
        buttonlay.add_widget(Button("Cancel", self._quit),3)
        self.fix()

    def _ok(self):
            pass

    @staticmethod
    def _quit():
            raise NextScene("Main")
    
class UnusedScreen(Frame):
    zed = "Hello World"

    def __init__(self, screen):
        super(RetrieveScreen, self).__init__(screen,
                                          screen.height ,
                                          screen.width ,
                                          hover_focus=True,
                                          can_scroll=False,
                                          title="Retrieve Data",
                                          reduce_cpu=True)
        mainlay = Layout([1], fill_frame=True)
        self.add_layout(mainlay)
        mainlay.add_widget(Divider(height=2))
        mainlay.add_widget(Label(self.zed, align='^'))
        mainlay.add_widget(Divider(height=1))
        mainlay.add_widget(TextBox(height=8, label="output", readonly=True, as_string=True)).value=self.zed
        buttonlay = Layout([1,1,1,1])
        self.add_layout(buttonlay)
        buttonlay.add_widget(Button("Retrieve Data", self._ok),0)
        buttonlay.add_widget(Button("Relationships", self._ok),1)
        buttonlay.add_widget(Button("Add", self._ok),2)
        buttonlay.add_widget(Button("Cancel", self._quit),3)
        self.fix()


    def _ok(self):
            pass

    @staticmethod
    def _quit():
            raise NextScene("Main")
    
    
    
    
#Retrieve
#Relative
#Add
def t(screen):
    scenes = [
        Scene([MainScreen(screen, model)], -1, name="Main"),
        Scene([RetrieveScreen(screen, model)], -1,  name= "Retrieve"),
        Scene([RelativeScreen(screen)], -1,  name= "Relative"),
        Scene([AddScreen(screen)], -1,  name= "Add")
        ]
    screen.play(scenes, stop_on_resize=True, start_scene=None, allow_int=True)
    
if __name__ == '__main__':
    engine = create_engine('sqlite:///db/thirddb.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    model = Model()
    Screen.wrapper(t, catch_interrupt=True)
