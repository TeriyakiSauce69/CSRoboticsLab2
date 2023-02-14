import math
import numpy as np

#Six blocks to formulate complex motions. Taken from slides.

def trans_x(a):
    trans = np.array([[1, 0, 0, a],
                    [0, 1, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])
    return trans


def trans_y(b):
    trans = np.array([[1, 0, 0, 0],
                    [0, 1, 0, b],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])
    return trans


def trans_z(c):
    trans = np.array([[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 1, c],
                    [0, 0, 0, 1]])
    return trans


def rot_x(alpha):
    rot = np.array([[1, 0, 0, 0],
                    [0, math.cos(alpha), -math.sin(alpha), 0],
                    [0, math.sin(alpha), math.cos(alpha), 0],
                    [0, 0, 0, 1]])
    return rot


def rot_y(beta):
    rot = np.array([[math.cos(beta), 0, math.sin(beta), 0],
                    [0, 1, 0, 0],
                    [-math.sin(beta), 0, math.cos(beta), 0],
                    [0, 0, 0, 1]])
    return rot


def rot_z(gamma):
    rot = np.array([[math.cos(gamma), -math.sin(gamma), 0, 0],
                    [math.sin(gamma), math.sin(gamma), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])
    return rot