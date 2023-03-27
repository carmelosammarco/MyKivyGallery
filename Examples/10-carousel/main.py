from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyBoxLayout(Widget):
    pass

class CarouselApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    CarouselApp().run()