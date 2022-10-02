import logging
from typing import Any, Iterable

from example_project.config import Step
from example_project.steps import STEP_LOOKUP, BaseStep

LOGGER = logging.getLogger(__name__)


class Pipeline:
    def __init__(self, steps: list[BaseStep]):
        self.steps = steps

    @classmethod
    def from_config(cls, step_config=Iterable[Step]) -> "Pipeline":
        steps = [
            STEP_LOOKUP[step.type](step.name, step.quantity) for step in step_config
        ]
        return cls(steps)

    def run(self, value: Any) -> Any:
        LOGGER.info("Starting pipeline with value '%s'.", value)
        for step_nr, step in enumerate(self.steps):
            value = step.run(value)
            LOGGER.info("Value after step #%s '%s': '%s'.", step_nr, step.name, value)
        return value
