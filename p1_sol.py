import rbm
import math
import numpy as np

def roll_pitch_yaw(x0, y0, z0, ):

    np.set_printoptions(precision=5, suppress=True)

    #Current Frame - Post Multiply

    a = np.matmul(rbm.rot_y(y0), rbm.rot_x(x0))

    a = np.matmul(rbm.rot_z(z0), a)

    return a


if __name__ == '__main__':
    psi = math.pi/2
    theta = math.pi/2
    phi = math.pi/2

    test = roll_pitch_yaw(psi, theta, phi)

    print(test)