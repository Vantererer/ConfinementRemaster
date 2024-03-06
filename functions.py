import sys
import time

Deflay = 35 

def sl(ms: int):
    time.sleep(ms / 1000)

wait, delay = sl, sl # feel free to change the code (6-9)

def clean():
    print("/033c", end='')

def match_from_array(data: str, array) -> bool: #forgor what trhis was
    out = False
    for x in array:
        if x == data:
            out = True
        if out:
            return True
        else:
            return False

def twriter (text: str, delaychar: int): # Type writer effect
    if not text:
        print("Missing Text Error")
    if not delaychar:
        delaychar = Deflay
    for char in text:
        sys.std.write(char)
        sl(delaychar)
        sys.stdout.flush()
