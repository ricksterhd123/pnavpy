import numpy as np

class Particle:
    def __init__(
            self,
            position = np.array([0.0, 0.0, 0.0]), 
            velocity = np.array([0.0, 0.0, 0.0]),
            acceleration = np.array([0.0, 0.0, 0.0])
        ):

        self._position = position
        self._velocity = velocity
        self._acceleration = acceleration

    def set_position(self, x, y, z):
        self._position = np.array([x, y, z])

    def get_position(self):
        return self._position

    def set_velocity(self, velocity = np.array([0.0, 0.0, 0.0])):
        self._velocity = velocity

    def get_velocity(self):
        return self._velocity
    
    def set_acceleration(self, acceleration = np.array([0.0, 0.0, 0.0])):
        self._acceleration = acceleration

    def get_acceleration(self):
        return self._acceleration

    def update(self, dt):
        self._velocity += self._acceleration * dt
        self._position += self._velocity * dt
