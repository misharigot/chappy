# chappy
Automatic video chapterization.

## Usage

```
usage: app.py [-h] [--word-count WORD_COUNT] [--chapters CHAPTERS] URL

Chapterize a YouTube video.

positional arguments:
  URL                   The URL of the YouTube video to chapterize

optional arguments:
  -h, --help            show this help message and exit
  --word-count WORD_COUNT, -w WORD_COUNT
                        Number of words in the summary for each section.
  --chapters CHAPTERS, -c CHAPTERS
                        Number of chapters to return.
```

## Development guide

1. Build the container.

    ```bash
    docker build -t chappy .
    ```

1. Run the container in the background and mount the repo.

    ```bash
    docker run -dit -v /Users/misha/cs/wdps/chappy:/app/chappy chappy:latest bash
    ```

1. Get into the container's shell.

    ```bash
    docker exec -it <container-name> bash
    ```

1. Set the working directory to the chappy folder.

    ```
    cd chappy
    ```

1. Install Poetry dependencies (+ dev deps) from `pyproject.toml`.

    ```bash
    poetry install
    ```

1. Install the pretrained Neural Network to punctuate text
    ```bash
    download-model.sh
    ```

2. Run it or run the tests.

    ```bash
    poetry run python3 src/app.py https://www.youtube.com/watch?v=Hu4Yvq-g7_Y
    ```

    ```bash
    poetry run pytest
    ```

### Adding packages to your env

Use poetry for this. Example:

```bash
poetry add pandas
```
