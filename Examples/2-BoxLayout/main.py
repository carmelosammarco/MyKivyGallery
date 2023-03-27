from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('box.kv') # Use a whatever kv file using the Builder

class MyBoxLayout(Widget):
    pass

class coolApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    coolApp().run()