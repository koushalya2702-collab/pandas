#Pandas Merging and Joining
import pandas as pd
students=pd.DataFrame({
    "ID":[1,2,3],
    "Name":["koushalya","Anu","kavitha"]
})
marks=pd.DataFrame({
    "ID":[1,2,3],
    "Marks":[78,45,96]
})
result=pd.merge(students,marks,on="ID")
print(result)

#Inner Merge
students=pd.DataFrame({
    "ID":[1,2,3],
    "Name":["koushalya","kavya","harshita"]
})
marks=pd.DataFrame({
    "ID":[1,2],
    "Marks":[99,88]
})
result=pd.merge(students,marks,on="ID",how="inner")
print(result)

#Left Merge
students=pd.DataFrame({
    "ID":[1,2,3],
    "Name":["koushalya","kavya","harshita"]
})
marks=pd.DataFrame({
    "ID":[1,2],
    "Marks":[99,88]
})
result=pd.merge(students,marks,on="ID",how="left")
print(result)


#Right Merge
students=pd.DataFrame({
    "ID":[1,2,3],
    "Name":["koushalya","kavya","harshita"]
})
marks=pd.DataFrame({
    "ID":[1,2],
    "Marks":[99,88]
})
result=pd.merge(students,marks,on="ID",how="right")
print(result)


#Outer Merge

students=pd.DataFrame({
    "ID":[1,2,3],
    "Name":["koushalya","kavya","harshita"]
})
marks=pd.DataFrame({
    "ID":[1,2],
    "Marks":[99,88]
})
result=pd.merge(students,marks,on="ID",how="outer")
print(result)

#Joining in Pandas
students=pd.DataFrame({
    "Name":["Koushalya","priya","navya"]
},index=[1,2,3])
marks=pd.DataFrame({
    "Marks":[58,99,89]
},index=[1,2,3])
result=students.join(marks)
print(result)