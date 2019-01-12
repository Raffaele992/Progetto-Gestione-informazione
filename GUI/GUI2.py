from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from kivy.core.window import Window

class DBListButton(ListItemButton):
    pass


class ProjectDB(BoxLayout):
    author_text_input = ObjectProperty()
    title_text_input = ObjectProperty()
    year_from_text_input = ObjectProperty()
    year_to_text_input = ObjectProperty()

    def search_DB(self):
        pass

    def reset_search_DB(self):
        pass

    def quit_DB(self):
        return exit()


class ProjectDBApp(App):
    def build(self):
        Window.clearcolor = (0.7, 0.7, 0.7, 0)
        return ProjectDB()


dbApp = ProjectDBApp()
dbApp.run()
