# This Python program stores all my math programs.

# Importing libraries:

from math import *

# 2nd degree equation

def delta(a,b,c):
    '''Function that return the descriminant of a 2nd degree polynomial.

    Keyword arguments:
    a -- a in ax²+bx+c (default 0.0)
    b -- b in ax²+bx+c (default 0.0)
    c -- c in ax²+bx+c (default 0.0)
    '''
    return b**2-4*a*c                           # Return the value of the descriminant.

def sde_resolution(a,b,c):
    '''Function that solve a 2nd degree equation.

    Keyword arguments:
    a -- a in ax²+bx+c (default 0.0)
    b -- b in ax²+bx+c (default 0.0)
    c -- c in ax²+bx+c (default 0.0)
    '''
    if delta(a, b, c) > 0:                      # If the descriminant is strictly positive then resolve.
        x1 = (-b-sqrt(delta(a,b,c))/(2*a))
        x2 = (-b+sqrt(delta(a,b,c))/(2*a))
        return x1,x2
    elif delta(a, b, c) == 0:                   # If the descriminant is equal to 0 then resolve.
        return (-b)/(2*a)
    else:                                       # If the descriminant is strictly negative then return an error. 
        raise ValueError('The descriminant is negative')

def check_delta_positive(a,b,c):
    '''Function that check if the descriminant of a 2nd degree polynomial is positive.

    Keyword arguments:
    a -- a in ax²+bx+c (default 0.0)
    b -- b in ax²+bx+c (default 0.0)
    c -- c in ax²+bx+c (default 0.0)
    '''
    if delta(a, b, c) >= 0:                     # If descriminant is positive then return True.
        return True
    else:                                       # If descriminant is negative then return False.
        return False