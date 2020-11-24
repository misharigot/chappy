import sys
from youtube_video import YoutubeVideo


def main():
    if len(sys.argv) != 2:
        raise ValueError("No argument given.")
    arg = sys.argv[1]
    print(f"Processing: {arg}\n")
    youtube_video = YoutubeVideo(arg)
    print(youtube_video.segmentize())
    index = youtube_video.segmentize()[-1]["starts_at_index"]
    print("\nlast transcript item:\n", youtube_video.transcript[index])
    print("\nnumber of items in transcript:\n", len(youtube_video.transcript))


if __name__ == "__main__":
    main()
