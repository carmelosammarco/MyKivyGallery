from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyBoxLayout(Widget):
    def spinner_clicked(self, value):
        self.ids.click_label.text = f'You selected: {value}'


class DropdownApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    DropdownApp().run()