#You can also remove the rows for wrong data in larger datasets.

import pandas as pd
sharad = pd.read_csv('dirtydata,csv')
for i in sharad.index:
    if sharad.loc[i, "Duration"] > 120:
        sharad.drop(i, inplace=True)
print(sharad.to_string())

#Removing the duplicate value:

#you need to discover the duplicate values via duplicated() method. 

#Loading and reading the original dataframe 

import pandas as pd
sharad = pd.read_csv('dirtydata,csv')
print(sharad.to_string())

#returns true for every row that is duplicate, 
# otherwise returns false.

import pandas as pd
sharad = pd.read_csv('dirtydata,csv')
print(sharad.duplicated())

#Removing the duplicate from the dataset via drop_duplicates().

import pandas as pd
sharad = pd.read_csv('dirtydata,csv')
sharad.drop_duplicates(inplace=True)
print(sharad.to_string())





