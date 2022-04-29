from pathlib import Path
from loguru import logger
import pytest


# TODO: Ссылки на оплату


@pytest.fixture(autouse=True)
def write_logs(request):
    log_path = Path("tests") / "b2c" / "logs"

    module = request.module
    class_ = request.cls
    name = request.node.originalname + ".log"

    if module:
        log_path /= module.__name__.replace("tests.", "")
    if class_:
        log_path /= class_.__name__

    log_path.mkdir(parents=True, exist_ok=True)

    log_path /= name

    logger.remove()
    logger.configure(handlers=[{"sink": log_path,
                                "level": "DEBUG",
                                "format": "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
                                "rotation": "2 days",
                                "compression": "zip"
                                }])
    logger.enable("my_package")
