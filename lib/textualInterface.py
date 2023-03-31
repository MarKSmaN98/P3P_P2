from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Button, Static, Input, DataTable, ContentSwitcher
from textual.containers import Container, Horizontal
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
    # towns = []
    # restaurants = []
    # reviews = []
    def __init__(self):
        engine = create_engine('sqlite:///db/thirddb.db')
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.towns = [town for town in self.session.query(Town)]
        self.restaurants = [rest for rest in self.session.query(Restaurant)]
        self.reviews = [rev for rev in self.session.query(Review)]


class LoginPage(Screen):
    """Main Page"""

    def compose(self):
        yield Header(show_clock=True)
        yield Footer()
        yield LoginWidget()

class MainPage(Screen):
    """Test Page"""

    BINDINGS=[('q', "pop_screen()", "Log Out"), ('z', "ret()", "Raw Data"), ('x', "rel()", "Relative Data"), ('c', "add", "Add Data")]


    def compose(self):
        yield Header(show_clock=True)
        yield Footer()
        with Container():
            yield Static(f"Welcome, {self.get_name()}", id="welcome")
        with Horizontal():
            yield Button("Retrieve Data Lists", id="dataButton")
            yield Button("View Relationship", id="relationButton")
            yield Button("Add Data", id="addButton")
    def on_load(self):
        self.query_one("#welcome").update()
    def get_name(self):
        name = CLI.data["username"]
        if len(name) > 0:
            return name
        else: 
            return "Guest"
        
    def on_button_pressed(self, event:Button.Pressed):
        if event.button.id == "dataButton":
            app.push_screen('Retrieve')
        elif event.button.id == "relationButton":
            app.push_screen("Relative")
        elif event.button.id == "addButton":
            app.push_screen("Add")

    def action_ret(self):
        app.push_screen('Retrieve')
    def action_rel(self):
        app.push_screen("Relative")
    def action_add(self):
        app.push_screen("Add")
        

    

class RetrievePage(Screen):

    BINDINGS=[('q', "pop_screen()", "Go Back"), ('t', 'get_towns()', 'Town Data'), ('r', 'get_rest()', 'Restaurant Data'), ('v', 'get_rev()', 'Review Data')]

    def compose(self):
        yield Header(show_clock=True)
        yield Footer()
        with Container(id="buttons"):
            yield Button("Raw Towns", id="town")
            yield Button("Raw Restaurants", id="rest")
            yield Button("Raw Reviews", id="rev")
        yield Container(id="target")
        yield Static(id="retrieved")

    def on_button_pressed(self, event:Button.Pressed):
        if event.button.id == 'town':
            self.action_get_towns()
        elif event.button.id == 'rest':
            self.action_get_rest()
        elif event.button.id == 'rev':
            self.action_get_rev()

    def action_get_towns(self):
        self.query_one("#retrieved").remove()
        towns = CLI.model.towns
        table = DataTable(id="retrieved", name="Container", zebra_stripes=True)
        table.add_columns("ID", "Town Name", "State", f"Length: {len(towns)}")
        for town in towns:
            table.add_row(town.id, town.name, town.id)
        self.query_one("#target").mount(table)

    def action_get_rest(self):
        self.query_one("#retrieved").remove()
        rest = CLI.model.restaurants     
        table = DataTable(id="retrieved", name="Container", zebra_stripes=True)
        table.add_columns("ID", "Name", "Address", "Phone", f"Length: {len(rest)}")
        for r in rest:
            table.add_row(r.id, r.name, r.address, r.phone)
        self.query_one("#target").mount(table)

    def action_get_rev(self):
        self.query_one("#retrieved").remove()
        table = DataTable(id="retrieved", name="Container", zebra_stripes=True)
        rev = CLI.model.reviews
        table.add_columns("ID", "Review", "Star Rating", f"Length: {len(rev)}")
        for r in rev:
            table.add_row(r.id, r.review_text, r.review_rating)
        self.query_one("#target").mount(table)
        pass
        
class RelativePage(Screen):

    BINDINGS=[('q', "pop_screen()", "Go Back"), ('t', 'get_towns_rest()', 'See Restaurants in Towns'), ('r', 'get_rest_rev()', 'See Restaurant Reviews')]

    def compose(self):
        yield Header(show_clock=True)
        yield Footer()
        with Container(id='buttons'):
            yield Button("View Restaurants in Towns", id='one')
            yield Button ("View Reviews for Restaurants", id='two')
        yield Container(id="target")
        yield Static(id="retrieved")

    def on_button_pressed(self, event:Button.Pressed):
        if event.button.id == "one":
            self.action_get_towns_rest()
        elif event.button.id == "two":
            self.action_get_rest_rev()

    def action_get_towns_rest(self):
        towns = CLI.model.towns
        rests = CLI.model.restaurants
        self.query_one("#retrieved").remove()
        table = DataTable(id="retrieved", name="Container", zebra_stripes=True)
        table.add_columns("Town", "Restaurants")
        for town in towns:
            table.add_row(town.name, None)
            for rest in rests:
                if rest.town_id == town.id:
                    table.add_row(None, rest.name)
        self.query_one("#target").mount(table)

    def action_get_rest_rev(self):
        rests = CLI.model.restaurants
        revs = CLI.model.reviews
        towns = CLI.model.towns
        self.query_one("#retrieved").remove()
        table = DataTable(id="retrieved", name="Container", zebra_stripes=True)
        table.add_columns("Town", "Restaurant", "Review", "Stars")
        for town in towns:
            table.add_row(town.name, None, None, None)
            for rest in rests:
                if rest.town_id == town.id:
                    table.add_row(None, rest.name, None, None)
                    for rev in revs:
                        if rev.restaurant_id == rest.id:
                            table.add_row(None, None, rev.review_text, rev.review_rating)
        self.query_one("#target").mount(table)


class AddPage(Screen):
    """Add"""

    BINDINGS=[('q', "pop_screen()", "Go Back"),('t', 'add_town()', "Add Town"),('r', 'add_rest()', "Add Restaurant"),('v', 'add_rev()', "Add Review")]


    def compose(self):
        yield Header(show_clock=True)
        yield Footer()
        yield Container(id="listswitch")
        yield DataTable(id="listview")
        with Horizontal(id="buttons"):
            yield Button("Add Town", id="town")
            yield Button("Add Restaurant", id="rest")
            yield Button("Add Review", id="rev")
        with ContentSwitcher(id="switcher", initial="town"):
            with Container(id="town"):
                yield Input(placeholder="Town Name", id="town_name")
                yield Input(placeholder="Town State", id="town_state")
                yield Button("Submit", id="town_submit")
            with Container(id="rest"):
                yield Input(placeholder="Restaurant Name", id="rest_name")
                yield Input(placeholder="Address", id="rest_address")
                yield Input(placeholder="Phone", id="rest_phone")
                yield Input(placeholder="Residing Town ID", id="rest_town")
                yield Button("Submit", id="rest_submit")
            with Container(id="rev"):
                yield Input(placeholder="Rating Text", id="rev_text")
                yield Input(placeholder="Stars", id="rev_stars")
                yield Input(placeholder="Pertaining Restaurant ID", id="rev_rest")
                yield Button("Submit", id="rev_submit")

    def on_button_pressed(self, event:Button.Pressed):
        #SWITCH BUTTONS
        if event.button.id == "town":
            self.query_one("#switcher").current=event.button.id
            self.pop_town()
        if event.button.id == "rest":
            self.query_one("#switcher").current=event.button.id
            self.pop_town()
        if event.button.id == "rev":
            self.query_one("#switcher").current=event.button.id
            self.pop_rest()
        #END SWITCH BUTTONS

        #SUBMIT BUTTONS
        if event.button.id == "town_submit":
            town_name = self.query_one("#town_name").value
            town_state = self.query_one("#town_state").value
            new_town = Town(name=town_name, state=town_state)
            self.add_town(new_town)
        if event.button.id == "rest_submit":
            rest_name = self.query_one("#rest_name").value
            rest_address = self.query_one("#rest_address").value
            rest_phone = self.query_one("#rest_phone").value
            rest_town = self.query_one("#rest_town").value
            new_rest = Restaurant(name=rest_name, address=rest_address, phone=rest_phone, town_id=rest_town)
            self.add_rest(new_rest)
        if event.button.id == "rev_submit":
            rev_text = self.query_one("#rev_text").value
            rev_stars = self.query_one("#rev_stars").value
            rev_rest = self.query_one("#rev_rest").value
            new_rev = Review(review_text=rev_text, review_rating=rev_stars, restaurant_id=rev_rest)
            self.add_rev(new_rev)
        #END SUBMIT BUTTONS

    #SQL QUERIES

    def add_town(self, town):
        session = CLI.model.session
        session.add(town)
        session.commit()
        CLI.model.towns.append(town)
    def add_rest(self, rest):
        session = CLI.model.session
        session.add(rest)
        session.commit()
        CLI.model.restaurants.append(rest)
    def add_rev(self, rev):
        session = CLI.model.session
        session.add(rev)
        session.commit()
        CLI.model.reviews.append(rev)
    
    #END SQL QUERIES

    #TABLE OPERATIONS

    def add_table(self, table):
        self.query_one('#listview').remove()
        self.query_one("#listswitch").mount(table)


    def pop_town(self):
        t_t = DataTable(id="listview", zebra_stripes=True)
        towns = CLI.model.towns
        t_t.add_columns("ID", "Town Name", "State", f"Length: {len(towns)}")
        for town in towns:
            t_t.add_row(town.id, town.name, town.id)
        self.add_table(t_t)

    def pop_rest(self):
        r_t = DataTable(id="listview", zebra_stripes=True)
        rest = CLI.model.restaurants
        r_t.add_columns("ID", "Name", "Address", "Phone", f"Length: {len(rest)}")
        for r in rest:
            r_t.add_row(r.id, r.name, r.address, r.phone)
        self.add_table(r_t)
    
    def pop_rev(self):
        v_t = DataTable(id="listview", zebra_stripes=True)
        rev = CLI.model.reviews
        v_t.add_columns("ID", "Review", "Star Rating", f"Length: {len(rev)}")
        for r in rev:
            v_t.add_row(r.id, r.review_text, r.review_rating)
        self.add_table(v_t)

    #END TABLE OPERATIONS

    #HOT KEY ACTIONS

    def action_add_town(self):
        self.query_one("#switcher").current="town"
        self.pop_town()
    def action_add_rest(self):
        self.query_one("#switcher").current="rest"
        self.pop_town()
    def action_add_rev(self):
        self.query_one("#switcher").current="rev"
        self.pop_rest()

    #END HOT KEY ACTIONS
        





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
    SCREENS= {"Login": LoginPage(), "Menu": MainPage(), "Retrieve": RetrievePage(), "Relative": RelativePage(), "Add": AddPage()}
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
