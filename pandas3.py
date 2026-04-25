#Load Files Into a DataFrame
import pandas as pd

df = pd.read_csv('data.csv')

print(df)

#example
import pandas as pd

df = pd.read_csv('data1.csv')

print(df.to_string()) 

#max_rows
import pandas as pdom

pd.options.display.max_rows = 9999

df = pd.read_csv('data1.csv')

print(df)

#create excel file using pandas
import pandas as pd
data={
    "name":["koushalya","rahul","pranith"],
    "age":[15,89,45],
    "marks":[77,99,89]
}
df=pd.DataFrame(data)
df.to_excel("studenst.xlsx",index=False)
new_df=pd.read_excel("students.xlsx")
print(new_df)