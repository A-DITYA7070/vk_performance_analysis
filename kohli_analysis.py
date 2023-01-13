import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Virat_Kohli.csv")

# total no of runs kohli scored
# total no of balls he has faced
# avg sr of kohli

# runs=df["Runs"]

# sum=np.sum(runs)


# balls=df["BF"]
# ball_sum=np.sum(balls)
# print(ball_sum)


# avg_Sr=df["SR"]
# avg=np.sum(avg_Sr)
# print(avg/132)
# print(sum)
# print("Total runs : ",df["Runs"].sum())
# print("Total Balls faced : ",df["BF"].sum())
# print("avg sr ",df["SR"].mean())

#1. no of matches vk has playes at diff positions..
#2. total runs scored in diff positions..
#3. total sixes scored in diff positions..
#4. no of tons scored by vk in first and sec innings
#5. cal the dissmissals of kohli..
#6 against which team he has scored the most runs..
#7 against which team he has scored the most centuries..
#8 runs scored by him ans 6's played..

#1. 
positions = df["Pos"].unique()
# print(positions)
df["Pos"] = df["Pos"].map({
    3.0 : "Batting at 3",
    4.0 : "Batting at 4",
    5.0 : "Batting at 5",
    6.0 : "Batting at 6",
    7.0 : "Batting at 7",
    1.0 : "Batting at 1",
    2.0 : "Batting at 2"
})
# print(df[["Runs","Pos"]])

# pos_counts = df["Pos"].value_counts()
# # print(pos_counts,type(pos_counts))
# # printing pie-chart..
# pos_counts_values = pos_counts.values
# pos_counts_labels = pos_counts.index

# fig = plt.figure(figsize=(10,7))
# plt.pie(pos_counts_values,labels=pos_counts_labels)
# plt.title("Total match played by Kohli batting at different positions..")
# plt.show()

# six_count = df["6s"].value_counts()
# fig = plt.figure(figsize=(10,7))
# plt.pie(six_count,labels=positions)
# plt.show()

# def show_pie_plots(df,key):
#     counts=df[key].value_counts()
#     count_values=counts.values
#     count_labels=counts.index
#     fig=plt.figure(figsize=(10,10))
#     plt.pie(count_values,labels=count_labels)
#     # plt.show()
# No of matches played at diff positions..
# show_pie_plots(df,"Opposition")

# No of matches played at diff grounds..
# show_pie_plots(df,"Ground")

# runs_at_pos = df.groupby("Pos")['6s'].sum()
# print(runs_at_pos,type(runs_at_pos))
# fig=plt.figure(figsize=(10,7))

# runs_at_pos_values = runs_at_pos.values
# runs_at_pos_labels = runs_at_pos.index
# # plt.pie(runs_at_pos_values,labels=runs_at_pos_labels)
# # plt.show()
# plt.bar(
#     runs_at_pos_labels,
#     runs_at_pos_values,
#     color="red",
#     width=0.3
# )
# plt.show()

# runs_scored=df.groupby("Opposition")["Runs"].sum()
# print("runs scored at diff pos ")
# fig=plt.figure(figsize=(10,7))
# runs_at_pos_values=runs_scored.values
# runs_at_pos_labels=runs_scored.index
# plt.bar(
#     runs_at_pos_labels,
#     runs_at_pos_values,
#     color="black",
#     width=0.5
# )
# plt.show()

def Total_at_pos(df,key):
    runs_scored=df.groupby("Pos")[key].sum()
    print("runs scored at diff pos ")
    fig=plt.figure(figsize=(10,7))
    runs_at_pos_values=runs_scored.values
    runs_at_pos_labels=runs_scored.index
    plt.bar(
        runs_at_pos_labels,
        runs_at_pos_values,
        color="black",
        width=0.5
    )
    plt.show()
    
# Total_at_pos(df,"Dismissal")
# print(df)
# Total_at_pos(df,"Dismissal")

#4. no of tons scored by vk in first and sec innings
centuries = df.query("Runs >= 100")
# print(centuries)

innings = centuries["Inns"].value_counts()
plt.pie(innings.values,labels=innings.index)
plt.show()

# tons = centuries["Runs"]
# plt.bar(innings,tons,width=0.3,color="red")
# plt.show()

# 9.cal dismissals of kohli.


# print(df)