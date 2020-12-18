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

    # Initialize Chapterizer
    chappy = Chapterizer(summary_word_count=args.word_count, number_of_chapters=args.chapters)
    chappy.segmentizer = SimpleSegmentizer(n_parts=args.chapters)

    # Chapterize YouTube video
    chapterized_youtube_video = chappy.chapterize(url=args.url)
    chapterized_youtube_video.print_chapters()


if __name__ == "__main__":
    main()
