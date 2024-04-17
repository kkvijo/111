# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("C:\\Users\\CLUE\\Desktop\\nba.csv", index_col="Name")

# retrieving row by loc method
first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]

print(first, "\n\n\n", second)



# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("C:\\Users\\CLUE\\Desktop\\nba.csv", index_col="Name")

# retrieving columns by indexing operator
first = data["Age"]

print(first)

