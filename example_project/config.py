from typing import Optional

import numpy as np
from pydantic import BaseModel, BaseSettings

from example_project.steps import StepType


class Step(BaseModel):
    """"""

    name: str
    type: StepType
    quantity: Optional[int] = None


class Config(BaseSettings):
    """"""

    input_value: list[float]
    steps: list[Step]
