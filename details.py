from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import *
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp

button_gender = Button(text='--Select--')

class MyApp(App):

    def build(self):
        layout= GridLayout(cols=4)
        
        self.label = Label(text="")
        layout.add_widget(self.label)
        self.label = Label(text="")
        layout.add_widget(self.label)
        self.label = Label(text="")
        layout.add_widget(self.label)
        self.label = Label(text="")
        layout.add_widget(self.label)
        self.label = Label(text="")
        layout.add_widget(self.label)

        self.label1 = Label(text="ID")
        layout.add_widget(self.label1)
        self.user_id= TextInput(text='', multiline=False)
        layout.add_widget(self.user_id)

        self.label = Label(text="")
        layout.add_widget(self.label)
        self.label = Label(text="")
        layout.add_widget(self.label)


        self.label2 = Label(text="Name")
        layout.add_widget(self.label2)
        self.uname= TextInput(text='', multiline=False)
        layout.add_widget(self.uname)

        self.label = Label(text="")
        layout.add_widget(self.label)
        self.label = Label(text="")
        layout.add_widget(self.label)


        self.labelG = Label(text="Gender")
        layout.add_widget(self.labelG)
        dropdown_gender = DropDown()
        btn_male = Button(text='Male', size_hint_y=None, height=30)
        btn_male.bind(on_release=lambda btn: dropdown_gender.select(btn_male.text))
        dropdown_gender.add_widget(btn_male)
        btn_female = Button(text='Female', size_hint_y=None, height=30)
        btn_female.bind(on_release=lambda btn: dropdown_gender.select(btn_female.text))
        dropdown_gender.add_widget(btn_female)
        button_gender.bind(on_release=dropdown_gender.open) 
        dropdown_gender.bind(on_select=lambda instance, x: setattr(button_gender, 'text', x))
        layout.add_widget(button_gender)

        self.label = Label(text="")
        layout.add_widget(self.label)

        self.label = Label(text="")
        layout.add_widget(self.label)


        self.label0 = Label(text="Age")
        layout.add_widget(self.label0)
        self.age = TextInput(text='', multiline=False)
        layout.add_widget(self.age)

        self.label = Label(text="")
        layout.add_widget(self.label)
        self.label = Label(text="")
        layout.add_widget(self.label)


        self.label3 = Label(text="Address")
        layout.add_widget(self.label3)
        self.address = TextInput(text='', multiline=False)
        layout.add_widget(self.address)

        self.label = Label(text="")
        layout.add_widget(self.label)
        self.label = Label(text="")
        layout.add_widget(self.label)


        self.label4 = Label(text="Contact")
        layout.add_widget(self.label4)
        self.contact = TextInput(text='', multiline=False)
        layout.add_widget(self.contact)
        self.label = Label(text="")
        layout.add_widget(self.label)
        self.label = Label(text="")
        layout.add_widget(self.label)

        self.label5 = Label(text="Email")
        layout.add_widget(self.label5)
        self.email = TextInput(text='', multiline=False)
        layout.add_widget(self.email)

        self.label = Label(text="")
        layout.add_widget(self.label)
        self.label = Label(text="")
        layout.add_widget(self.label)

        self.label6 = Label(text="Height")
        layout.add_widget(self.label6)
        self.height = TextInput(text='', multiline=False)
        layout.add_widget(self.height)

        self.label = Label(text="")
        layout.add_widget(self.label)

        self.label = Label(text="")
        layout.add_widget(self.label)

        self.label7 = Label(text="Weight")
        layout.add_widget(self.label7)
        self.weight = TextInput(text='', multiline=False)
        layout.add_widget(self.weight)

        self.label = Label(text="")
        layout.add_widget(self.label)
        self.label = Label(text="")
        layout.add_widget(self.label)
        self.label = Label(text="")
        layout.add_widget(self.label)
        self.label = Label(text="")
        layout.add_widget(self.label)
        self.label = Label(text="")
        layout.add_widget(self.label)
        self.label = Label(text="")
        layout.add_widget(self.label)

        layout2= GridLayout(cols=2)
        self.label = Label(text="")
        layout2.add_widget(self.label)
        btn_update = Button(text="Update")
        btn_update.bind(on_press=self.buttonClicked_update)
        layout2.add_widget(btn_update)
        self.label = Label(text="")
        layout2.add_widget(self.label)
        layout.add_widget(layout2)

        return layout

    def buttonClicked_update(self, btn):
        pass

if __name__ == '__main__':
    MyApp().run()
