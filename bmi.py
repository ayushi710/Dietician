from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import *
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp

class MyApp(App):

    def build(self):
        mainlayout = BoxLayout(orientation='vertical',padding=10,spacing=5)
        layout= GridLayout(cols=4)

        self.label = Label(text="")
        layout.add_widget(self.label)
        label= Label(text="BMI", font_size='40sp')
        layout.add_widget(label)
        label0= Label(text="Calculator", font_size='40sp')
        layout.add_widget(label0)
        self.label = Label(text="")
        layout.add_widget(self.label)
        mainlayout.add_widget(layout)


        self.label = Label(text="")
        mainlayout.add_widget(self.label)

        layout= GridLayout(cols=4)
        self.label = Label(text="")
        layout.add_widget(self.label)
        self.label1 = Label(text="Weight")
        layout.add_widget(self.label1)
        self.wt= TextInput(text='', multiline=False)
        layout.add_widget(self.wt)
        self.label2 = Label(text="kg")
        layout.add_widget(self.label2)
        mainlayout.add_widget(layout)

        layout= GridLayout(cols=4)
        self.label = Label(text="")
        layout.add_widget(self.label)
        self.label3 = Label(text="Height")
        layout.add_widget(self.label3)
        self.ht= TextInput(text='', multiline=False)
        layout.add_widget(self.ht)
        self.label4 = Label(text="cm")
        layout.add_widget(self.label4)
        mainlayout.add_widget(layout)

        self.label = Label(text="")
        mainlayout.add_widget(self.label)

        layout= GridLayout(cols=5)
        self.label = Label(text="")
        layout.add_widget(self.label)
        self.label = Label(text="")
        layout.add_widget(self.label)
        btn_calc = Button(text="Calculate BMI")
        btn_calc.background_normal=""
        btn_calc.background_color=[0,1,0,0.5]
        btn_calc.bind(on_press=self.calc)
        layout.add_widget(btn_calc)
        self.label = Label(text="")
        layout.add_widget(self.label)
        self.label = Label(text="")
        layout.add_widget(self.label)
        mainlayout.add_widget(layout)

        layout= GridLayout(cols=4)
        self.label = Label(text="")
        layout.add_widget(self.label)
        self.label5=Label(text="Your Body Mass Index is :")
        layout.add_widget(self.label5)
        self.label7 = Label(text="")
        layout.add_widget(self.label7)
        self.label = Label(text="")
        layout.add_widget(self.label)
        mainlayout.add_widget(layout)

        layout= GridLayout(cols=4)
        self.label = Label(text="")
        layout.add_widget(self.label)
        self.label6=Label(text="You are :")
        layout.add_widget(self.label6)
        self.label9 = Label(text="")
        layout.add_widget(self.label9)
        self.label = Label(text="")
        layout.add_widget(self.label)
        mainlayout.add_widget(layout)

        self.label = Label(text="")
        mainlayout.add_widget(self.label)
        self.label = Label(text="")
        mainlayout.add_widget(self.label)
        
        return mainlayout
    
    def calc(self, btn):
        weight = int(self.wt.text)
        height = int(self.ht.text)
        bmi = (weight * 10000)/(height * height)
        bmi = float("{0:.2f}".format(bmi))
        if bmi >= 25.0:
            status = "Over Weight"
        elif bmi >= 18.5 and bmi < 25.0:
            status = "Healthy"
        else:
            status = "Under Weight"
        self.label7.text = str(bmi)
        self.label9.text = status

if __name__ == '__main__':
    MyApp().run()