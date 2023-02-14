import math
import p2_sol
import numpy as np

def H_1():
    #Current Frame - Post Multiply
    a = np.matmul(p2_sol.trans_x(2.5), p2_sol.trans_z(0.5))

    a = np.matmul(a, p2_sol.trans_z(-1.5))
    return a

def H_2():
    #Current Frame - Post Multiply
    a = np.matmul(p2_sol.trans_z(0.5), p2_sol.trans_x(2.5))

    a = np.matmul(a, p2_sol.trans_y(-1.5))
    return a

def H_3():
    #Fixed Pre Multiply
    a = np.matmul(p2_sol.trans_y(-1.5), p2_sol.trans_z(0.5))

    a = np.matmul(a, p2_sol.trans_x(2.5))
    return a


def H_4():
    #Fixed Pre Multiply
    a= np.matmul(p2_sol.trans_y(-1.5), p2_sol.trans_x(2.5))

    a = np.matmul(a, p2_sol.trans_z(0.5))
    return a


def H_5():
    # Current Frame - Post Multiply

    # Rotate pi/2 & Rotate 3
    a = np.matmul(p2_sol.rot_x(math.pi / 2), p2_sol.trans_x(3))

    # * Rotate -3
    a = np.matmul(a, p2_sol.trans_z(-3))


    #Rotate -pi/2 @ z-axis
    x = p2_sol.rot_z((-1) * (math.pi / 2))


    a = np.matmul(a, x)

    return a


if __name__ == '__main__':
    np.set_printoptions(precision=5, suppress=True)
