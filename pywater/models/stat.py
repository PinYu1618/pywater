from collections import namedtuple
from typing import Union
from pathlib import Path
from datetime import date

import pandas as pd
import matplotlib.pyplot as plt

# water needed per day per kg
ML_PER_KG = 35.0

# bmi status
OBESE = 1
NORMAL = 0
UNDERWEIGHT = -1

Record = namedtuple("Record", ["water", "weight", "height"])


class Stat(object):
    def __init__(
        self, db_path: Path, weight: Union[int, float] = 55, water: int = 0
    ) -> None:
        # init db
        self.db_path = db_path
        try:
            self.db_path.touch(exist_ok=False)
            self.df = pd.DataFrame(columns=["date", "water", "weight", "height"])
            self.save()
        except:
            self.load()
        self.weight = weight
        self.water = water
        self.height = 100

    @classmethod
    def water_per_day(cls, weight: float) -> int:
        return round(weight * ML_PER_KG)

    def bmi_msg(self) -> str:
        record = self.get_record(date.today())
        # 計算BMI
        bmi = round(float(record.weight) / (float(record.height) / 100.0) ** 2, 2)
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
        """
        Load data from disk
        """
        try:
            self.df = pd.read_csv(self.db_path, sep="\t", parse_dates=["date"])
            self.df["date"] = pd.to_datetime(self.df["date"], yearfirst=True).dt.date
            today = date.today()
            if today not in self.df["date"].values:
                self._add(today, Record(0, 60.0, 165.0))
                self.save()
        except (FileNotFoundError, pd.errors.EmptyDataError):
            print("Db load error")

    def get_record(self, date: date) -> Union[Record, None]:
        """
        Get record by date
        """
        self.df["date"] = pd.to_datetime(self.df["date"]).dt.date
        if date not in self.df["date"].values:
            return None
        else:
            index = self.df.index[self.df["date"] == date][0]
            water = self.df.at[index, "water"]
            weight = self.df.at[index, "weight"]
            height = self.df.at[index, "height"]
            return Record(water, weight, height)

    def set_record(self, date: date, record: Record) -> None:
        """
        Update (in memory) data
        """
        self.df["date"] = pd.to_datetime(self.df["date"]).dt.date
        if date not in self.df["date"].values:
            self._add(date, record)
        else:
            self._modify(date, record)

    def save(self):
        """
        Save data to disk
        """
        self.df.to_csv(self.db_path, sep="\t", index=False)

    def _add(self, date: date, record: Record):
        new_df = pd.DataFrame(
            {
                "date": [date],
                "water": [record.water],
                "weight": [record.weight],
                "height": [record.height],
            }
        )
        self.df = pd.concat([self.df, new_df], ignore_index=True)

    def _modify(self, date: date, record: Record):
        index = self.df.index[self.df["date"] == date][0]
        self.df.at[index, "weight"] = record.weight
        self.df.at[index, "water"] = record.water
        self.df.at[index, "height"] = record.height
