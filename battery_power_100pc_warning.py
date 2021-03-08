# python script showing battery details 
import psutil
import time
from tkinter import *

battery = psutil.sensors_battery()

while battery.percent > 0:
    if battery.power_plugged == True:
        if battery.percent == 90:
            root = Tk()
            myLabel1 = Label(root, text="Battery Fully Charged!")
            myLabel2 = Label(root, text="Remove Charger!")
            myLabel1.grid(row=0, column=0)
            myLabel2.grid(row=0, column=1)
            root.mainloop()

    time.sleep(1)
    battery = psutil.sensors_battery()
