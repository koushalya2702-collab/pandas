#Grouping and Aggregation in Pandas
import pandas as pd

data = {
    "Name": ["Rahul", "Anu", "Kiran", "Priya", "Ravi", "Sneha"],
    "Department": ["CS", "AI", "CS", "AI", "CS", "AI"],
    "Marks": [78, 45, 92, 67, 88, 95]
}

df = pd.DataFrame(data)
grouped=df.groupby("Department")
print(grouped["Marks"].mean())

#Sum (sum())

import pandas as pd

data = {
    "Name": ["Rahul", "Anu", "Kiran", "Priya", "Ravi", "Sneha"],
    "Department": ["CS", "AI", "CS", "AI", "CS", "AI"],
    "Marks": [78, 45, 92, 67, 88, 95]
}

df = pd.DataFrame(data)
grouped=df.groupby("Department")
print(grouped["Marks"].sum())

#Count (count())
import pandas as pd

data = {
    "Name": ["Rahul", "Anu", "Kiran", "Priya", "Ravi", "Sneha"],
    "Department": ["CS", "AI", "CS", "AI", "CS", "AI"],
    "Marks": [78, 45, 92, 67, 88, 95]
}

df = pd.DataFrame(data)
grouped=df.groupby("Department")
print(grouped["Marks"].count())


#Maximum (max())
import pandas as pd

data = {
    "Name": ["Rahul", "Anu", "Kiran", "Priya", "Ravi", "Sneha"],
    "Department": ["CS", "AI", "CS", "AI", "CS", "AI"],
    "Marks": [78, 45, 92, 67, 88, 95]
}

df = pd.DataFrame(data)
grouped=df.groupby("Department")
print(grouped["Marks"].max())

#Min()
import pandas as pd

data = {
    "Name": ["Rahul", "Anu", "Kiran", "Priya", "Ravi", "Sneha"],
    "Department": ["CS", "AI", "CS", "AI", "CS", "AI"],
    "Marks": [78, 45, 92, 67, 88, 95]
}

df = pd.DataFrame(data)
grouped=df.groupby("Department")
print(grouped["Marks"].min())


#Multiple Aggregations Together
import pandas as pd

data = {
    "Name": ["Rahul", "Anu", "Kiran", "Priya", "Ravi", "Sneha"],
    "Department": ["CS", "AI", "CS", "AI", "CS", "AI"],
    "Marks": [78, 45, 92, 67, 88, 95]
}

df = pd.DataFrame(data)
print(df.groupby("Department")["Marks"].agg(["mean","sum","max","min","count"]))