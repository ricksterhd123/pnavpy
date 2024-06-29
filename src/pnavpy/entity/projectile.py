import numpy as np
from particle import Particle

class Projectile(Particle):
    def __init__(self, position, velocity, acceleration, color='r'):
        super().__init__(position, velocity, acceleration)
        self._xyzs = np.reshape(np.array([[position]]), (1,3))

    def __is_moving(self):
        return np.linalg.norm(super().get_velocity()) > 0

    def update(self, dt):
        super().update(dt)
        if self.__is_moving():
            self._xyzs = np.append(self._xyzs, [super().get_position()], axis=0)

    def get_xyzs(self):
        return self._xyzs
