"""Main launcher."""
import cv2
from torch import Tensor
from ultralytics.yolo.engine.results import Results  # type: ignore[import]

from controllers.capture import capture_stream
from controllers.models import predict_person

# from schemas.keypoints import KeyPoints


@capture_stream
def run(ret: Tensor, original_frame: Tensor) -> None:
    """Predict person."""

    if not ret:
        return

    # Predict the key points and pose
    res: Results = predict_person(frame=original_frame)

    # Show the prediction in real time
    cv2.imshow(
        winname="Yoga pose detection",
        mat=res.plot(
            probs=False,
            conf=False,
            labels=False,
            boxes=False,
            masks=False,
        ),
    )

    # Map the keypoints to human body components
    # keypoints = KeyPoints.parse_numpy(res.keypoints[0])
