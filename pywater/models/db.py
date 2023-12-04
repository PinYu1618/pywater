from pathlib import Path


class DbHandler:
    def __init__(self, db_path: Path) -> None:
        self._db_path = db_path
