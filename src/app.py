import sys
import argparse

from chapterizer import Chapterizer
from simple_segmentizer import SimpleSegmentizer


def main():

    parser = argparse.ArgumentParser(description="Chapterize a YouTube video.")
    parser.add_argument(
        "url",
        metavar="URL",
        type=str,
        help="The URL of the YouTube video to chapterize",
    )
    parser.add_argument(
        "--word-count",
        "-w",
        default=30,
        type=int,
        help="Number of words in the summary for each section.",
    )
    parser.add_argument(
        "--chapters", "-c", default=10, type=int, help="Number of chapters to return."
    )

    args = parser.parse_args()

    chappy = Chapterizer(url=args.url, summary_word_count=args.word_count)
    chappy.segmentizer = SimpleSegmentizer(chappy.youtube_video, n_parts=args.chapters)
    chappy.chapterize()
    chappy.print()


if __name__ == "__main__":
    main()
