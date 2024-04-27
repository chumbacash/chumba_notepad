# chumba_notepad_gui.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.text import LabelBase

class ChumbaNotepadGUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create a text input widget for the notepad
        self.text_input = TextInput(multiline=True, text="Write your note here")

        # Bind events for text selection and hover
        self.text_input.bind(on_cursor_pos=self.on_cursor_pos)
        self.text_input.bind(on_touch_down=self.on_touch_down)

        # Add the text input widget to the layout
        self.add_widget(self.text_input)

    def on_cursor_pos(self, instance, cursor_pos):
        # Check if text is selected
        if instance.selection_text:
            # Text is selected, display formatting options
            LabelBase.register(name='Arial',
                        fn_regular='Arial.ttf')
            instance.font_name='Arial'
        else:
            # No text is selected, hide formatting options
            instance.font_name = 'default'

    def on_touch_down(self, instance, touch):
        # Check if touch is inside the TextInput
        if instance.collide_point(*touch.pos):
            # Touch is inside the TextInput, check for hover
            if touch.is_double_tap:
                # Touch is a double-tap, display formatting options
                instance.font_name = 'Arial'
        else:
            # Touch is outside the TextInput, hide formatting options
            instance.font_name = 'default'
