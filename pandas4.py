#Pandas - Analyzing DataFrames
import pandas as pd
df=pd.read_csv("data1.csv")
print(df.head(10))

#example
import pandas as pd
df=pd.read_csv("data1.csv")
print(df.head())

#tail
import pandas as pd
df=pd.read_csv("data1.csv")
print(df.tail(5))
print(len(df))

#Info About the Data
import pandas as pd
df=pd.read_csv("data1.csv")
print(df.info())


