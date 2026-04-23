#DataFrames
import pandas as pd
data={
    "calories":[420,380,390],
    "duration":[50,40,45]
}
myvar=pd.DataFrame(data)
print(myvar)

#Locate Row
import pandas as pd
data={
    "calories":[420,380,390],
    "duration":[50,40,45]
}
myvar=pd.DataFrame(data)
print(myvar.loc[[0]])

#example
import pandas as pd
data={
    "calories":[420,380,390],
    "duration":[50,40,45]         
}
myvar=pd.DataFrame(data)
print(myvar.loc[[0,1]])


#Named Indexes
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 


#example
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])


print(df.loc["day2"])