import argparse

from chapterizer import Chapterizer


def main():
    parser = argparse.ArgumentParser(description="Chapterize a YouTube video.")
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
    chappy = Chapterizer(
        summary_word_count=args.word_count, number_of_chapters=args.chapters
    )

    print_chappy_splash_ascii()

    while True:
        urls = input(
            "\n-----\nPlease provide one (or more, space seperated) YouTube URL(s) you wish to chapterize: "
        ).split(" ")

        # Chapterize YouTube video
        for url in urls:
            try:
                chapterized_youtube_video = chappy.chapterize(url=url)
                chapterized_youtube_video.print_chapters()
            except Exception:
                print(f"Could not retrieve a transcript for the video {url}!")



def print_chappy_splash_ascii():
    print(
        """
   ________                           
  / ____/ /_  ____ _____  ____  __  __
 / /   / __ \/ __ `/ __ \/ __ \/ / / /
/ /___/ / / / /_/ / /_/ / /_/ / /_/ / 
\____/_/ /_/\__,_/ .___/ .___/\__, /  
                /_/   /_/    /____/   
    """
    )


if __name__ == "__main__":
    main()
