import os
import sys
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

class MyApp(App):

    def build(self):
        layout= GridLayout(cols=1)
        
        label= Label(text="Personal AI Dietician", font_size='40sp')
        layout.add_widget(label)

        label= Label()
        layout.add_widget(label)

        btn_details = Button(text="My Details")
        btn_details.bind(on_press=self.buttonClicked_details)
        layout.add_widget(btn_details)

        btn_bmi = Button(text="BMI Status")
        btn_bmi.bind(on_press=self.buttonClicked_bmi)
        layout.add_widget(btn_bmi)

        btn_plan = Button(text="Diet Plan")
        btn_plan.bind(on_press=self.buttonClicked_plan)
        layout.add_widget(btn_plan)

        btn_chart = Button(text="Diet Chart")
        btn_chart.bind(on_press=self.buttonClicked_chart)
        layout.add_widget(btn_chart)

        btn_bot = Button(text="Hygieia")
        btn_bot.bind(on_press=self.buttonClicked_bot)
        layout.add_widget(btn_bot)

        btn_feedback = Button(text="Feedback")
        btn_feedback.bind(on_press=self.buttonClicked_feedback)
        layout.add_widget(btn_feedback)
               
        return layout

    def buttonClicked_details(self,btn):
        os.system('python details.py')
    
    def buttonClicked_bmi(self,btn):
        os.system('python bmi.py')
    
    def buttonClicked_plan(self,btn):
        os.system('python dietplan.py')
    
    def buttonClicked_chart(self,btn):
        os.system('python dietChart.py')
    
    def buttonClicked_feedback(self,btn):
        os.system('python feedback.py')
    
    def buttonClicked_bot(self,btn):
        os.system('python hygieia.py')

if __name__ == '__main__':
    MyApp().run()