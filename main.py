from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup

class MyApp(App):
    def build(self):
        # Create the main layout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Create text input fields
        self.text_input1 = TextInput(multiline=False, hint_text='Enter text 1')
        self.text_input2 = TextInput(multiline=False, hint_text='File location will be displayed here.', readonly=True)

        # Create a label for displaying the result
        self.result_label = Label(text='Result will be displayed here.')

        # Create a button to run code
        run_button = Button(text='Run Code', on_press=self.run_code)

        # Create a button to open the file explorer
        file_button = Button(text='Open File Explorer', on_press=self.open_file_explorer)

        # Add widgets to the layout
        layout.add_widget(self.text_input1)
        layout.add_widget(self.text_input2)
        layout.add_widget(file_button)
        layout.add_widget(run_button)
        layout.add_widget(self.result_label)

        return layout

    def run_code(self, instance):
        # Get the text from the input fields
        text1 = self.text_input1.text
        text2 = self.text_input2.text

        # Perform some processing or code execution here
        # For example, concatenate the input texts
        result = f'Success! Text 1: {text1}, Text 2: {text2}'

        # Display the result in the label
        self.result_label.text = result

    def open_file_explorer(self, instance):
        # Create a popup for the file explorer
        file_chooser = FileChooserListView()
        file_popup = Popup(title='Select File', content=file_chooser, size_hint=(0.9, 0.9), auto_dismiss=False)

        # Bind the selection event to set the file location
        file_chooser.bind(on_submit=lambda x: self.set_file_location(file_chooser, file_popup))

        # Open the file explorer popup
        file_popup.open()

    def set_file_location(self, file_chooser, file_popup):
        # Set the selected file location to the text input
        selected_file = file_chooser.selection and file_chooser.selection[0] or ''
        self.text_input2.text = selected_file

        # Close the file explorer popup
        file_popup.dismiss()

if __name__ == '__main__':
    MyApp().run()
