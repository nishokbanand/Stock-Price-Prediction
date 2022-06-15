# import pickle
# with open("model.pkl","rb") as f:
#     p=pickle.load(f)
#     f.close()
# print("predicted stock market price of year are:",p.predict([[2901]]))

# importing pyplot for graph plotting
from matplotlib import pyplot as plt
import pickle

# importing numpy
import pandas as pd
import numpy as np
from kivy.garden.matplotlib import FigureCanvasKivyAgg

# importing kivyapp
from kivymd.uix.screen import MDScreen


# importing kivy builder
from kivy.lang import Builder
import kivy.garden.matplotlib



# this is the main class which will
# render the whole application
class Graph(MDScreen):

	def __init__(self,string,result):
		string=int(string)
		result=int(float(result))
		y1,y2=2000,3000
		self.str = Builder.load_string("""
MDScreen:
    MDBoxLayout:
        layout:layout
        size_hint:(0.8,0.8)
        pos_hint:{"center_x":0.5,"center_y":0.5}
        BoxLayout:
        
            id:layout
	MDFillRoundFlatButton:
        text: "Check"
        md_bg_color: (233/255, 59/255, 129/255,0.5)
        pos_hint:{"center_x":0.9,"center_y":0.9}
        on_release:app.change_screen1()
        
								""")
		df=pd.read_csv("stock_market.csv")

		import matplotlib.dates as mdates
		years = mdates.YearLocator() # Get every year
		yearsFmt = mdates.DateFormatter('%Y') # Set year format
		fig,ax= plt.subplots()# Create subplots to plot graph and control axes
		ax.plot(df['Date'], df['Close'])
		# Format the ticks
		ax.xaxis.set_major_locator(years)
		ax.xaxis.set_major_formatter(yearsFmt)

		plt.title('Close Stock Price History')
		plt.xlabel('Date')
		plt.ylabel('Closing Stock Price in $')
		if y1>string :
			y1=string/2
			y2=string*2
		elif y2<string:
			y1=y2/2
			y2=string*2
		plt.xlim([y1, y2])

		plt.plot(string, result, marker="o", markersize=10, markeredgecolor="red", markerfacecolor="green")
		
		
		# adding plot to kivy boxlayout
		self.str.ids.layout.add_widget(FigureCanvasKivyAgg(plt.gcf()))

