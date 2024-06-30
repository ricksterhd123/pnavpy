import numpy.typing as npt
import numpy as np

def simple_seek(
        source_position: npt.NDArray[3],
        target_position: npt.NDArray[3],
        source_velocity: npt.NDArray[3],
        target_velocity: npt.NDArray[3],
    ) -> npt.NDArray[3]:

    offset = target_position - source_position
    offset_velocity = target_velocity - source_velocity

    distance = np.linalg.norm(offset)

    offset_norm = offset / distance
    offset_velocity_norm = offset_velocity / np.linalg.norm(offset_velocity)

    a_c = (offset_velocity_norm + offset_norm)
    a_c_dist = np.linalg.norm(a_c)
    if a_c_dist <= 0:
        return 0
    return a_c / a_c_dist
