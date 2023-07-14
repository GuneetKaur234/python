from pygame import mixer
import datetime
from time import time
from plyer import notification

def getdate():
    return datetime.datetime.now()

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break


def log_now(msg):
    with open ("mylogs.txt", "a") as f:
        f.write(f"{msg} {getdate()}\n")

if __name__ == "__main__":
    init_water = time()
    init_eyes = time()
    init_excersie = time()

    water_sec = 5
    eyes_sec = 10
    exercise_sec = 20

    while True:
        if time() - init_water > water_sec:
                notification.notify(
                title = 'Reminder',
                message = 'Drink Water',
                app_icon = None)
                print("Drink water. Enter 'Drank' to stop the alarm. ")
                musiconloop("drinking water.mp3", "Drank")
                init_water = time()
                log_now("Drank water at ")
                
        elif time() - init_eyes > eyes_sec:
                notification.notify(
                title = 'Reminder',
                message = 'Blink your eyes',
                app_icon = None)
                print("Blink your eyes. Enter 'Blink' to stop the alarm. ")
                musiconloop("drinking water.mp3", "Blink")
                init_eyes = time()
                log_now("Blinked your eyes at  ")

        elif time() - init_excersie > exercise_sec:
                notification.notify(
                title = 'Reminder',
                message = 'Time to do exercise',
                app_icon = None)
                print("Time to do exercise. Enter 'Done' to stop the alarm. ")
                musiconloop("drinking water.mp3", "Done")
                init_excersie = time()
                log_now("Excersice done at  ")




