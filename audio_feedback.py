from gpiozero import Button
import array
import urllib
import pyttsx
import os

START_X =0
START_Y =0
END_X =100
END_Y =100
TOTAL_X_CAP =100
TOTAL_Y_CAP =100
NUMBER_READOUTS = 5
button = Button(23)
exit = Button (18)
XPin = 0
YPin = 1
name = [0,0,0,0,0,0,0,0,0,0]

print ("PROGRAM LOADED!\n")
print ("IP Adress for SSH:")
os.system('hostname -I')
os.system('iwgetid')
os.system('espeak "Welcome to V I map by Group 12" 2>/dev/null')


while True:
    if button.is_pressed:
        #latitude = analogReadFUNCTION(XPin); / TOTAL_X_CAP * (START_X - END_X) + START_X
        latitude = 51.4984856
        #longtitude = analogReadFUNCTION(YPin); / TOTAL_Y_CAP * (START_Y - END_Y) + START_Y
        longtitude = -0.1750946
        URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?radius=100&rankby=prominence&key=AIzaSyA3aYU6UKfZkp8QfafB2WCfouPjxVrFx2A&locatio$
        html=urllib.urlopen(URL)
        htmltext=html.read()
        #htmltext = "TEST\"name\" : \"Imperial College London\",TESTTEST\"name\" : \"Museum\",TESTTEST\"name\" : \"NATAAAA\",TEST"
        print("DATABASE UPDATED!\n")
        postname = 1
        os.system('espeak "Top{0}places nearby are" 2>/dev/null'.format(NUMBER_READOUTS))
        for i in range(NUMBER_READOUTS):
            phrase =  "\"name\" : \""
            prename = htmltext.find(phrase,postname)
            postname =  htmltext.find("\"", prename+len(phrase)+1)
            name[i] = htmltext[prename+len(phrase):postname]
            print(i+1),
            print(": "),
            print(name[i])
            os.system('espeak "{0}" 2>/dev/null'.format(name[i]))
    if exit.is_pressed:
        exit()
