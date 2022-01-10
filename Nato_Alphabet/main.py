import pandas
from pandas.core.frame import DataFrame
from pandas.io.parsers import read_csv
df=DataFrame()
df=read_csv("nato_phonetic_alphabet.csv")


##way1
mydict={row["letter"]:row["code"] for (index,row) in df.iterrows()} #mine


##way2
mydict2={row.letter:row.code for (index,row) in df.iterrows()}


##way3
test=dict(zip(df.letter,df.code))
print(test)

##way4
test2={df.letter:df.code for (df.letter,df.code) in df}

print(test2)
