
import random
import os
from time import sleep
import subprocess
from playsound import playsound

input = input("press enter to start")

def run():
    rantime = random.randint(1, 2)*2
    print("what time will it be??")
    sleep(rantime*60)
    print("yay")
    playsound('ding.mp3')
    continueInput = input("press enter to start")
    print(continueInput)

run()
run()
run()
run()
run()