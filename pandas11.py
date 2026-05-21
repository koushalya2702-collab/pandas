#pandas data transformation

#Example Dataset
import pandas as pd

data = {
    "Name": ["Rahul", "Anu", "Kiran", "Priya"],
    "Age": [21, 19, 22, 20],
    "Marks": [78, 45, 92, 67]
}

df = pd.DataFrame(data)

print(df)

#Creating New Column
import pandas as pd

data = {
    "Name": ["Rahul", "Anu", "Kiran", "Priya"],
    "Age": [21, 19, 22, 20],
    "Marks": [78, 45, 92, 67]
}

df = pd.DataFrame(data)
df["Bonus"]=df["Marks"]+5
print(df)

#Using apply() Function
import pandas as pd

data = {
    "Name": ["Rahul", "Anu", "Kiran", "Priya"],
    "Age": [21, 19, 22, 20],
    "Marks": [78, 45, 92, 67]
}

df = pd.DataFrame(data)
def result(marks):
    if marks >=50:
        return "Pass"
    else:
        return "Fail"
df["Result"]=df["Marks"].apply(result)
print(df)

# Transform Text Data Convert Names to Uppercase
import pandas as pd

data = {
    "Name": ["Rahul", "Anu", "Kiran", "Priya"],
    "Age": [21, 19, 22, 20],
    "Marks": [78, 45, 92, 67]
}

df = pd.DataFrame(data)
df["Name"]=df["Name"].str.upper()
print(df)

#Change Data Type

import pandas as pd

data = {
    "Name": ["Rahul", "Anu", "Kiran", "Priya"],
    "Age": [21, 19, 22, 20],
    "Marks": [78, 45, 92, 67]
}

df = pd.DataFrame(data)
df["Age"] = df["Age"].astype(float)

print(df.dtypes)


#Using map()
import pandas as pd

data = {
    "Name": ["Rahul", "Anu", "Kiran", "Priya"],
    "Age": [21, 19, 22, 20],
    "Marks": [78, 45, 92, 67]
}

df = pd.DataFrame(data)
grades={
    78:"B",
    45:"F",
    92:"A",
    67:"C"
}
df["Grades"]=df["Marks"].map(grades)
print(df)

# #Using replace()

# import pandas as pd

# data = {
#     "Name": ["Rahul", "Anu", "Kiran", "Priya"],
#     "Age": [21, 19, 22, 20],
#     "Marks": [78, 45, 92, 67]
# }

# df = pd.DataFrame(data)
# def result(marks):
#     if marks >=50:
#         return "Pass"
#     else:
#         return "Fail"
# df["Result"]=df["Result"].replace({
#     "Pass":"P",
#     "Fail":"F"
# })
# print(df)

#Sorting Data
import pandas as pd

data = {
    "Name": ["Rahul", "Anu", "Kiran", "Priya"],
    "Age": [21, 19, 22, 20],
    "Marks": [78, 45, 92, 67]
}

df = pd.DataFrame(data)
df=df.sort_values(by="Marks")
print(df)