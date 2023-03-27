import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button



class MyGridLayout(GridLayout):
    # Inizialise infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout contructor
        super(MyGridLayout, self).__init__(**kwargs)

        # Set columns
        self.cols = 2

        # Add widget
        self.add_widget(Label(text="Name: "))
        # Add Input Box
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        # Add widget
        self.add_widget(Label(text="Surname: "))
        # Add Input Box
        self.surname = TextInput(multiline=False)
        self.add_widget(self.surname)

        # Create a button
        self.submit = Button(text="Submit", font_size=32)
        # Bind the button
        self.submit.bind(on_press=self.press)
        # Add the button
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        surname = self.surname.text
        # print(f'Hello {name}  {surname}!')
        self.add_widget(Label(text=f'Hello {name}  {surname}!'))
        # Clear input boxes
        self.name.text = ""
        self.surname.text = ""






class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()