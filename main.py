from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivymd.uix.list import OneLineListItem, ThreeLineListItem
from kivymd.uix.label import MDLabel
import requests
import json

class HomeScreen(Screen):
	
	def start(self):
		querystring = {'country': f'{self.ids.country.text}'}
		url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"
		headers = {
		    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
		    'x-rapidapi-key': "b21859cfffmshaff6d279482f4b3p11c3c5jsn446b2a67648c"
		    }

		response = requests.request("GET", url, headers=headers, params=querystring)
		response = response.json()
		print(response)
		lst=[]
		while True:
			try:
				for i in range(100):
					x = str(response['data']['covid19Stats'][i]['province'])
					y = str(response['data']['covid19Stats'][i]['confirmed'])
					z = str(response['data']['covid19Stats'][i]['deaths'])
					if [x] not in lst:
						lst.append([x,y,z])
			except:
				break
		i=0
		for a in lst:
			self.ids.scroll.add_widget(ThreeLineListItem(text=f"{a[0]}", secondary_text=f"Confirmed Cases: {a[1]}", tertiary_text=f"Deaths : {a[2]}"))
class GlobalScreen(Screen):
	pass

class ScreenManager(ScreenManager):
	pass

class MainApp(MDApp):
	
	def build(self):
		self.theme_cls.primary_palette = "Red"
		master = Builder.load_file("main.kv")
		return master
	
MainApp().run()