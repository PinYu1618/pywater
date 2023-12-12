from typing import Union
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# water needed per day per kg
ML_PER_KG = 35.0


class Stat(object):
    def __init__(self, db, weight: Union[int, float] = 55, water: int = 0) -> None:
        # init db
        self.db_path = Path("./db").joinpath(db)
        try:
            self.db_path.touch(exist_ok=False)
            self.df = pd.DataFrame(columns=["date", "weight"])
            self.save()
        except:
            self.df = pd.DataFrame(columns=["date", "weight"])
        self.weight = weight
        self.water = water
        # self.load()

    def water_per_day(self) -> int:
        return round(self.weight * ML_PER_KG)

    def load(self):
        try:
            self.df = pd.read_csv(self.db_path, sep="\t", parse_dates=["date"])
            self.df["date"] = pd.to_datetime(self.df["date"])
        except (FileNotFoundError, pd.errors.EmptyDataError):
            print("Db load error")

    def save(self):
        self.df.to_csv(self.db_path, sep="\t", index=False)
