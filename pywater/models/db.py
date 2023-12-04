import json
from pathlib import Path
from typing import Any, Dict, List, NamedTuple


class DBResponse(NamedTuple):
    todo_list: List[Dict[str, Any]]
    success: bool


class DbHandler:
    def __init__(self, db_path: Path) -> None:
        self._db_path = db_path

    def read(self) -> DBResponse:
        try:
            with self._db_path.open("r") as db:
                try:
                    return DBResponse(json.load(db), True)
                except json.JSONDecodeError:  # Catch wrong JSON format
                    return DBResponse([], False)
        except OSError:  # Catch file IO problems
            return DBResponse([], False)

    def write(self, lst: List[Dict[str, Any]]) -> DBResponse:
        try:
            with self._db_path.open("w") as db:
                json.dump(lst, db, indent=4)
            return DBResponse(lst, True)
        except OSError:  # Catch file IO problems
            return DBResponse(lst, False)
