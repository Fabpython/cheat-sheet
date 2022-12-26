#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 18:00:44 2022

@author: fabioribeiro
"""

class Coordinate(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def distance(self, other):
        x_diff_sq =(self.x-other.x)**2
        y_diff_sq=(self.y-other.y)**2
        return(x_diff_sq+y_diff_sq)**0.5
    
    
#gives the distance between 2 points 
x=Coordinate(2,4)
y=Coordinate(3,6)
print(x.distance(y))

#we can see to use the object "distance" since there is self and other when we create it, to use it we basic
#juste put the name of the first coordinate(self, here x) and the"other" will be point y so we evaluate
#the distance between "self" which is x here and "other" which is y here.

print(x)

#if we just print the object x we will get a shit result we need to code it to get an appropriate result

class Coordinate(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def distance(self, other):
        x_diff_sq =(self.x-other.x)**2
        y_diff_sq=(self.y-other.y)**2
        return(x_diff_sq+y_diff_sq)**0.5
    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"
    
x=Coordinate(2,4)
print(x)