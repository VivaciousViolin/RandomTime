
import random
import os
from time import sleep
import subprocess
from playsound import playsound

r_time = 1, 2
c_time =

def request_start():
    ask = input("press enter to start")
    return ask

def r():
    rantime = random.randint(1, 2)*2
    print("what time will it be??")
    sleep(rantime*60)
    print("yay")
    playsound('ding.mp3')
    ask_to_continue = input("press enter to continue")
    return ask_to_continue


def c():
    rantime = random.randint(1, 2)*2
    print("what time will it be??")
    sleep(rantime*60)
    print("yay")
    playsound('ding.mp3')
    ask_to_continue = input("press enter to continue")
    return ask_to_continue


request_start()
r()
c()