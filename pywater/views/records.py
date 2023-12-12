import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QInputDialog,
)
from PyQt5.QtCore import Qt
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


class WeightRecordApp(QWidget):
    def __init__(self):
        super().__init__()

        self.file_path = "使用者體重紀錄.txt"
        self.loaded_data = pd.DataFrame(columns=["日期", "體重"])
        self.load_data()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("體重紀錄應用程式")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        btn_add = QPushButton("新增數據", self)
        btn_add.clicked.connect(self.add_data)
        layout.addWidget(btn_add)

        btn_modify = QPushButton("修改特定紀錄", self)
        btn_modify.clicked.connect(self.modify_data)
        layout.addWidget(btn_modify)

        btn_delete = QPushButton("刪除特定紀錄", self)
        btn_delete.clicked.connect(self.delete_data)
        layout.addWidget(btn_delete)

        btn_plot = QPushButton("顯示變化趨勢", self)
        btn_plot.clicked.connect(self.plot_chart)
        layout.addWidget(btn_plot)

        self.lbl_status = QLabel("", self)
        layout.addWidget(self.lbl_status)

        self.setLayout(layout)

    def load_data(self):
        try:
            self.loaded_data = pd.read_csv(self.file_path, sep="\t", parse_dates=["日期"])
            self.loaded_data["日期"] = pd.to_datetime(self.loaded_data["日期"])
        except (FileNotFoundError, pd.errors.EmptyDataError):
            pass

    def save_data(self):
        self.loaded_data.to_csv(self.file_path, sep="\t", index=False)

    def plot_chart(self):
        if self.loaded_data.empty:
            self.lbl_status.setText("尚未輸入數據，無法繪製折線圖。")
            return

        self.loaded_data = self.loaded_data.sort_values(by="日期")

        plt.figure(figsize=(10, 6))
        plt.plot(
            self.loaded_data["日期"],
            self.loaded_data["體重"],
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

    def add_data(self):
        date_input, ok = QLineEdit.getText(
            QInputDialog(), "新增數據", "請輸入要新增的日期(如：2023-12-01):"
        )
        weight_input, ok = QLineEdit.getText(
            QInputDialog(), "新增數據", "請輸入體重，單位為kg(如：62.1):"
        )

        try:
            date = datetime.strptime(date_input, "%Y-%m-%d").date()
            weight = float(weight_input)

            self.loaded_data["日期"] = pd.to_datetime(self.loaded_data["日期"]).dt.date

            if date not in self.loaded_data["日期"].values:
                new_data = pd.DataFrame({"date": [date], "weight": [weight]})
                self.loaded_data = pd.concat(
                    [self.loaded_data, new_data], ignore_index=True
                )
                self.lbl_status.setText("登錄成功！")
                self.save_data()
            else:
                self.lbl_status.setText("該日期已有紀錄，請輸入新的日期。")

        except ValueError:
            self.lbl_status.setText("錯誤！請重新輸入正確的日期和體重格式。")

    def modify_data(self):
        date_input, ok = QLineEdit.getText(
            QInputDialog(), "修改特定紀錄", "請輸入要修改的日期(如：2023-12-01):"
        )

        try:
            date = datetime.strptime(date_input, "%Y-%m-%d").date()

            self.loaded_data["日期"] = pd.to_datetime(self.loaded_data["日期"]).dt.date

            if date in self.loaded_data["日期"].values:
                index = self.loaded_data.index[self.loaded_data["日期"] == date][0]
                new_weight, ok = QLineEdit.getText(
                    QInputDialog(), "修改特定紀錄", "請輸入新的體重，單位為kg:"
                )
                new_weight = float(new_weight)
                self.loaded_data.at[index, "體重"] = new_weight
                self.lbl_status.setText("修改成功！")
                self.save_data()
            else:
                self.lbl_status.setText("該日期未存在紀錄！")

        except ValueError:
            self.lbl_status.setText("錯誤！請重新輸入正確的日期和體重格式。")

    def delete_data(self):
        date_input, ok = QLineEdit.getText(
            QInputDialog(), "刪除特定紀錄", "請輸入要刪除的日期(如：2023-12-01):"
        )

        try:
            date = datetime.strptime(date_input, "%Y-%m-%d").date()
            self.loaded_data["日期"] = pd.to_datetime(self.loaded_data["日期"]).dt.date
            if date not in self.loaded_data["日期"].values:
                self.lbl_status.setText("該日期未存在紀錄！")
                return

            self.loaded_data = self.loaded_data[self.loaded_data["日期"] != date]
            self.lbl_status.setText("刪除成功！")
            self.save_data()
        except ValueError:
            self.lbl_status.setText("錯誤！請重新輸入正確的日期格式。")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = WeightRecordApp()
    ex.show()
    sys.exit(app.exec_())
