import os
import time
from random import *
def Change():
    print('Max number for random 5 <--')
    HowMuch = int(input('Number of random --> '))
    if HowMuch > 5:
        print('Max number for random 5 <--')
        Change()
    print('Max number is 999999999999999999')
    MaxNumber = int(input('Max random number --> '))
    if MaxNumber > 999999999999999999:
        print('Max number is 999999999999999999')
        Change
    a1 = randint(a=1,b=MaxNumber)
    a2= randint(a=1,b=MaxNumber)
    a3= randint(a=1,b=MaxNumber)
    a4= randint(a=1,b=MaxNumber)
    a5= randint(a=1,b=MaxNumber)
    print('|NUM1| -->', a1)
    if HowMuch >= 2:
        print('|NUM2| -->', a2)
    if HowMuch >= 3:
        print('|NUM3| -->', a3)
    if HowMuch >= 4:
        print('|NUM4| -->', a4)
    if HowMuch >= 5:
        print('|NUM5| -->', a5)
    
    COMMAND = """
    1.Exit
    2.Restart
    By qrxvino
    """
    print(COMMAND)
    COMM = int(input('ENTER Num of command --> '))
    if COMM == 1:
        Mode()    
    else:
        Change()
def Change2():
    HowMuch2 = int(input('Number of random --> '))
    MaxNumber2 = int(input('Max random number --> '))
    NUM = 0
    while HowMuch2 != 0:
        time.sleep(0.001)
        rand = randint(a=1,b=MaxNumber2)
        NUM += 1
        print('Num',NUM,'-->',  rand)
        HowMuch2 -= 1
def Change3():
    HowMuch3 = int(input('Number for search--> '))
    MaxNumber3 = int(input('Max random number --> '))
    NUM = 0
    rand = 0
    while rand != HowMuch3:
        time.sleep(0.001)
        randg = randint(a=1,b=MaxNumber3)
        rand = randg
        NUM += 1
        if rand == HowMuch3:
            print('|-->', rand, '<--|')
        else:
            print('-->', rand)
        if rand == HowMuch3:
            print('It took',NUM,'attempts') 
            break

def Mode():
    ChangeModeGUI = """
    1.infinite mode
    2.Normal mode
    3.generate not yet ...
    """
    print(ChangeModeGUI)
    ChangeMode = int(input('--> '))
    if ChangeMode == 2:
        Change()
    elif ChangeMode == 3:
        Change3()
    elif ChangeMode == 1:
        Change2()
Mode()

