from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder


class MyBoxLayout(Widget):
    def press(self):
        name = self.ids.name_input.text
        # update label
        self.ids.name_label.text = name

class updatelabelApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    updatelabelApp().run()