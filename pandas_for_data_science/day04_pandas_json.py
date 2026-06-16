#JSON big datasets are normally stored and extracted as JSON.

#JSON is a plain text, but it has a format of an object. 

#Loading the JSON into a data frame 

import pandas as pd
sharad = pd.read_json('data.js')
print(sharad.to_string())

#dictionary as JSON, if your JSON: code is not in a file but in a Python dictionary, 

#then you can do all below:

#Viewing the data - one of the most used methods 

#for a quick overview of the data frame is the head() method. 

#This method returns the headers and a specified number of rows. 

#Here we will print the 10 rows in the data frame. 

import pandas as pd
sharad = pd.read_csv('data.csv')
print(sharad.head(10))

#Here we will print the last 10 rows in the data frame.

import pandas as pd
sharad = pd.read_csv('data.csv')
print(sharad.tail(10))

#What if you want the information about the data in the data frame: via info()

import pandas as pd
df = pd.read_csv('data.csv')
print(df.info())





