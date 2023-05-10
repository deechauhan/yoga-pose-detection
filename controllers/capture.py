"""Capture controller.

All things related to capturing frames.
"""
from typing import Any, Callable, TypeVar, cast

import cv2

from settings import Settings

Func = TypeVar("Func", bound=Callable[..., Any])


def get_camera(
    settings: Settings = Settings(),
    precedence: int = 0,
) -> cv2.VideoCapture:
    """Open the camera."""
    camera = cv2.VideoCapture(precedence)  # type:ignore[call-arg]
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, settings.width)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, settings.height)
    camera.set(cv2.CAP_PROP_BUFFERSIZE, 2)
    is_camera_opened(camera=camera)
    return camera


def is_camera_opened(camera: cv2.VideoCapture) -> None:
    """Validate that the camera is open."""
    if not camera.isOpened():
        # TODO: add logging
        exit()


def capture_stream(func: Func) -> Func:
    """Capture realtime decorator."""

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """Wrapper around the function."""
        camera = get_camera()
        while True:
            ret, original_frame = camera.read()
            kwargs["ret"] = ret
            kwargs["original_frame"] = original_frame
            func(*args, **kwargs)
            key = cv2.waitKey(1)
            if key == ord("q"):
                break
        camera.release()
        cv2.destroyAllWindows()

    return cast(Func, wrapper)
