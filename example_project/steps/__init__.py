"""Step definitions."""

from enum import Enum

from .add import Add
from .average import Average
from .base import BaseStep


class StepType(Enum):
    """"""

    ADD = "add"
    AVERAGE = "average"


STEP_LOOKUP: dict[StepType:BaseStep] = {
    StepType.ADD: Add,
    StepType.AVERAGE: Average,
}
