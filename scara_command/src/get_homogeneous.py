#!/usr/bin/env python3

from scara_command.srv import ScaraHomoMatrix, ScaraHomoMatrixResponse
import numpy
from helper import np2ma

import rospy


## Assuming that the input is q1 q2 q3 the output should be x y z phi theta psi
def homogeneous_A(a1, alph1, d1, theta1):
    A = numpy.array([[numpy.cos(theta1), (numpy.sin(theta1)*-1) * numpy.cos(alph1), numpy.sin(theta1) * numpy.sin(alph1), a1 * numpy.cos(theta1)],
                      [numpy.sin(theta1), numpy.cos(theta1) * numpy.cos(alph1), (numpy.cos(theta1)*-1) * numpy.sin(alph1), a1 * numpy.sin(theta1)],
                      [0, numpy.sin(alph1), numpy.cos(alph1), d1],
                      [0, 0, 0, 1]])
    return A


def handle_homogeneous_matrix(req):
    ##_---------------------- DH Parameters----------------------------------------
    a1 = .35
    alph1 = 0
    d1 = .36
    theta1 = req.q1

    a2 = .30
    alph2 = 3.14
    d2 = 0
    theta2 = req.q2

    a3 = 0
    alph3 = 0
    d3 = req.q3  + .11
    theta3 = 0

    A1 = np2ma(homogeneous_A(a1, alph1, d1, theta1))
    A2 = np2ma(homogeneous_A(a2, alph2, d2, theta2))
    A3 = np2ma(homogeneous_A(a3, alph3, d3, theta3))

    return ScaraHomoMatrixResponse(A1, A2, A3)


def get_homogeneous():
    rospy.init_node('homogeneous_matrix_server')
    s = rospy.Service('homogeneous_matrix', ScaraHomoMatrix, handle_homogeneous_matrix)

    rospy.spin()


if __name__ == "__main__":
    get_homogeneous()