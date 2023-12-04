from functools import partial
from typing import Callable

from .views.home import HomeView


class Presenter:
    def __init__(self, _v_home: HomeView, encourage: Callable, bmi: Callable) -> None:
        self._v_home = _v_home
        self._encourage = encourage
        self._bmi = bmi
        self._init_ui()
        self._connect_signals()

    def _init_ui(self):
        self._v_home.print_msg(self._encourage())

    def _connect_signals(self):
        self._v_home.btnsub.clicked.connect(partial(self._update_water, -100))
        self._v_home.btn100.clicked.connect(partial(self._update_water, 100))
        self._v_home.btn200.clicked.connect(partial(self._update_water, 200))
        self._v_home.btn500.clicked.connect(partial(self._update_water, 500))
        self._v_home.btn_bmi.clicked.connect(self._calc_bmi)

    def _calc_bmi(self):
        txt_h = self._v_home.height_text()
        txt_w = self._v_home.weight_text()
        if not _is_num(txt_h):
            self._v_home.print_msg("Height input error. Please enter a number")
        elif not _is_num(txt_w):
            self._v_home.print_msg("Weight input error. Please enter a number")
        else:
            print("Calculating...")
            bmi_msg = self._bmi(float(txt_h), float(txt_w))
            self._v_home.print_msg(bmi_msg)

    def _update_water(self, delta: int) -> None:
        print("Updating water...")
        lvl_old = self._v_home.glass.water_level
        self._v_home.glass.update_water(lvl_old + delta)


def _is_num(v) -> bool:
    try:
        _ = float(v)
        return True
    except:
        return False
