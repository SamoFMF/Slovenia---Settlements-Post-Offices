# Utilities

import pickle
from math import pi, cos, sin, asin, sqrt

def saveFile(filename, data):
    with open(filename, "wb") as f:
        pickle.dump(data, f)

def loadFile(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)

def coordToDeg(coord):
    return coord[0] + coord[1] / 60 + coord[2] / 3600

def deg2rad(deg):
    return deg * pi / 180

def rad2deg(rad):
    return 180 * rad / pi

'''
Uses Haversine formula to calculate
distance between 2 points on a sphere
(approximation of Earth).

Input:
    -point P given as (longitude, latitude),
        where each is given as (degrees, minutes, seconds)
    -point Q

Output:
    -distance in kilometers
'''
def getDistance(P, Q): # point = (longitude, latitude)
    x1, y1 = P; x1 = deg2rad(coordToDeg(x1)); y1 = deg2rad(coordToDeg(y1))
    x2, y2 = Q; x2 = deg2rad(coordToDeg(x2)); y2 = deg2rad(coordToDeg(y2))

    f1 = sin((y2-y1)/2)**2
    f2 = cos(y1)
    f3 = cos(y2)
    f4 = sin((x2-x1)/2)**2

    f = sqrt(f1 + f2*f3*f4)
    R = (6356.752 + 6378.137) / 2 # Average of "Earth radius" at the poles and at the equator

    return 2 * R * asin(f)