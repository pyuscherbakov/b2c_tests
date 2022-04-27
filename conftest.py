from pathlib import Path
from loguru import logger
import pytest


@pytest.fixture(autouse=True)
def write_logs(request):
    # put logs in tests/logs
    log_path = Path("tests") / "logs"

    # tidy logs in subdirectories based on test module and class names
    module = request.module
    class_ = request.cls
    name = request.node.name + ".log"

    if module:
        log_path /= module.__name__.replace("tests.", "")
    if class_:
        log_path /= class_.__name__

    log_path.mkdir(parents=True, exist_ok=True)

    # append last part of the name
    log_path /= class_.__name__ + ".log"

    # enable the logger
    logger.remove()
    logger.configure(handlers=[{"sink": log_path,
                                "level": "TRACE",
                                "format": "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}"
                                }])
    logger.enable("my_package")

