from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class Sport(MDApp):
    def build(self):
        return MDLabel(text="Hello, Sport", halign="center")


Sport().run()