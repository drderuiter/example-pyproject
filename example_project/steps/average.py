import numpy as np

from .base import BaseStep


class Average(BaseStep):
    """"""

    def run(self, data: np.ndarray) -> float:
        """"""
        return data.mean()
