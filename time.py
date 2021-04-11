
import random
import os
from time import sleep
import subprocess
from playsound import playsound

def run():
    rantime = random.randint(1, 2)*2
    print("what time will it be??")
    sleep(rantime*60)
    print("yay")
    playsound('ding.mp3')

run()
run()
run()