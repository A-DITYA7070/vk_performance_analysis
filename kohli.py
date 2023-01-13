import pandas as pd

df = pd.read_csv("Virat_Kohli.csv")
# print(df.head(10)) first 10 values
# print(df.tail(10)) last 10 values

# df.info() gives info about the csv files
# print(df.shape)
# print(df.describe()) Describes the dataset of the table ...
# print(df["Opposition"].describe())
# print(df["BF"].describe())

# run_frequency = df["Opposition"].value_counts()

# print(run_frequency)

# run_freq=df["Runs"].value_counts()
# print(run_freq)

# new_df = df[["Runs","SR","Opposition"]]
# print(new_df)

# conditional selection

# vs_kangro = df[df["Opposition"]=="v Australia"]
# print(vs_kangro)


# find all the matches where vk scored century
# find all matches where vk sr was > 100
#find all matches where vk played with srilanka and scored a century

# matches = df[df["Runs"]>=100]
# print(matches)

# matches2 = df[df["SR"]>=100]
# print(matches2)

# matches3=df[(df["Opposition"]=="v Sri Lanka") & (df["Runs"] >= 100)]

# print(matches3)

def find_centuries(x):
    if x>=100:
        return "OG"
    else:
        return "NOOB"
    pass

df["Centuries"]=df["Runs"].apply(find_centuries)
print(df.tail(10))
print(df)




















