import kivy
kivy.require("1.10.1")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup


class CustomPopup(Popup):
    pass


class MasterLayout(BoxLayout):
    checkbox_is_active = ObjectProperty(False)

    def checkbox_18_clicked(self, instance, value):
        if value is True:
            print("Checkbox checked")
        else:
            print("Checkbox is Unchecked")


class MasterApp(App):
    def build(self):
        return MasterLayout()


master_app = MasterApp()
master_app.run()
