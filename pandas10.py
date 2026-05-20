#Pandas data filtering

import pandas as pd
data={
    "Name":["Rahul","koushalya","koushik","priya","ravi"],
    "Age":[34,56,78,99,76],
    "Marks":[99,88,77,66,87]

}
df=pd.DataFrame(data)
print(df[df["Marks"]>80])

# Equal Condition

import pandas as pd
data={
    "Name":["Rahul","koushalya","koushik","priya","ravi"],
    "Age":[34,56,78,99,76],
    "Marks":[99,88,77,66,87]

}
df=pd.DataFrame(data)
print(df[df["Age"]==78])

#Multiple Conditions using AND
import pandas as pd
data={
    "Name":["Rahul","koushalya","koushik","priya","ravi"],
    "Age":[34,56,78,99,76],
    "Marks":[99,88,77,66,87]

}
df=pd.DataFrame(data)
print(df[(df["Marks"] > 80) & (df["Age"] < 80)])

#Multiple Conditions using OR |
import pandas as pd
data={
    "Name":["Rahul","koushalya","koushik","priya","ravi"],
    "Age":[34,56,78,99,76],
    "Marks":[99,88,77,66,87]

}
df=pd.DataFrame(data)
print(df[(df["Marks"] > 80) | (df["Age"] < 23)])
