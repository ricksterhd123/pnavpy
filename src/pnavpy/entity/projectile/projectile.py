import numpy as np
import numpy.typing as npt

from ..particle import Particle
from .guidance_laws import simple_seek

class Projectile(Particle):
    def __init__(self, position, velocity, acceleration):
        super().__init__(position, velocity, acceleration)

    def update(self, dt):
        super().update(dt)

class SimpleSeekProjectile(Projectile):
    def __init__(self, postiion: npt.NDArray[3], velocity: npt.NDArray[3], target: Particle):
        super().__init__(postiion, velocity, np.array([0.0, 0.0, 0.0]))
        self._target = target

    def update(self, dt: float):
        self._acceleration = simple_seek(
            self._position, 
            self._target.get_position(),
            self._velocity,
            self._target.get_velocity()
        )
        super().update(dt)
