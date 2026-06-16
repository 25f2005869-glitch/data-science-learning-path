#Read CSV file:

#csv = comma-separated file. 

#It is a simple way to store the big and biggest datasets. 

#CSV files contain plain text. 

#Loading the CSV into a data frame with to_string

import pandas as pd
df = pd.read_csv('data.csv')
print(df.to_string())

#Loading the CSV into a data frame without two strings. 

import pandas as pd
df = pd.read_csv('data.csv')
print(df)

# Max_rows- you can check your system's maximum row width.

import pandas as pd
print(pd.options.display.max_rows)

#Here, so we can increase the maximum number of rows to display the entire data frame.

import pandas as pd
pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
print(df)