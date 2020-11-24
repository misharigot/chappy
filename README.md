# chappy
Automatic video chapterization.

## Development guide

1. Build the container.

    ```bash
    docker build -t chappy .
    ```

1. Run the container in the background and mount the repo.

    ```bash
    docker run -d -v /Users/misha/cs/wdps/chappy:/app/chappy chappy:latest bash
    ```

1. Get into the container's shell.

    ```bash
    docker exec -it <container-name> bash
    ```

1. Install Poetry dependencies (+ dev deps) from `pyproject.toml`.

    ```bash
    poetry install
    ```

2. Run it or run the tests.

    ```bash
    poetry run python3 src/app.py https://www.youtube.com/watch?v=Hu4Yvq-g7_Y
    ```

    ```bash
    poetry run pytest
    ```
