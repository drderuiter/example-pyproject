import abc
from abc import ABC
from typing import Optional, Union

import numpy as np


class BaseStep(ABC):
    """"""

    def __init__(self, name: str, quantity: Optional[str]):
        """"""
        self.name = name
        self.quantity = quantity

    @abc.abstractmethod
    def run(self, data: np.ndarray) -> Union[np.ndarray, float]:
        raise NotImplementedError
