from kivy.app import App
from kivy.uix.button import Label, Button


class MainApp(App):
    def build(self):
        return Button(text='Hello!')

MainApp().run()

