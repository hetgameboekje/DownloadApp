from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from music import download_playlist

class MyApp(App):
    def build(self):
        # Create the main layout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Create text input fields
        self.text_input1 = TextInput(multiline=False, hint_text='Enter text 1')
        self.text_input2 = TextInput(multiline=False, hint_text='Enter text 2')

        # Create a button
        button = Button(text='Run Code')
        button.bind(on_press=self.run_code)  # Bind the on_press event to the run_code method

        # Create a label for displaying the result
        self.result_label = Label(text='Result will be displayed here.')

        # Add widgets to the layout
        layout.add_widget(self.text_input1)
        layout.add_widget(self.text_input2)
        layout.add_widget(button)
        layout.add_widget(self.result_label)

        return layout

    def run_code(self, instance):
        # Get the text from the input fields
        playlist_url = self.text_input1.text
        download_dir = self.text_input2.text
        
        # Call the function from music.py with the user-entered variables
        download_playlist(playlist_url, download_dir)

        # Update the result label
        result = f'Success! Playlist URL: {playlist_url}, Download Dir: {download_dir}'
        self.result_label.text = result

if __name__ == '__main__':
    MyApp().run()
