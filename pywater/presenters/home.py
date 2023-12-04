from functools import partial

from ..views.home import HomeView


class HomePresenter:
    def __init__(self, view: HomeView, encourage: callable) -> None:
        self.view = view
        self._encourage = encourage
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
        print("Calculating...")

    def _add_water(self, amount: int) -> None:
        print("Adding water...")
        print(amount)
        lvl_old = self.view.glass._waterLvl
        self.view.glass.setup_animation(lvl_old + amount)
