import sys
from youtube_video import YoutubeVideo


def main():
    if len(sys.argv) != 2:
        raise ValueError("No argument given.")
    arg = sys.argv[1]
    print(f"Processing: {arg}")
    youtube_video = YoutubeVideo(arg)
    print(youtube_video.segmentize())
    


if __name__ == "__main__":
    main()
