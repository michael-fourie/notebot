from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from backend import main


class DropFile(Button):
    def __init__(self, **kwargs):
        super(DropFile, self).__init__(**kwargs)

        # get app instance to add function from widget
        app = App.get_running_app()

        # add function to the list
        app.drops.append(self.on_dropfile)

    def on_dropfile(self, widget, filename):
        # a function catching a dropped file
        # if it's dropped in the widget's area
        if self.collide_point(*Window.mouse_pos):
            # on_dropfile's filename is bytes (py3)
            self.text = filename.decode('utf-8')


class DropApp(App):
    def build(self):
        # set an empty list that will be later populated
        # with functions from widgets themselves
        self.drops = []

        # bind handling function to 'on_dropfile'
        Window.bind(on_dropfile=self.handledrops)

        stack = StackLayout()
        dragDrop = DropFile(text='Drag and drop your *.pptx file', font_size="32sp", size=(50, 50))
        stack.add_widget(dragDrop)

        title = Label(text="notebot v0.0.1", font_size="32sp", color=(1, 1 ,1 ,1))
        stack.add_widget(title)

        return stack


    def handledrops(self, *args):

        main.main(args[-1].decode())


DropApp().run()