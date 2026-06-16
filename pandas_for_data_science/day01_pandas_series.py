#A Pandas Series is like a column in a table. 

#It is an  1D array which holds data of any type. 

#Here we will create a simple Pandas Series. 

import pandas as pd
Sharad = [1,7,2] 
sharadnew= pd.Series(Sharad)
print(sharadnew)

#Labeling label can use to access a specific label. 

import pandas as pd
Sharad = [1,7,2] 
sharadnew= pd.Series(Sharad)
print(sharadnew[0])

# with Create label, you can create your own labels.

import pandas as pd
Sharad = [1,7,2] 
sharadnew= pd.Series(Sharad, index=["x","y","z"])
print(sharadnew)

#Labeling label can use to access a specified value(after creating own labels).

import pandas as pd
Sharad = [1,7,2] 
sharadnew= pd.Series(Sharad, index=["x","y","z"])
print(sharadnew["x"])

#You can also use a key or value object like a dictionary when creating a series. 

#here we will create a simple Panda series for a dictionary. 

import pandas as pd
cal = {"day1": 420, "day2": 380, "day3": 390}
sharadnew= pd.Series(cal)
print(sharadnew)

#Now we will create a series using only data from day1 and day2.

import pandas as pd
cal = {"day1": 420, "day2": 380, "day3": 390}
result= pd.Series(cal, index=["day1", "day2"])
print(result)

#Dataframe - datasets and Pandari volume, multidimensional tables and they are called dataframes. 

# Series are like columns and dataframe is the whole table. 
 
# We will now create a dataframe from series.

import pandas as pd
sharad = {"cal": [420,380,390], "duration": [50,40,45]}
sharadnew= pd.DataFrame(sharad)
print(sharadnew)






