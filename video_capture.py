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
t = time.localtime()
x = time.strftime("%H:%M:%S", t)
name = "Video"


path_on_cloud = "User/{0}{1}".format(name,x)
local_path = "videos/{0}{1}.mp4".format(name,x)
print("Capturing Video")
os.system(("ffmpeg -video_size 640x480 -f v4l2 -i /dev/video0 -t 00:00:10 videos/{}{}.mp4".format(name,x)))
print("video Captured")

print("sending")
storage.child(path_on_cloud).put(local_path)
url = storage.child(path_on_cloud).get_url(None)
db.child("video").push(url)

print("done")
