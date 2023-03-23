import sys
from .cli import run


def main():
    return run(sys.argv[1])


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
