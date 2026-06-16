#Here we can also replace the empty cell using mean(), median() or mode().

#  we can calculate the mean and replace the empty value with it.

import pandas as pd
sharad = pd.read_csv('dirtydata,csv')
x = sharad["calories"].mean()
sharad["calories"].fillna(x, inplace=True)
print(sharad.to_string())

#Calculate the Median and replace any empty value with it.

import pandas as pd
sharad = pd.read_csv('dirtydata,csv')
x = sharad["calories"].median()
sharad["calories"].fillna(x, inplace=True)
print(sharad.to_string())

#Calculate the Mode and replace the empty cell with it.

import pandas as pd
sharad = pd.read_csv('dirtydata,csv')
x = sharad["calories"].mode()[0]
sharad["calories"].fillna(x, inplace=True)
print(sharad.to_string())

#Data in a wrong format: To fix this problem, there are 2 ways: 

#removing the row or convert all the cells in the same format, 

#loading and reading the original dataframe. 

import pandas as pd
sharad = pd.read_csv('dirtydata,csv')
print(sharad.to_string)

#Now let's try to convert all the data cell in the date column into dates.via to_datetime()

import pandas as pd
sharad = pd.read_csv('dirtydata,csv')
sharad["Date"] = pd.to_datetime(sharad['Date'])
print(sharad.to_string())


