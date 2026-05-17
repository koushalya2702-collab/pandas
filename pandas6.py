#Pandas - Cleaning Data
#Remove Rows

import pandas as pd
data={
    "Name":["A","B","C","D"],
    "Marks":[90,None,80,None]
}
df=pd.DataFrame(data)
df2=df.dropna()
print(df2)

#example

import pandas as pd

data={
    "Name":["A","B","C","D"],
    "Marks":[90,None,80,None]
}
df=pd.DataFrame(data)
df2=df.dropna(inplace=True)
print(df2)

#fillna
import pandas as pd

data={
    "Name":["A","B","C","D"],
    "Marks":[90,None,80,None]
}
df=pd.DataFrame(data)
df.fillna({"Marks":99},inplace=True)
print(df)


