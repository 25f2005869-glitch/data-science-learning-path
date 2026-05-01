#Data frame - it is a two-dimensional data structure like an  2D array with a 
# 
#table that includes rows and columns.

import pandas as pd
data = {"cal": [420, 380, 390], "dur":[50, 40, 45]}
sharad = pd.DataFrame(data)
print(sharad)

#Locate row, Panda use the lock attribute to return one or more specific row.

import pandas as pd
data = {"cal": [420, 380, 390], "dur":[50, 40, 45]}
sharad = pd.DataFrame(data)
print(sharad.loc[0])

#Example of returning row  0 and 1

import pandas as pd
data = {"cal": [420, 380, 390], "dur":[50, 40, 45]}
sharad = pd.DataFrame(data)
print(sharad.loc[[0,1]])

#Named index: With the index argument, you can name your own index.

import pandas as pd
data = {"cal": [420, 380, 390], "dur":[50, 40, 45]}
sharad = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(sharad)

#Locate the named index 

import pandas as pd
data = {"cal": [420, 380, 390], "dur":[50, 40, 45]}
sharad = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(sharad.loc[ "day2"])

#output in a data frame.

import pandas as pd
data = {"cal": [420, 380, 390], "dur":[50, 40, 45]}
sharad = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(sharad.loc[["day1", "day2"]])

#Load the data from the CSV file into DataFrame i.e. data csv. 

import pandas as pd
fileload = pd.read_csv('data.csv')
print(fileload)


