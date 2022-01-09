import pandas

data=pandas.read_csv("Day25\weather_data.csv")
# print(data.day)
# print(data.day=="Monday")
# print("------------------")
# print(data[data.day=="Monday"])
# print("------------------")
# print(data.iloc[1])
hottestday=data[data.temp==data.temp.max()].day
hottestemp=data[data.temp==data.temp.max()].temp
print(str(hottestday))
print(hottestemp)
