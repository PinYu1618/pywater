from typing import Union

# water needed per day per kg
ML_PER_KG = 35.0


class Stat(object):
    def __init__(self, weight: Union[int, float]) -> None:
        self.weight = weight

    def water_per_day(self) -> int:
        return round(self.weight * ML_PER_KG)
