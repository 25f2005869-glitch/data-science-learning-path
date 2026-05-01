#ScreenTime analysis is the task of analyzing and creating a report on which application 
#and websites are used and used for how much time. 
#Apple devices have one of the best ways of creating a screen time report. 

import pandas as pd
import numpy as np 
import plotly.express as px 
import plotly.graph_objects as go

data = pd.read_csv("screen_time_app_details.csv")
#print(data.head())
#print(data.isnull().sum())
#print(data.describe())
figure = px.bar(data_frame=data, x="Data", y="Notification", 
color="App", title="Notification graph")
figure.show()

figure = px.scatter(data_frame=data, x="Notification", y="Usage", 
size="Notification", trendline="ols", title="Relationship between Notifications and Usage")
figure.show()


