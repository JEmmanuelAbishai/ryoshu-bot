import pytest

from src.core.exceptions import InvalidDurationError
from src.utils.time_parser import parse_duration


def test_parses_minutes():
    delta = parse_duration("10m")
    assert delta.total_seconds() == 600


def test_parses_hours():
    delta = parse_duration("2h")
    assert delta.total_seconds() == 7200


def test_parses_days():
    delta = parse_duration("1d")
    assert delta.total_seconds() == 86400


def test_rejects_malformed_input():
    with pytest.raises(InvalidDurationError):
        parse_duration("banana")


def test_rejects_exceeding_max_days():
    with pytest.raises(InvalidDurationError):
        parse_duration("29d")


def test_rejects_zero_duration():
    with pytest.raises(InvalidDurationError):
        parse_duration("0m")
