import re
from datetime import timedelta

from src.core.exceptions import InvalidDurationError

_UNIT_TO_KWARG = {
    "s": "seconds",
    "m": "minutes",
    "h": "hours",
    "d": "days"
}

_PATTERN = re.compile(r"(\d+)([smhd])")

_MAX_TIMEOUT_DAYS = 28

def parse_duration(duration_str: str) -> timedelta:
    match = _PATTERN.fullmatch(duration_str.strip().lower())
    if not match:
        raise InvalidDurationError(f"Invalid duration format: '{duration_str}'")

    amount, unit = match.groups()
    kwarg = _UNIT_TO_KWARG[unit]
    delta = timedelta(**{kwarg: int(amount)})

    if delta > timedelta(days=_MAX_TIMEOUT_DAYS):
        raise InvalidDurationError(f"Duration exceeds maximum allowed timeout of {_MAX_TIMEOUT_DAYS} days.")

    if delta.total_seconds() <= 0:
        raise InvalidDurationError("Duration must be greater than zero.")

    return delta