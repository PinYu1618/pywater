from typing import Union

from PyQt5.QtWidgets import QWidget


class AnalysisView(QWidget):
    def __init__(self, parent: Union[QWidget, None] = None):
        super().__init__(parent)


import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]

file_path = "使用者體重紀錄.txt"

try:
    loaded_data = pd.read_csv(file_path, sep="\t", parse_dates=["日期"])
    loaded_data["日期"] = pd.to_datetime(loaded_data["日期"])
except (FileNotFoundError, pd.errors.EmptyDataError):
    loaded_data = pd.DataFrame(columns=["日期", "體重"])
    loaded_data.to_csv(file_path, sep="\t", index=False)


def save_data():
    loaded_data.to_csv(file_path, sep="\t", index=False)


def plot_chart():
    global loaded_data

    if loaded_data.empty:
        print("\n✖尚未輸入數據，無法繪製折線圖。\n_____________________")
        return

    loaded_data["日期"] = pd.to_datetime(loaded_data["日期"])

    loaded_data = loaded_data.sort_values(by="日期")

    plt.figure(figsize=(10, 6))

    plt.plot(
        loaded_data["日期"],
        loaded_data["體重"],
        linestyle="-",
        marker="o",
        label="體重趨勢",
        color="blue",
    )

    plt.title("體重變化折線圖")
    plt.xlabel("日期")
    plt.ylabel("體重 (kg)")
    plt.legend()
    plt.grid(True)
    plt.show()


def add_data():
    global loaded_data
    print("\n▼ 新增數據")
    date_input = input("★請輸入要新增的日期(如：2023-12-01): ")
    weight_input = input("★請輸入體重，單位為kg(如：62.1): ")

    try:
        date = datetime.strptime(date_input, "%Y-%m-%d").date()
        weight = float(weight_input)

        loaded_data["日期"] = pd.to_datetime(loaded_data["日期"]).dt.date

        if date not in loaded_data["日期"].values:
            new_data = pd.DataFrame({"日期": [date], "體重": [weight]})
            loaded_data = pd.concat([loaded_data, new_data], ignore_index=True)
            print("\n√登錄成功！\n_____________________")
            save_data()
        else:
            print("\n✖該日期已有紀錄，請輸入新的日期。\n_____________________")

    except ValueError:
        print("\n✖錯誤！請重新輸入正確的日期和體重格式。\n_____________________")


def modify_data():
    global loaded_data
    print("\n▼ 修改特定紀錄")
    date_input = input("★請輸入要修改的日期(如：2023-12-01): ")

    try:
        date = datetime.strptime(date_input, "%Y-%m-%d").date()

        loaded_data["日期"] = pd.to_datetime(loaded_data["日期"]).dt.date

        if date in loaded_data["日期"].values:
            index = loaded_data.index[loaded_data["日期"] == date][0]
            new_weight = float(input("★請輸入新的體重，單位為kg: "))
            loaded_data.at[index, "體重"] = new_weight
            print("\n√修改成功！\n_____________________")
            save_data()
        else:
            print("\n✖該日期未存在紀錄！\n_____________________")

    except ValueError:
        print("\n✖錯誤！請重新輸入正確的日期和體重格式。\n_____________________")


def delete_data():
    global loaded_data
    print("\n▼ 刪除特定紀錄")
    date_input = input("★請輸入要刪除的日期(如：2023-12-01): ")

    try:
        date = datetime.strptime(date_input, "%Y-%m-%d").date()
        loaded_data["日期"] = pd.to_datetime(
            loaded_data["日期"]
        ).dt.date  # 將 loaded_data 中的日期轉換為日期格式
        if date not in loaded_data["日期"].values:
            print("\n✖該日期未存在紀錄！\n_____________________")
            return

        loaded_data = loaded_data[loaded_data["日期"] != date]
        print("\n√刪除成功！\n_____________________")
        save_data()
    except ValueError:
        print("\n✖錯誤！請重新輸入正確的日期格式。\n_____________________")
