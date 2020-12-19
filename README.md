# chappy
Automatic video chapterization.

## Usage

```
usage: app.py [-h] [--word-count WORD_COUNT] [--chapters CHAPTERS]

Chapterize a YouTube video.

optional arguments:
  -h, --help            show this help message and exit
  --word-count WORD_COUNT, -w WORD_COUNT
                        Number of words in the summary for each section.
  --chapters CHAPTERS, -c CHAPTERS
                        Number of chapters to return.
```

## Running in a Docker container

The following describes how to run the app in a Docker container by first building the image from the `Dockerfile`.

1. Build the container

    ```bash
    cd path/to/chappy
    docker build -t chappy .
    ```

1. Run the container and run the app

    ```bash
    docker run -it chappy bash

    # Inside the container
    $ poetry run python3 src/app.py <youtube URL>
    ```

## Development guide

You can re-use the above container and simply mount your locally checked-out repository.

1. Build the container.

    ```bash
    docker build -t chappy .
    ```

1. Download the punctuator model locally, since it will be mounted in the next step:

    ```bash
    ./download-model.sh
    ```

1. Run the container in the background and mount the local repo.

    ```bash
    docker run -dit -v /path/to/chappy:/app/chappy chappy:latest bash
    ```

1. Get into the container's shell.

    ```bash
    docker exec -it <container-name> bash
    ```
1. Run it or run the tests.

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
