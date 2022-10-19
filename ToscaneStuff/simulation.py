from random import randint

def lancer():
    return randint(1, 6) + randint(1, 6) + randint(1, 6)

def counting(n, list):
    return list.count(n)

def simulation(og):
    num_list = []
    for i in range(0, og):
        num_list.append(lancer())
    return counting(10, num_list), counting(9, num_list)

print(simulation(100000))