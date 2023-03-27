from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.animation import Animation

class MyBoxLayout(Widget):
    def animate_it(self, widget, *args):
        animate = Animation(
            background_color=(0,1,0,1),
            duration= 1,
        )

        animate += Animation(
            size_hint = (1,1),
        )

        animate += Animation(
            size_hint = (.5,.5),
        )

        animate += Animation(
            pos_hint= {"center_x": 0.1},
        )

        animate += Animation(
            pos_hint= {"center_x": 0.5},
        )

        animate += Animation(  #to add another slot of animation
            opacity=0,
            duration=3,
        )

        animate.start(widget)

        animate.bind(on_complete =self.my_callback)
    
    def my_callback(self, *args):
        self.ids.my_label.text = "Animation Done!!"



class AnimationApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    AnimationApp().run()