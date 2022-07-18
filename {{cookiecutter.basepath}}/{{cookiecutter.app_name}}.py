
import platform
import sys
from textwrap import dedent


__version__ = "0.1.0"


def getname():
    return "hello"

def version_info() -> str:
    """Display the version of the program, python and the platform."""
    return dedent(
        f"""\
        ------------------------------------------------------------------
             {{cookiecutter.basepath}}: {__version__}
             Python: {sys.version.split(" ", maxsplit=1)[0]}
             Platform: {platform.platform()}
        ------------------------------------------------------------------"""
    )


def main():
    print("hello {{cookiecutter.loc}}")
 
if __name__ == '__main__':
    main()