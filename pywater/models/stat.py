from typing import Union
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# water needed per day per kg
ML_PER_KG = 35.0

# bmi status
OBESE = 1
NORMAL = 0
UNDERWEIGHT = -1


class Stat(object):
    def __init__(self, db, weight: Union[int, float] = 55, water: int = 0) -> None:
        # init db
        self.db_path = Path("./db").joinpath(db)
        try:
            self.db_path.touch(exist_ok=False)
            self.df = pd.DataFrame(columns=["date", "weight"])
            self.save()
        except:
            self.load()
        self.weight = weight
        self.water = water

    def water_per_day(self) -> int:
        return round(self.weight * ML_PER_KG)

    def bmi_msg(self) -> str:
        # 計算BMI
        bmi = round(float(self.weight) / (float(self.height) / 100.0) ** 2, 2)
        # 判斷BMI
        if bmi < 18.5:
            warning = "過輕，建議增加飲食營養和適量運動。"
        elif 18.5 <= bmi < 24:
            warning = "正常，保持良好的生活習慣，繼續保持健康。"
        elif 24 <= bmi < 27:
            warning = "過重，建議注意飲食並增加運動，以維持健康體重。"
        elif 27 <= bmi < 30:
            warning = "輕度肥胖，建議諮詢醫生，並進行適當的飲食和運動調整。"
        elif 30 <= bmi < 35:
            warning = "中度肥胖，建議尋求專業的醫療建議，制定科學的減重計畫。"
        else:
            warning = "重度肥胖，請立即諮詢專業醫生，並進行相應的治療。"

        return str(bmi) + " " + warning

    def load(self):
        try:
            self.df = pd.read_csv(self.db_path, sep="\t", parse_dates=["date"])
            self.df["date"] = pd.to_datetime(self.df["date"])
        except (FileNotFoundError, pd.errors.EmptyDataError):
            print("Db load error")

    def update(self, water=None, weight=None, height=None):
        """Update today records (in memory)"""
        if water is not None:
            self.water = water
        if weight is not None:
            self.weight = weight
        if height is not None:
            self.height = height

    def save(self):
        self.df.to_csv(self.db_path, sep="\t", index=False)
