# chumba_notepad_gui.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class ChumbaNotepadGUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create a text input widget for the notepad
        self.text_input = TextInput(multiline=True)

        # Create buttons for text formatting
        self.bold_button = Button(text="B", size_hint=(None, None))
        self.bold_button.bind(on_press=self.toggle_bold)
        self.italic_button = Button(text="I", size_hint=(None, None))
        self.italic_button.bind(on_press=self.toggle_italic)
        self.underline_button = Button(text="U", size_hint=(None, None))
        self.underline_button.bind(on_press=self.toggle_underline)

        # Create a save button
        self.save_button = Button(text="Save", size_hint=(None, None))
        self.save_button.bind(on_press=self.save_note)

        # Add buttons and text input to the layout
        self.add_widget(self.bold_button)
        self.add_widget(self.italic_button)
        self.add_widget(self.underline_button)
        self.add_widget(self.text_input)
        self.add_widget(self.save_button)

    def toggle_bold(self, instance):
        # Toggle bold formatting for selected text
        self.text_input.bold = not self.text_input.bold

    def toggle_italic(self, instance):
        # Toggle italic formatting for selected text
        self.text_input.italic = not self.text_input.italic

    def toggle_underline(self, instance):
        # Toggle underline formatting for selected text
        self.text_input.underline = not self.text_input.underline

    def save_note(self, instance):
        # Get the text from the text input widget
        note_text = self.text_input.text

        # Save the note to a file
        with open("note.txt", "w") as file:
            file.write(note_text)

        # Optional: Provide feedback to the user
        print("Note saved successfully!")
