from enum import Enum


class SchedulerPredictionType(str, Enum):
    EPSILON = "epsilon"
    SAMPLE = "sample"
    V_PREDICTION = "v_prediction"

    def __str__(self) -> str:
        return str(self.value)
