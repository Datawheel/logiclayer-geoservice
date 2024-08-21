from typing import Annotated

from fastapi import HTTPException, Path

from .models import RelationsMode


def validate_range(mode: Annotated[RelationsMode, Path()], range_: int = 0) -> int:
    if mode == RelationsMode.Distance and range_ == 0:
        message = "Invalid value for range. In 'distance' mode, 'range' is required and must be greater than 0."
        raise HTTPException(400, message)

    return range_
