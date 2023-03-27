from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

from kivy.core.window import Window

Builder.load_file('bg.kv') # Use a whatever kv file using the Builder

class MyBoxLayout(Widget):
    pass

class coolApp(App):
    def build(self):
        Window.clearcolor = (1,1,0,1)
        return MyBoxLayout()

if __name__ == '__main__':
    coolApp().run()