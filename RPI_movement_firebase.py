import RPi.GPIO as GPIO
import schedule
import pyrebase
import os
import time

config = {
  "apiKey": "AIzaSyAm-Xm1MjDWTspvJ0gp3XJkhF7A7Zt7ayw",
  "authDomain": "surveillance-d050d.firebaseapp.com",
  "projectId": "surveillance-d050d",
  "storageBucket": "surveillance-d050d.appspot.com",
  "messagingSenderId": "208971016355",
  "appId": "1:208971016355:web:7b4667e0d9046bac177716",
  "measurementId": "G-KK27ZJQCTV",
  "databaseURL" : "https://surveillance-d050d-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
db = firebase.database()

IR = 8
temp = 1
print("Connecting...")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(IR,GPIO.IN)
t = time.localtime()
name = 'image'

def MovementAlertsec():
  t = time.localtime()
  x = time.strftime("%H:%M:%S", t)
  os.system(('fswebcam images/{}{}.jpg -S 20'.format(name,x)))
  path_on_cloud = "User/{0}{1}".format(name,x)
  local_path = "images/{0}{1}.jpg".format(name,x)
  storage.child(path_on_cloud).put(local_path)
  url = storage.child(path_on_cloud).get_url(None)
  db.child("Piimage").push(url)

def MovementAlert():
  t = time.localtime()
  x = time.strftime("%H:%M:%S", t)
  os.system(('fswebcam images/{}{}.jpg -S 20'.format(name,x)))
  path_on_cloud = "User/{0}{1}".format(name,x)
  local_path = "images/{0}{1}.jpg".format(name,x)
  storage.child(path_on_cloud).put(local_path)
  url = storage.child(path_on_cloud).get_url(None)
  db.child("Movement").push(url)
  db.child().update({'motor':0})

def Detect():
    n = GPIO.input(IR)
    if(n == 0):
        print("@@@@@@@@@@@@Movement Detected!! Capturing Image.....")
        MovementAlert()
       # os.system('play Police.wav')
        
schedule.every(30).seconds.do(MovementAlertsec)

while True:
    schedule.run_pending()
    Detect()
    
