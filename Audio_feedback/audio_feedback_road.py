from gpiozero import Button
import array
import urllib
import pyttsx
import os
from time import sleep

START_X =0
START_Y =0
END_X =100
END_Y =100
TOTAL_X_CAP =100
TOTAL_Y_CAP =100
# NUMBER_READOUTS = 5
button_road = Button(23) #need to change the button name for roads
exit = Button (18)
XPin = 0
YPin = 1
placeId = [0,0,0,0,0,0,0,0,0,0]

road = [0,0,0,0,0,0,0,0,0,0]

print ("PROGRAM LOADED!\n")
print ("IP Adress for SSH:")
os.system('hostname -I')
os.system('iwgetid')
os.system('espeak "Welcome to Visually Impaired map by Group 12" 2>/dev/null')

def getRoad():
    points=[]
    while button_road.is_pressed:
        #lat = analogReadFUNCTION(XPin); / TOTAL_X_CAP * (START_X - END_X) + START_X
        #long = analogReadFUNCTION(YPin); / TOTAL_Y_CAP * (START_Y - END_Y) + START_Y
        #pt=[lat, long]
        #points.append(pt)
        #sleep(.300)    #sleep for 300 ms, wait until next input

    #test points - 3 points for latitude and longitude
    points=[[60.170880,24.942795], [60.170879,24.942796],[60.170877,24.942796]]


    #latitude = analogReadFUNCTION(XPin); / TOTAL_X_CAP * (START_X - END_X) + START_X
    #longtitude = analogReadFUNCTION(YPin); / TOTAL_Y_CAP * (START_Y - END_Y) + START_Y

    URL = "https://roads.googleapis.com/v1/api/place/nearestRoads?&key=AIzaSyA3aYU6UKfZkp8QfafB2WCfouPjxVrFx2A&points="
    for pt in points:
        URL=URL+"|"+pt[i][0]+pt[i][1]
    html=urllib.urlopen(URL)
    htmltext=html.read()
    print("DATABASE UPDATED!\n")
    postname = 1

    phrase =  "\"placeId\" : \""
    prename = htmltext.find(phrase,postname)
    postname =  htmltext.find("\"", prename+len(phrase)+1)
    placeId = htmltext[prename+len(phrase):postname]
    print("Place Id: "),
    print(placeId)
    os.system('espeak "{0}" 2>/dev/null'.format(placeId))
    return placeId

while True:

    # we will search here with Google roads, then obtain the place ID and do the place search
    if button_road.is_pressed:

        placeId=getRoad()

        URL = "https://maps.googleapis.com/maps/api/place/details/json?&key=AIzaSyA3aYU6UKfZkp8QfafB2WCfouPjxVrFx2A&placeid="+placeId
        html=urllib.urlopen(URL)
        htmltext=html.read()
        print("DATABASE UPDATED!\n")
        postname = 1
        phrase =  "\"formatted_address\" : \""
        prename = htmltext.find(phrase,postname)
        postname =  htmltext.find("\"", prename+len(phrase)+1)
        road_address = htmltext[prename+len(phrase):postname]
        print("Road name: "),
        print(road_address)
        os.system('espeak "{0}" 2>/dev/null'.format(road_address))


    if exit.is_pressed:
        exit()
