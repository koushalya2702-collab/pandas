#Pandas Series

import pandas as pd
a=[1,2,3]
myvar=pd.Series(a)
print(myvar)

#Labels
import pandas as pd
a=[1,2,3,4]
myvar=pd.Series(a,index=["x","y","z","k"])
print(myvar)
print(myvar["y"])

#Key/Value Objects as Series
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

#example

import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)
