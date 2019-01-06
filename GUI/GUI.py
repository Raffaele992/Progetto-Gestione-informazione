from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
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
