##get data from db, manipulate it if you want,
## then take output as json or csv 

import sqlite3
import csv
import json
from typing import Dict

mydbConnection=sqlite3.connect("Chinook.db")
myCursor=mydbConnection.execute("""
SELECT Artist.Name, Album.Title FROM Artist 
INNER JOIN Album on Album.ArtistId=Artist.ArtistId
WHERE length(Name)<7 LIMIT 10
""")

queryResult=myCursor.fetchall()


obj_list=[]
for row in queryResult:
    mydict={} #dışarda tanımlanırsa üzerine yazılır (adres ref?) önceki veriler gider.
    print(f"ARTIST: {row[0]} | ALBUM TITLE: {row[1]}")
    mydict["Artist"]=row[0]
    mydict["Album Title"]=row[1]
    obj_list.append(mydict)


def dbToCSV():
    f = open('dbdata.csv', 'a',newline='')
    writer=csv.writer(f)
    writer.writerow(["artist", "album"])
    writer.writerows(queryResult)

def dbToJSON():
    j=json.dumps(obj_list, indent=4)
    with open("dbdata.json", "w") as f:
        f.write(j)

dbToJSON()
dbToCSV()
