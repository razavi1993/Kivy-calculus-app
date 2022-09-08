from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from sympy import *

x = symbols('x')

def take_deriv(func_str):
	return diff(eval(func_str), x)

def take_integ(func_str):
	return integrate(eval(func_str), x)

class MyLayout(FloatLayout):
	
	def show_deriv(self):
		try:
			self.ids.result.text = ""
			func_str = self.ids.my_func.text
			self.ids.result.text = str(take_deriv(func_str))

		except Exception:
			self.ids.result.text = "Error!"

	def show_integ(self):
		try:
			self.ids.result.text = ""
			func_str = self.ids.my_func.text
			self.ids.result.text = str(take_integ(func_str))
		except Exception:
			self.ids.result.text = "Error!"

class MainApp(MDApp):
	def build(self):
		return MyLayout()

app = MainApp()
app.run()

