import math
import numpy as np

def get_angle_between_vectors(a, b):
    adist = np.linalg.norm(a)
    bdist = np.linalg.norm(b)
    if (adist <= 0 or bdist <= 0):
        return 0
    return math.acos(np.dot(a, b) / (adist * bdist))
