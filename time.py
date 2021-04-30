
import random
import os
from time import sleep
import subprocess
from playsound import playsound


def request_start():
    ask = input("press enter to start")
    return ask

def r():
    rantime = random.uniform(2, 4)*2
    print("what r time will it be??")
    sleep(rantime*60)
    print("yay")
    playsound('ding.mp3')
    ask_to_continue = input("press enter to continue")
    return ask_to_continue


def c():
    rantime = random.uniform(1, 2)
    print("what c time will it be??")
    sleep(rantime*60)
    print("yay")
    playsound('ding.mp3')
    ask_to_continue = input("press enter to continue")
    return ask_to_continue


request_start()
r()
c()
r()
c()
r()
c()
r()
c()