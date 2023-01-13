import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv("Virat_Kohli.csv")
# print(df)
# print(df.head(10))
# print(df.tail(10))
# df.info()
# print(df.shape)
# print(df.describe())
# print(df["Opposition"].min())
# print(df["Opposition"]=="v Australia")
# vs_aussies=df[df["Opposition"]=="v Australia"]
# print(vs_aussies)

# virat_century=df[df["Runs"]>=100 ]

# print(virat_century)

# sril_cent=df[
#     (df["Opposition"]=="v Sri Lanka") & (df["Runs"]>=100)
# ]
# print(sril_cent)

# sr=df[df["SR"]>=100]
# print(sr)

# def find_centuries(x):
#     if x>=100:
#         return "OG"
#     else:
#         return "NOOB"

# df["Centuries"]=df["Runs"].apply(find_centuries)
# print(df.tail(10))

# total_score=df["Runs"].sum()
# print("totals runs of virat kholi:",total_score)

# print("Total balls faced:",df["BF"].sum())

# print("Average strike rate:",df["SR"].mean())



# # #number of matches he has played at different position
print(df["Pos"].head(10))


possitions=df["Pos"].unique()
print(possitions)


df["Pos"]=df["Pos"].map({
    3.0:"Batting at 3",
    4.0:"Batting at 4",
    2.0:"Batting at 2",
    1.0:"Batting at 1",
    7.0:"Batting at 7",
    6.0:"Batting at 6",
    5.0:"Batting at 5"
})

# print(df[["Runs","Pos"]])
pos_counts=df["Pos"].value_counts()
print(pos_counts)
print(type(pos_counts))




# #total runs in different position

pos_counts_values=pos_counts.values
pos_counts_lables=pos_counts.index

fig=plt.figure(figsize=(10,7))

plt.pie(pos_counts_values, labels=pos_counts_lables)

plt.show()

#total six in different position
def show_pie_plots(df,key):
    counts=df[key].value_counts()
    count_values=counts.values
    count_lables=counts.index
    fig=plt.figure(figsize=(10,7))
    plt.pie(count_values, labels=count_lables)
    plt.show()





#total runs in different position
# show_pie_plots(df,"Opposition")
#different ground
# show_pie_plots(df,"Ground")
#total sixs in different position

run_at_pos=df.groupby("Pos")["6s"].sum()
print(run_at_pos,type(run_at_pos))
run_at_pos_values=run_at_pos.values
run_at_pos_labels=run_at_pos.index

plt.bar(
    run_at_pos_labels,
    run_at_pos_values,
    color="green",
    width=0.3
)
plt.show()

#total runs with different countries
runs_with_countries=df.groupby("Opposition")["Runs"].sum()
runs_with_countries_values=runs_with_countries.values
runs_with_countries_lables=runs_with_countries.index

plt.bar(
    runs_with_countries_lables,
    runs_with_countries_values,
    color="red",
    width=0.3
)
plt.show()

# number of centuries scored by him in 1st and 2 innings
cuentries=df.query("Runs >= 100")
print(cuentries)
innings=cuentries["Inns"].value_counts()
plt.pie(innings.values, labels=innings.index)
plt.show()




#against which teams he has scored the most