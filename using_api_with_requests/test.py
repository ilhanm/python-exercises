import requests
from tkinter import *

def getLocation():
    res=requests.get("http://api.open-notify.org/iss-now.json")
    position=res.json()["iss_position"]
    position={key:float(val) for (key,val) in position.items()}
    latlabel.configure(text=f"latitude: {position['latitude']}")
    lnglabel.configure(text=f"longitude: {position['longitude']}")
window=Tk()
canvas=Canvas(width=410,height=400)
window.maxsize(400,600)
backgroundImg=PhotoImage(file="using_api_with_requests\issimage.png")
canvas.create_image(200,200,image=backgroundImg)
#quote_text = canvas.create_text(100, 100, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
#canvas.itemconfig(quote_text, text="hahah")
canvas.grid(row=7,column=0)
window.configure(bg="black")
window.geometry("400x600")
infolabel=Label(text="Where is ISS NOW?\n This program gets lat/long value and shows you where ISS is. ")
infolabel.configure(width=60)
infolabel.grid(row=0,column=0)
latlabel=Label(text="latitude: ",font="Helvetica",fg="silver",bg="black")
latlabel.grid(row=1,column=0)
lnglabel=Label(text="longitude: ",font="Imperial",fg="silver", bg="black")
lnglabel.grid(row=3,column=0)
getCoordButton=Button(text="Click",bg="beige",fg="black",command=getLocation)
getCoordButton.grid(row=4,column=0)






window.mainloop()