from random import randint

def lancer():
    print(randint(1, 6), randint(1, 6), randint(1, 6))

def simulation(og):
    for i in range(0, og):
        lancer()

simulation(100000)