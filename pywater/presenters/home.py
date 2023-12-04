from functools import partial

from ..views.home import HomeView


class HomePresenter:
    def __init__(self, view: HomeView, encourage: callable) -> None:
        self.view = view
        self.view.set_status(encourage())
        self._connect_signals()

    def _connect_signals(self):
        self.view.btnsub.clicked.connect(partial(self._add_water, -100))
        self.view.btn100.clicked.connect(partial(self._add_water, 100))
        self.view.btn200.clicked.connect(partial(self._add_water, 200))
        self.view.btn500.clicked.connect(partial(self._add_water, 500))

    def _add_water(self, amount: int) -> None:
        print("Adding water...")
        print(amount)
        lvl_old = self.view.glass._waterLvl
        self.view.glass.setup_animation(lvl_old + amount)
