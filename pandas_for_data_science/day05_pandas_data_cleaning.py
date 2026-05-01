#Cleaning data - it means fixing the bad data in your dataset. 

#Bad data could be empty cell, data in a wrong format, duplicate data, and wrong data. 

#Empty cell, it will give you a wrong result always. 

#We will have to remove the rows always that contain the bad data. 

#Loading and reading the original data frame.
 

import pandas as pd
sharad = pd.read_csv('dirtydata,csv')
print(sharad.to_string)

#here we will return a new data frame with no empty cell.

import pandas as pd
sharad = pd.read_csv('dirtydata,csv')
sharadnew = sharad.dropna()
print(sharadnew.to_string())

#If at any case you want to change the original data frame, then use the inplace=True argument. 

# It will remove the row containing the NULL(NaN) values.

import pandas as pd
sharad = pd.read_csv('dirtydata,csv')
sharad.dropna(inplace=True)
print(sharad.to_string())

#Replacing the empty value, we will use the fillna() method, 

# which will allow us to replace the empty cell with the value.

import pandas as pd
sharad = pd.read_csv('dirtydata,csv')
sharad.fillna(130, inplace=True)
print(sharad.to_string())

#To replace only the empty value for one column, you need to specify the column name.

import pandas as pd
sharad = pd.read_csv('dirtydata,csv')
sharad["calories"].fillna(130, inplace=True)
print(sharad.to_string())






