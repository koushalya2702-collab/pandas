#selecting data in pandas
import pandas as pd
data={
    "Name":["A","B","C","D"],
    "Age":[25,78,91,23],
    "Marks":[78,98,88,90]
}
df=pd.DataFrame(data)
print(df)

#select column
import pandas as pd
data={
    "Name":["A","B","C","D"],
    "Age":[25,78,91,23],
    "Marks":[78,98,88,90]
}
df=pd.DataFrame(data)
print(df["Name"])

#selecting multiple columnns
import pandas as pd
data={
    "Name":["A","B","C","D"],
    "Age":[25,78,91,23],
    "Marks":[78,98,88,90]
}
df=pd.DataFrame(data)
print(df[["Name","Marks"]])

#select rows using index
import pandas as pd
data={
    "Name":["A","B","C","D"],
    "Age":[25,78,91,23],
    "Marks":[78,98,88,90]
}
df=pd.DataFrame(data)
print(df.iloc[0])

#example
import pandas as pd
data={
    "Name":["A","B","C","D"],
    "Age":[25,78,91,23],
    "Marks":[78,98,88,90]
}
df=pd.DataFrame(data)
print(df.iloc[0:3])

#select rows using label
import pandas as pd
data={
    "Name":["A","B","C","D"],
    "Age":[25,78,91,23],
    "Marks":[78,98,88,90]
}
df=pd.DataFrame(data)
print(df.loc[0:1])

#Filtering data
import pandas as pd

data={
    "Name":["A","B","C","D"],
    "Age":[25,78,91,23],
    "Marks":[78,98,88,90]
}
df=pd.DataFrame(data)
print(df["Age"]>25)

#multiple conditions
import pandas as pd

data={
    "Name":["A","B","C","D"],
    "Age":[25,78,91,23],
    "Marks":[78,98,88,90]
}
df=pd.DataFrame(data)
print(df[(df["Age"]>20) & (df["Marks"]>80)])

#select specific columns after filtering
import pandas as pd

data={
    "Name":["A","B","C","D"],
    "Age":[25,78,91,23],
    "Marks":[78,98,88,90]
}
df=pd.DataFrame(data)
print(df[df["Marks"]>70] [["Name","Marks"]])


#using isin()
import pandas as pd

data={
    "Name":["A","B","C","D"],
    "Age":[25,78,91,23],
    "Marks":[78,98,88,90]
}
df=pd.DataFrame(data)
print(df[df["Name"].isin(["A","D"])])


#using not
import pandas as pd

data={
    "Name":["A","B","C","D"],
    "Age":[25,78,91,23],
    "Marks":[78,98,88,90]
}
df=pd.DataFrame(data)
print(df[~(df["Age"]>25)])


#query method
import pandas as pd

data={
    "Name":["A","B","C","D"],
    "Age":[25,78,91,23],
    "Marks":[78,98,88,90]
}
df=pd.DataFrame(data)
print(df.query("Age>25 and Marks>70"))
