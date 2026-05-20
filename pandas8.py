#Pandas - Cleaning Empty Cells

import pandas as pd
df=pd.read_csv('data4.csv')
new_df=df.dropna()
print(new_df.to_string())


#Example
import pandas as pd

df = pd.read_csv('data4.csv')

df.dropna(inplace = True)

print(df.to_string())


#Replace Empty Values
import pandas as pd
df=pd.read_csv('data4.csv')
df=df.fillna(30)
print(df.to_string())


#Replace Only For Specified Columns
import pandas as pd
df=pd.read_csv('data4.csv')
df=df.fillna({"Marks": 70})
print(df.to_string)

#Replace Using Mean
import pandas as pd
df=pd.read_csv('data4.csv')
x=df["Marks"].mean()
df=df.fillna({"Marks":x})
print(df.to_string)

#Replace Using Median
import pandas as pd
df=pd.read_csv('data4.csv')
x=df["Marks"].median()
df=df.fillna({"Marks":x})
print(df.to_string)

#Replace Using Mode
import pandas as pd
df=pd.read_csv('data4.csv')
x=df["Marks"].mode()[0]
df=df.fillna({"Marks":x})
print(df.to_string)