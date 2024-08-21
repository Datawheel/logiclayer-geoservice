from typing import Annotated, Dict

import logiclayer as ll
from fastapi import Depends, Path

from .dependencies import validate_range
from .models import LevelDescriptor, RelationsMode


class GeoserviceModule(ll.LogicLayerModule):
    def __init__(self, shapes: Dict[str, LevelDescriptor]):
        self.shape_map = shapes

    @ll.route("GET", "/coordinates")
    def get_coordinates(self):
        pass

    @ll.route("GET", "/neighbors/{geo_id}")
    def get_neighbors(self, geo_id: str):
        pass

    @ll.route("GET", "/relations/{mode}/{geo_id}")
    def get_relations(
        self,
        mode: Annotated[RelationsMode, Path()],
        geo_id: str,
        levels: str = "",
        overlap: bool = False,
        range_: int = Depends(validate_range),
    ):
        pass
