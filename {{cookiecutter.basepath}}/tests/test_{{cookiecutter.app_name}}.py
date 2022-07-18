from pathlib import Path
import pytest
import platform
import sys

self_pth = Path(__file__)
dir_test = self_pth.parent
dir_prj = dir_test.parent

sys.path.insert(0, str(dir_prj))

from {{cookiecutter.app_name}} import __version__, version_info, getname

def test_getname() -> None:
    res = getname()
    assert "hello" in res


def test_version() -> None:
    """
    Given: Nothing
    When: version_info is called
    Then: the expected output is given
    """
    result = version_info()

    assert sys.version.split(" ", maxsplit=1)[0] in result
    assert platform.platform() in result
    assert __version__ in result
