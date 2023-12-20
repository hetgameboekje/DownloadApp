from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MyApp(App):
    def build(self):
        # Create the main layout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Create text input fields
        self.text_input1 = TextInput(multiline=False, hint_text='Enter text 1')
        self.text_input2 = TextInput(multiline=False, hint_text='Enter text 2')

        # Create a button
        button = Button(text='Run Code', on_press=self.run_code)

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
        text1 = self.text_input1.text
        text2 = self.text_input2.text

        # Perform some processing or code execution here
        # For example, concatenate the input texts
        result = f'Success! Text 1: {text1}, Text 2: {text2}'

        # Display the result in the label
        self.result_label.text = result

if __name__ == '__main__':
    MyApp().run()
