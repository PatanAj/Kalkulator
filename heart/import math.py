import math
from turtle import *

def hearta(K):
    return 12*math.cos(K)**3

def heartb(K) :
    return 12*math.sin(K)-5*\
    math.cos(2*K)-2*\
    math.cos(3*K)-\
    math.cos(4*K)

speed(9000)
bgcolor("white")

for i in range(6000):
    goto(hearta(i)*20,heartb(i)*20)
    for j in range(5):
        color("pink")
    goto(0,0)
    done()
