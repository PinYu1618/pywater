from functools import partial
from typing import Callable

import matplotlib

matplotlib.use("Qt5Agg")

from .views import View
from .models.stat import Stat
from .models.db import DbHandler


class Presenter:
    def __init__(
        self,
        view: View,
        stat: Stat,
        db: DbHandler,
        encourage: Callable,
        bmi: Callable,
    ) -> None:
        self._ui = view
        self._encourage = encourage
        self._bmi = bmi
        self._stat = stat
        self._db = db
        self._init_ui()
        self._connect_signals()

    def _init_ui(self):
        lvl = float(self._stat.water)
        mx = float(self._stat.water_per_day())
        self._ui.home.glass.update_water(lvl / mx)
        self._ui.home.print_msg(self._encourage())
        self._stat.df.plot(ax=self._ui.analysis.sc.axes)

    def _connect_signals(self):
        self._ui.home.btnsub.clicked.connect(partial(self._update_water, -100))
        self._ui.home.btn100.clicked.connect(partial(self._update_water, 100))
        self._ui.home.btn200.clicked.connect(partial(self._update_water, 200))
        self._ui.home.btn500.clicked.connect(partial(self._update_water, 500))
        self._ui.home.btn_bmi.clicked.connect(self._calc_bmi)

    def _calc_bmi(self):
        txt_h = self._ui.home.height_text()
        txt_w = self._ui.home.weight_text()
        if not _is_num(txt_h):
            self._ui.home.print_msg("Height input error. Please enter a number")
        elif not _is_num(txt_w):
            self._ui.home.print_msg("Weight input error. Please enter a number")
        else:
            print("Calculating...")
            bmi_msg = self._bmi(float(txt_h), float(txt_w))
            self._ui.home.print_msg(bmi_msg)

    def _update_water(self, delta: int) -> None:
        print("Updating water...")
        lvl = float(self._stat.water + delta)
        if lvl >= 0.0:
            self._stat.water += delta
            mx = float(self._stat.water_per_day())
            self._ui.home.glass.update_water(lvl / mx)


def _is_num(v) -> bool:
    try:
        _ = float(v)
        return True
    except:
        return False
