import pytest

from rpi_backlight import Backlight
from rpi_backlight.utils import FakeBacklightSysfs


def test_get_brightness() -> None:
    with FakeBacklightSysfs() as backlight_sysfs:
        backlight = Backlight(backlight_sysfs_path=backlight_sysfs.path)

        assert backlight.brightness == 100


def test_set_brightness() -> None:
    with FakeBacklightSysfs() as backlight_sysfs:
        backlight = Backlight(backlight_sysfs_path=backlight_sysfs.path)

        backlight.brightness = 50
        assert backlight.brightness == 50

        backlight.brightness = 0
        assert backlight.brightness == 0

        with pytest.raises(TypeError):
            backlight.brightness = "foo"

        with pytest.raises(TypeError):
            backlight.brightness = True

        with pytest.raises(ValueError):
            backlight.brightness = 101

        with pytest.raises(ValueError):
            backlight.brightness = -1


def test_get_power() -> None:
    with FakeBacklightSysfs() as backlight_sysfs:
        backlight = Backlight(backlight_sysfs_path=backlight_sysfs.path)

        assert backlight.power is True


def test_set_power() -> None:
    with FakeBacklightSysfs() as backlight_sysfs:
        backlight = Backlight(backlight_sysfs_path=backlight_sysfs.path)

        backlight.power = False
        assert backlight.power is False

        backlight.power = True
        assert backlight.power is True

        with pytest.raises(TypeError):
            backlight.power = "foo"

        with pytest.raises(TypeError):
            backlight.power = 1
