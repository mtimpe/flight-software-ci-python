# test_rocket.py

import pytest

from .context import rocket


def test_read_sensor():
    # Test if value returned by sensor is in range
    val = rocket.read_sensor()
    assert 20 <= val <= 30

def test_rocket_name():
    # Test if function uppercases name
    assert rocket.rocket_name('piccard') == 'PICCARD'

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        rocket.rocket_name(9)

def test_tw_ratio():
    # Test if thrust-to-weight calculation is correct
    assert rocket.tw_ratio(1,2) == 0.5

def test_imperial_to_metric():
    # Test if conversion is correct (to within one part in a million)
    assert rocket.imperial_to_metric(19500) == pytest.approx(5943.6, 1e-6)

def test_metric_to_imperial():
    # Test if conversion is correct (to within one part in a million)
    assert rocket.metric_to_imperial(5943.6) == pytest.approx(19500, 1e-6)
