from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Button, Static, Input, DataTable
from textual.containers import Container
from db.models import Town, Restaurant, Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


#Define needed widgets / overall functions
#   Main Page, All Data Page, Relation Page, Add Page
#   Main Page
#       Will ask for user login, greet, and display page options as well as quit option
#   Data Page
#       Will list available data categories and display data upon request, has back button
#   Relation Page
#       Will list available data categories and display data updon request, has back button
#   Add Page    
#       Will list available data categories, provide form to add to each category, handle adding and updating database, refresh, display updated data, has back button


class Model:
    def __init__(self):
        engine = create_engine('sqlite:///db/thirddb.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        towns = [town for town in session.query(Town)]
        restaurants = [rest for rest in session.query(Restaurant)]
        reviews = [rev for rev in session.query(Review)]


class LoginPage(Screen):
    """Main Page"""

    def compose(self):
        yield Header(show_clock=True)
        yield Footer()
        yield LoginWidget()

class MainPage(Screen):
    """Test Page"""

    BINDINGS=[('q', "pop_screen()", "Log Out")]


    def compose(self):
        yield Header(show_clock=True)
        yield Footer()
        yield Static(f"Welcome, {self.get_name()}", id="welcome")
        yield MainOptionWidget()
    def on_load(self):
        self.query_one("#welcome").update()
    def get_name(self):
        name = CLI.data["username"]
        if len(name) > 0:
            return name
        else: 
            return "Guest"
        


class MainOptionWidget(Static):
    
    def compose(self):
        yield Button("Retrieve Data Lists", id="dataButton")
        yield Button("View Relationship", id="relationButton")
        yield Button("Add Data", id="addButton")

    def on_button_pressed(self, event:Button.Pressed):
        if event.button.id == "dataButton":
            app.push_screen('Retrieve')

class RetrievePage(Screen):

    BINDINGS=[('q', "pop_screen()", "Go Back"), ('1 t', 'get_towns', 'Town Data')]

    def compose(self):
        yield Header(show_clock=True)
        yield Footer()
        # yield DataTable(id="Retrieved", name="Container", zebra_stripes=True)
        yield Static("Hello",id="test")
        yield Container(id="xx")

    def get_towns(self):
        towns = CLI.model.towns
        t = self.query_one("#xx").mount(Static("this"))
        file = open("./log.txt", 'w')
        file.write(t)
        file.close()


        





class LoginWidget(Static):
    """Login Widget"""

    nameBool = False

    def compose(self) -> ComposeResult:
        """Create child widgets"""
        yield Input(placeholder="Username", id="username")
        yield Button("Log In", id="submit", variant="success")
        yield Container(id="temp")

    def on_button_pressed(self, event:Button.Pressed) -> None:
        inp = self.query_one('#username').value
        self.set_name(inp)
        self.app.push_screen("Menu")
    
    def set_name(self, name):
        CLI.data["username"] = name


class CLI(App):
    """A Textual app to find restaurants and reviews."""

    data = {
        "username": ''
    }
    model = Model()

    CSS_PATH="cli.css"
    SCREENS= {"Login": LoginPage(), "Menu": MainPage(), "Retrieve": RetrievePage()}
    BINDINGS = [('q', "exit", 'Exit'),("d", "toggle_dark", "Toggle dark mode")]

    def on_mount(self):
        self.push_screen("Login")

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark
    def action_exit(self):
        self.exit("Exiting")


if __name__ == "__main__":
    app = CLI()
    app.run()
