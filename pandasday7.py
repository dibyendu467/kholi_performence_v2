import pandas as pd

data={
    "apples":[4,3,6,1],
    "oranges":[5,4,7,2]
}

index_titles=[
    "Aaron","Shaun","James","wilson"
]


df=pd.DataFrame(data,index=index_titles)
# print(df.loc["Aaron"])
print(df["apples"].iloc[1:])
# print (df)
print(type(df))