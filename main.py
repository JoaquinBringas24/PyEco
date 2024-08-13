import pathlib
from libs.classes import country

WORK_DIR = pathlib.Path(__file__).parent.resolve()

def main():
    mexico = country.Country(0.4, 3000)

    print(mexico._population)

    mexico.grow()

    print(mexico._population)


if __name__ == "__main__":
    main()