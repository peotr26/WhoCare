# Importing libraries:
from random import randint

# Functions:
def throw()->int:
    '''This function generates a three dices throw.
    The integer that is return is the sum of the three dices result.
    '''
    return randint(1, 6) + randint(1, 6) + randint(1, 6)

def counting(n:int, list:list)->int:
    '''This function counts the number of occurence of an integer in a specified list.

    n -- The integer for which the function is going to count the number of occurences.
    list -- The list in which the number of occurence of n is going to be counted.
    '''
    return list.count(n)

# Main function of the script:
def simulation(mag:int)->tuple:
    '''This is the main function of the script.

    mag -- The integer that specifies the number of throws for the final result.
    '''
    num_list = [throw() for i in range(0, mag)]
    return counting(10, num_list), counting(9, num_list)
