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
        self.view.set_status(self._encourage())

    def _connect_signals(self):
        self.view.btnsub.clicked.connect(partial(self._add_water, -100))
        self.view.btn100.clicked.connect(partial(self._add_water, 100))
        self.view.btn200.clicked.connect(partial(self._add_water, 200))
        self.view.btn500.clicked.connect(partial(self._add_water, 500))
        self.view.btn_bmi.clicked.connect(self._calc_bmi)

    def _calc_bmi(self):
        txt_h = self.view.height_text()
        txt_w = self.view.weight_text()
        if not _is_num(txt_h):
            self.view.set_status("Height input error")
        elif not _is_num(txt_w):
            self.view.set_status("Weight input error")
        else:
            print("Calculating...")
            bmi_msg = self._bmi(float(txt_h), float(txt_w))
            self.view.set_status(bmi_msg)

    def _add_water(self, amount: int) -> None:
        print("Adding water...")
        print(amount)
        lvl_old = self.view.glass._waterLvl
        self.view.glass.setup_animation(lvl_old + amount)


def _is_num(v) -> bool:
    try:
        _ = float(v)
        return True
    except:
        return False
