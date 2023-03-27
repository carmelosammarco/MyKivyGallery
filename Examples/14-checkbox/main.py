from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window

class MyBoxLayout(Widget):
    checks=[]
    def checkbox_click(self, instance, value, topping):
        if value == True:
            MyBoxLayout.checks.append(topping)
            tops = ''
            for x in MyBoxLayout.checks:
                tops = f'{tops} {x}'
            self.ids.output_label.text = f'You selected: {tops}'
        else:
            MyBoxLayout.checks.remove(topping)
            tops = ''
            for x in MyBoxLayout.checks:
                tops = f'{tops} {x}'
            self.ids.output_label.text = f'You removed: {tops}'

            

class CheckApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return MyBoxLayout()

if __name__ == '__main__':
    CheckApp().run()