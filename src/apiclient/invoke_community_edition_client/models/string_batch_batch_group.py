from enum import Enum


class StringBatchBatchGroup(str, Enum):
    GROUP_1 = "Group 1"
    GROUP_2 = "Group 2"
    GROUP_3 = "Group 3"
    GROUP_4 = "Group 4"
    GROUP_5 = "Group 5"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)
