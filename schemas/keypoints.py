"""Body keypoints schema."""
from typing import Self

from pydantic import BaseModel, Field
from torch import Tensor

index_body_part_mapping = {
    "nose": 0,
    "r_eye": 1,
    "l_eye": 2,
    "r_ear": 3,
    "l_ear": 4,
    "r_shoulder": 5,
    "l_shoulder": 6,
    "r_elbow": 7,
    "l_elbow": 8,
    "r_wrist": 9,
    "l_wrist": 10,
    "r_hip": 11,
    "l_hip": 12,
    "r_knee": 13,
    "l_knee": 14,
    "r_ankle": 15,
    "l_ankle": 16,
}


class BodyPart(BaseModel):
    """Body part tracking details."""

    x: float
    y: float
    confidence: float = Field(le=1, ge=0)  # confidence can only be between 0-1

    @classmethod
    def parse_numpy(cls, nd_array: Tensor) -> Self:
        """Parse instance from ndarray."""
        return cls(
            x=nd_array[0],
            y=nd_array[1],
            confidence=nd_array[2],
        )


class KeyPoints(BaseModel):
    """Keypoint of human pose model."""

    nose: BodyPart
    r_shoulder: BodyPart
    r_elbow: BodyPart
    r_wrist: BodyPart
    l_shoulder: BodyPart
    l_elbow: BodyPart
    l_wrist: BodyPart
    r_hip: BodyPart
    r_knee: BodyPart
    r_ankle: BodyPart
    l_hip: BodyPart
    l_knee: BodyPart
    l_ankle: BodyPart
    r_eye: BodyPart
    l_eye: BodyPart
    r_ear: BodyPart
    l_ear: BodyPart

    @classmethod
    def parse_numpy(cls, nd_array: Tensor) -> Self:
        """Parse instance from ndarray."""
        return cls(
            nose=BodyPart.parse_numpy(nd_array=nd_array[0]),
            r_shoulder=BodyPart.parse_numpy(nd_array=nd_array[5]),
            r_elbow=BodyPart.parse_numpy(nd_array=nd_array[7]),
            r_wrist=BodyPart.parse_numpy(nd_array=nd_array[9]),
            l_shoulder=BodyPart.parse_numpy(nd_array=nd_array[6]),
            l_elbow=BodyPart.parse_numpy(nd_array=nd_array[8]),
            l_wrist=BodyPart.parse_numpy(nd_array=nd_array[10]),
            r_hip=BodyPart.parse_numpy(nd_array=nd_array[11]),
            r_knee=BodyPart.parse_numpy(nd_array=nd_array[13]),
            r_ankle=BodyPart.parse_numpy(nd_array=nd_array[15]),
            l_hip=BodyPart.parse_numpy(nd_array=nd_array[12]),
            l_knee=BodyPart.parse_numpy(nd_array=nd_array[14]),
            l_ankle=BodyPart.parse_numpy(nd_array=nd_array[16]),
            r_eye=BodyPart.parse_numpy(nd_array=nd_array[1]),
            l_eye=BodyPart.parse_numpy(nd_array=nd_array[2]),
            r_ear=BodyPart.parse_numpy(nd_array=nd_array[3]),
            l_ear=BodyPart.parse_numpy(nd_array=nd_array[4]),
        )
