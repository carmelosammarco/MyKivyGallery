from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('my.kv') # Use a whatever kv file using the Builder

class MyGridLayout(Widget):

    name = ObjectProperty(None)
    surname = ObjectProperty(None)
   
    def press(self):
        name = self.name.text
        surname = self.surname.text
        print(f'Hello {name}  {surname}!')
        # Clear input boxes
        self.name.text = ""
        self.surname.text = ""

class coolApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    coolApp().run()