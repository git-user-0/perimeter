import math
import time
import turtle
import random

def proveItTiny(v, h):
    turtle.lt(90)
    for pair in range(2):
        turtle.fd(v * 10)
        turtle.rt(90)
        turtle.fd(h * 10)
        turtle.rt(90)

def proveItSmall(v, h):
    turtle.lt(90)
    for pair in range(2):
        turtle.fd(v * 5)
        turtle.rt(90)
        turtle.fd(h * 5)
        turtle.rt(90)

def proveItMedium(v, h):
    turtle.lt(90)
    for pair in range(2):
        turtle.fd(v * 2.5)
        turtle.rt(90)
        turtle.fd(h * 2.5)
        turtle.rt(90)

def proveItLarge(v, h):
    turtle.lt(90)
    for pair in range(2):
        turtle.fd(v * 1.25)
        turtle.rt(90)
        turtle.fd(h * 1.25)
        turtle.rt(90)

print('Enter the number you would like to check: ')
number = int(input())
if (number % 2 != 0) or (number < 6):
    print('''It is not possible to draw even one rectilinear shape which has
a perimeter equal to that number.''')
elif number % 2 == 0:
    solution = math.floor(number / 4)
    solution = int(solution)
    print('There are ', solution, ' rectilinear shapes which can be drawn with')
    print('a perimeter equal to that number.')
    if number < 545:
        print()
        print('Would you like me to prove it for you?')
        answer = input()
        if answer.lower() == 'y':
            if number < 69:
                for i in range(1, (solution + 1)):
                    v = i
                    l = number - (i * 2)
                    h = int(l / 2)
                    proveItTiny(v, h)
                    turtle.rt(45)
            elif number > 69 and number < 137:
                for i in range(1, (solution + 1)):
                    v = i
                    l = number - (i * 2)
                    h = int(l / 2)
                    proveItSmall(v, h)
                    turtle.rt(45)
            elif number > 137 and number < 273:
                for i in range(1, (solution + 1)):
                    v = i
                    l = number - (i * 2)
                    h = int(l / 2)
                    proveItMedium(v, h)
                    turtle.rt(45)
            elif number > 273 and number < 545:
                for i in range(1, (solution + 1)):
                    v = i
                    l = number - (i * 2)
                    h = int(l / 2)
                    proveItLarge(v, h)
                    turtle.rt(80)
