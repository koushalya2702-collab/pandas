#Read CSV Files
import pandas as pd
df=pd.read_csv('data3.csv')
print(df)

#Pandas Read CSV
import pandas as pd
df=pd.read_csv('data3.csv')
print(df.to_string())

#max_rows
import pandas as pd
pd.options.display.max_rows=168
df=pd.read_csv('data3.csv')
print(df)

#Viewing the Data

import pandas as pd
df=pd.read_csv('data3.csv')
print(df.head(10))

#Example

import pandas as pd
df=pd.read_csv('data3.csv')
print(df.head())

#Example

import pandas as pd
df=pd.read_csv('data3.csv')
print(df.tail())

#Example

import pandas as pd
df=pd.read_csv('data3.csv')
print(df.info())



#Example

import pandas as pd
df=pd.read_csv('data3.csv')
print(df.describe())

