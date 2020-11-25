import sys

from chapterizator import Chapterizator


def main():
    if len(sys.argv) != 2:
        raise ValueError("No argument given.")
    arg = sys.argv[1]

    chappy = Chapterizator(url=arg)
    chappy.chapterize()
    chappy.print()


if __name__ == "__main__":
    main()
