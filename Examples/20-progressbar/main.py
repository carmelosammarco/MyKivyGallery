from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyBoxLayout(Widget):
    def press(self):
        current = self.ids.my_bar.value

        if current == 1:
            current = 0

        current += 0.25
        self.ids.my_bar.value = current
        self.ids.my_label.text = f'{int(current*100)}% Progress'

class ProgressbarApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    ProgressbarApp().run()