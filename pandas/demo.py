import pandas as pd 
"""
data = [100,102,104,200,202]

series = pd.Series(data, index = ["a","b","c","d","e"])

print(series)

# loc is location by lable

series.loc["c"] = 200
print(series.loc["a"] , series.loc["b"],series.loc["c"])

#iloc integer location - > like index 

print(series.iloc[0])

print(series[series < 200])


calories = {"Day 1 " : 1750, "Day 2":2100, "Day 3" :1700}

series = pd.Series(calories)

series.loc["Day 3"] += 550

print (series[series >=2000])



#data frame

data = {"Name":["Moni","sam","vishal"] ,
        "Age":[30,35,30]}

df = pd.DataFrame(data,index = ["emp1","emp2","emp3"])

#print(df.loc["emp1"])

#add a new column 
df["job"]=["cook","N/A","Cashier"]

#add a new row 
new_row = pd.DataFrame([{"Name":"Sandy","Age":30,"Job":"Engineer"}],index=["emp4"])

df = pd.concat([df,new_row])

print(df)


print(df)

print(df.to_string())

#selection by column 
print(df["Name"])
print(df[["Name","Height"]])
"""
df = pd.read_csv("data.csv",index_col="Name")

#selection by rows 
print(df.loc["Dragonair"])
 