from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.tabbedpanel import TabbedPanel

class MyBoxLayout(TabbedPanel):
    pass

class TabsApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    TabsApp().run()