from math import *

def dpi(w, h, screen_size):
    return (w*h)/screen_size

def ratio(w, h, screen_size):
    return 

def calculating(w, h, screen_size, distance):
    if 300/10 < dpi(w, h, screen_size)/distance < 300/12:
        return True
    else:
        return False

print(dpi(1920, 1080, 15))
print(calculating(1920, 1080, 15, 40))
