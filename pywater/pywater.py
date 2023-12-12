from functools import partial
from typing import Callable
from pathlib import Path
from datetime import date

import matplotlib

matplotlib.use("Qt5Agg")

from .views import View
from .models.stat import Stat


class PyWater:
    def __init__(self, db_path: Path, view: View, encourage: Callable) -> None:
        self._ui = view
        self._encourage = encourage
        self._stat = Stat(db_path, water=100)
        self._init_ui()
        self._connect_signals()

    def _init_ui(self):
        record = self._stat.get_record(date.today())
        lvl = float(self._stat.water)
        mx = float(self._stat.water_per_day())
        self._ui.home.glass.draw_water(lvl / mx)
        self._ui.home.print_msg(self._encourage())
        self._ui.history.show_record(record)
        if not self._stat.df.empty:
            self._stat.df.plot(ax=self._ui.analysis.sc.axes)

    def _connect_signals(self):
        self._ui.home.btnsub.clicked.connect(partial(self._on_water_btn, -100))
        self._ui.home.btn100.clicked.connect(partial(self._on_water_btn, 100))
        self._ui.home.btn200.clicked.connect(partial(self._on_water_btn, 200))
        self._ui.home.btn500.clicked.connect(partial(self._on_water_btn, 500))
        self._ui.home.btn_bmi.clicked.connect(self._on_bmi_btn)
        self._ui.history.calendar.selectionChanged.connect(self._on_date_changed)
        self._ui.history.btn_save.clicked.connect(self._on_save)

    def _on_bmi_btn(self):
        txt_h = self._ui.home.height_text()
        txt_w = self._ui.home.weight_text()
        if not _is_num(txt_h):
            self._ui.home.print_msg("Height input error. Please enter a number")
        elif not _is_num(txt_w):
            self._ui.home.print_msg("Weight input error. Please enter a number")
        else:
            today = date.today()
            record = self._stat.get_record(today)
            record = record._replace(weight=float(txt_w))
            record = record._replace(height=float(txt_h))
            self._stat.set_record(today, record)
            self._ui.home.print_msg(self._stat.bmi_msg())
            if self._ui.history.selected_date() == today:
                self._ui.history.show_record(record)
            self._stat.save()

    def _on_water_btn(self, delta: int) -> None:
        print("Updating water...")
        lvl = float(self._stat.water + delta)
        if lvl >= 0.0:
            self._stat.water += delta
            mx = float(self._stat.water_per_day())
            self._ui.home.glass.draw_water(lvl / mx)

    def _on_date_changed(self) -> None:
        print("Fake handling date changing...")

    def _on_save(self) -> None:
        print("Fake Saving...")


def _is_num(v) -> bool:
    try:
        _ = float(v)
        return True
    except:
        return False
