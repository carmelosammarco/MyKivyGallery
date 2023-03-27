from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyBoxLayout(Widget):
    def start(self):
        
        self.ids.my_image.source = "photo/buttondark.png"

    def start_off(self):
        self.ids.my_image.source = "photo/button.png"
        self.ids.my_label.text = "You started!!"



class ButtonimgApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    ButtonimgApp().run()