from kivy.app import App
from kivy.uix.image import Image


class MainApp(App):
    def build(self):
        img = Image(source='Picsart_23-10-22_22-34-05-877.jpg',
                    size_hint=(1, .5),
                    pos_hint={'center_x': .5, 'center_y': .5})

        return img


if __name__ == '__main__':
    app = MainApp()
    app.run()