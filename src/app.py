import sys

from chapterizer import Chapterizer


def main():
    if len(sys.argv) != 2:
        raise ValueError("No argument given.")
    arg = sys.argv[1]

    chappy = Chapterizer(url=arg, summary_word_count=30)
    chappy.chapterize()
    chappy.print()


if __name__ == "__main__":
    main()
