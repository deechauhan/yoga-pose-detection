"""Model controller."""
from functools import cache

from torch import Tensor
from ultralytics import YOLO  # type:ignore[import]
from ultralytics.yolo.engine.results import Results  # type:ignore[import]

from settings import Settings


@cache
def get_yolov8_model(settings: Settings = Settings()) -> YOLO:
    """Return the yolov8 model from ultralytics."""
    return YOLO(settings.yolov8_model_path)


def predict_person(frame: Tensor) -> Results:
    """Predict the person and keypoints for the given frame."""
    model = get_yolov8_model()
    return model(frame)[0]
