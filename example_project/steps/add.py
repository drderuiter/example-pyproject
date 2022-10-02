from typing import Optional

import numpy as np

from .base import BaseStep


class Add(BaseStep):
    """"""

    def __init__(self, name: str, quantity: Optional[str]):
        assert quantity is not None, f"Quantity is required for step '{self.name}'."
        super().__init__(name, quantity)

    def run(self, data: np.ndarray) -> np.ndarray:
        """"""
        return data + self.quantity
