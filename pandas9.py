#pandas Data Selection 
import pandas as pd
data={
    "name":["Rahul","koushalya","koushik","priya","ravi"],
    "Age":[34,56,78,99,76],
    "Marks":[99,88,77,66,87]

}
df=pd.DataFrame(data)
print(df)

#Select Single Column
import pandas as pd
data={
    "Name":["Rahul","koushalya","koushik","priya","ravi"],
    "Age":[34,56,78,99,76],
    "Marks":[99,88,77,66,87]

}
df=pd.DataFrame(data)
print(df["Name"])

#Select Multiple Columns
import pandas as pd
data={
    "Name":["Rahul","koushalya","koushik","priya","ravi"],
    "Age":[34,56,78,99,76],
    "Marks":[99,88,77,66,87]

}
df=pd.DataFrame(data)
print(df[["Name","Marks"]])

#Select One Row using loc
import pandas as pd
data={
    "Name":["Rahul","koushalya","koushik","priya","ravi"],
    "Age":[34,56,78,99,76],
    "Marks":[99,88,77,66,87]

}
df=pd.DataFrame(data)
print(df.loc[2])

#Select Multiple Rows
import pandas as pd
data={
    "Name":["Rahul","koushalya","koushik","priya","ravi"],
    "Age":[34,56,78,99,76],
    "Marks":[99,88,77,66,87]

}
df=pd.DataFrame(data)
print(df.loc[[1,2]])


#Select Rows and Columns Together
import pandas as pd
data={
    "Name":["Rahul","koushalya","koushik","priya","ravi"],
    "Age":[34,56,78,99,76],
    "Marks":[99,88,77,66,87]

}
df=pd.DataFrame(data)
print(df.loc[1:3,["Name","Marks"]])