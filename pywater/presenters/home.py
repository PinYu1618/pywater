from functools import partial

from ..views.home import HomeView


class HomePresenter:
    def __init__(self, view: HomeView, encourage: callable, bmi: callable) -> None:
        self.view = view
        self._encourage = encourage
        self._bmi = bmi
        self._init_ui()
        self._connect_signals()

    def _init_ui(self):
        self.view.print_msg(self._encourage())

    def _connect_signals(self):
        self.view.btnsub.clicked.connect(partial(self._update_water, -100))
        self.view.btn100.clicked.connect(partial(self._update_water, 100))
        self.view.btn200.clicked.connect(partial(self._update_water, 200))
        self.view.btn500.clicked.connect(partial(self._update_water, 500))
        self.view.btn_bmi.clicked.connect(self._calc_bmi)

    def _calc_bmi(self):
        txt_h = self.view.height_text()
        txt_w = self.view.weight_text()
        if not _is_num(txt_h):
            self.view.print_msg("Height input error. Please enter a number")
        elif not _is_num(txt_w):
            self.view.print_msg("Weight input error. Please enter a number")
        else:
            print("Calculating...")
            bmi_msg = self._bmi(float(txt_h), float(txt_w))
            self.view.print_msg(bmi_msg)

    def _update_water(self, delta: int) -> None:
        print("Updating water...")
        lvl_old = self.view.glass.water_level
        self.view.glass.update_water(lvl_old + delta)


def _is_num(v) -> bool:
    try:
        _ = float(v)
        return True
    except:
        return False
