#for the iPhone sale analysis task, I have got a dataset containing data about iPhone in India on Flipkart.

# It will be an ideal dataset to analyze the sale of iPhone in India.

# You can download the dataset from video description.

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
sharaddata = pd.read_csv("apple_products.csv")
#print(sharaddata.head())
#print(sharaddata.describe())
print(sharaddata.isnull().sum())

Highest_rated = sharaddata.sort_values(by=["star Rating"], ascending = False)
highest_rated = Highest_rated.head(10)
#Print(highest_rated['product Name'])
iPhone = highest_rated['product Name'].value_counts()
label = iPhone.index
counts = highest_rated["Number of Ratings"]
figure = px.bar(highest_rated, x = label, Y = counts,
title = "Number of ratings of highest Rated IPhone")
figure.show()

iPhone = highest_rated['product Name'].value_counts()
label = iPhone.index
counts = highest_rated["Number of Reviews"]
figure = px.bar(highest_rated, x = label, Y = counts,
title = "Number of Reviews of highest Rated IPhone")
figure.show()

figure = px.scatter(data_frame = sharaddata, x = "Number of Ratings",
y = "Sale Price", size = "Discount Percentage", trendline = "ols",
title = "Relationship between sale price and number of ratings of iPhones")
figure.show()

figure = px.scatter(data_frame = sharaddata, x = "Number of Ratings",
y = "Sale Price", size = "Sale Price", trendline = "ols",
title = "Relationship between sale price and number of ratings of iPhones")
figure.show()
figure = px.scatter(
    data_frame=sharaddata,
    x="Sale Price",
    y="Number of Ratings",
    size="Discount Percentage",
    trendline="ols",
    title="Relationship between sale price and number of ratings of iPhones"
)

figure.show()













