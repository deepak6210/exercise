#healthy programmer
#9am to 5am
# water - water.mp3(3.6 litres) - drank - log
# eyes - eyes.mp3 - every 30 min - eydone- log
# physical activity - physcial.mp3every - 45 min exdone - log
# rules
# pygame module to play audio
import time
import pygame
from pygame import mixer
def playmusic(file):
    print(file)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def isooficetime(currenttime):
    if currenttime>'09:00:00' and currenttime<'17:00:00':
        return  True
    else:
        return  False
NumberofWaterReamaining = 18
WaterAfterEvery = 1200
EyeExerciseAfterEvery = 1800
PhyscialExerciseAfterEVery = 2700
waterMp3 = 'water1.mp3'
eyesMp3 = 'eyeexc.mp3'
PhysicalMp3 = 'physicalwork.mp3'

currenttime = time.strftime('%H:%M:%S')
WaterTakenAt = time.time()
EyeExerciseAt = time.time()
PhyscialExerciseAt = time.time()

sleepTime = 60

while(isooficetime(currenttime)):
    if NumberofWaterReamaining > 0:
        if(time.time()-WaterTakenAt)>WaterAfterEvery:
            print("time to drink water")
            while True:
                playmusic(waterMp3)
                if input("enter done if you had water:").lower() == "done":
                    WaterTakenAt = time.time()
                    NumberofWaterReamaining = NumberofWaterReamaining - 1
                    break
    if (time.time() - EyeExerciseAt)>EyeExerciseAt:
        print("it's time to do some eye exersice")
        while(True):
            playmusic(eyesMp3)
            if input("enter done if you had the exercise:").lower() == "done":
                EyeExerciseAt = time.time()
                break
    if (time.time() - PhyscialExerciseAt)>PhyscialExerciseAt:
        print("it's time to do some physical work please do it")
        while(True):
            playmusic(PhysicalMp3)
            if input("enter done if you had your physical work").lower() == "done":
                PhyscialExerciseAt = time.time()
                break

time.time(sleepTime)
currenttime = time.strftime('%H:%M:%S')