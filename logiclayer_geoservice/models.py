from enum import Enum, auto
from pathlib import Path as FilePath
from typing import TypedDict


class LevelDescriptor(TypedDict):
    shape_path: FilePath


class RelationsMode(Enum):
    Parents = auto()
    Children = auto()
    Intersects = auto()
    Distance = auto()
