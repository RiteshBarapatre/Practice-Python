import time
from plyer import notification

while True:
    notification.notify(title = "Please Drink Water Now !!",
        message = "Drinking water is good for our health.",
        app_icon = "C:\Practice Programmes\icon.ico", #This the location of icon file
        timeout = 5 #Notification will appear for 5 sec 
    )
    time.sleep(60*60) #This line tell the notification to go sleep for 3600 sec

#If we want to work this programme in background 
#Write pythonw .\(file name)
