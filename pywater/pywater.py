from functools import partial
from typing import Callable
from pathlib import Path
from datetime import date

import matplotlib

matplotlib.use("Qt5Agg")

from .views import View
from .models.stat import Stat, Record


class PyWater:
    def __init__(self, db_path: Path, view: View, encourage: Callable) -> None:
        self._ui = view
        self._encourage = encourage
        self._stat = Stat(db_path)
        self._init_ui()
        self._connect_signals()

    def _init_ui(self):
        record = self._stat.get_record(date.today())
        if record is not None:
            lvl = float(record.water)
            mx = float(self._stat.water_per_day(record.weight))
            self._ui.home.glass.draw_water(lvl / mx)
            self._ui.home.print_msg(self._encourage())
            self._ui.home.show_water_label(lvl, mx)
            self._ui.history.show_record(record)
        else:
            self._on_no_today()
        # if not self._stat.df.empty:
        #    self._stat.df.plot(ax=self._ui.analysis.sc.axes)

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
            if record is not None:
                record = record._replace(weight=float(txt_w))
                record = record._replace(height=float(txt_h))
                self._stat.set_record(today, record)
                self._ui.home.print_msg(self._stat.bmi_msg())
                if self._ui.history.selected_date() == today:
                    self._ui.history.show_record(record)
                self._stat.save()
                mx = float(self._stat.water_per_day(record.weight))
                self._ui.home.show_water_label(record.water, mx)
                self._ui.home.glass.draw_water(min(record.water / mx, 1.0))
            else:
                self._on_no_today()

    def _on_water_btn(self, delta: int) -> None:
        today = date.today()
        record = self._stat.get_record(today)
        if record is not None:
            record = record._replace(water=max(0.0, record.water + delta))
            self._stat.set_record(today, record)
            mx = float(self._stat.water_per_day(record.weight))
            self._ui.home.glass.draw_water(min(record.water / mx, 1.0))
            self._ui.home.show_water_label(record.water, mx)
            if self._ui.history.selected_date() == today:
                self._ui.history.show_record(record)
            self._stat.save()

    def _on_date_changed(self) -> None:
        dt = self._ui.history.selected_date()
        maybe_record = self._stat.get_record(dt)
        self._ui.history.show_date(dt)
        if maybe_record is None:
            self._ui.history.clear_record()
        else:
            self._ui.history.show_record(maybe_record)

    def _on_save(self) -> None:
        h_txt = self._ui.history.input_height()
        w_txt = self._ui.history.input_weight()
        wat_txt = self._ui.history.input_water()
        if not _is_num(h_txt):
            self._ui.history.show_status("Height input error. Please enter a number")
        elif not _is_num(w_txt):
            self._ui.history.show_status("Weight input error. Please enter a number")
        elif not _is_num(wat_txt):
            self._ui.history.show_status("Water input error. Please enter a number")
        else:
            record = Record(float(wat_txt), float(w_txt), float(h_txt))
            dt = self._ui.history.selected_date()
            self._stat.set_record(dt, record)
            self._stat.save()
            self._ui.history.show_status("Record updated!")

    def _on_no_today(self):
        print("No today record!")


def _is_num(v) -> bool:
    try:
        _ = float(v)
        return True
    except:
        return False
