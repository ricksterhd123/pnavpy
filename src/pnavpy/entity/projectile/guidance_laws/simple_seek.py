import numpy.typing as npt
import numpy as np

def simple_seek(
        source_position: npt.NDArray[3],
        target_position: npt.NDArray[3]
    ) -> npt.NDArray[3]:
    return target_position - source_position
