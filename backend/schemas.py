from pydantic import BaseModel


class PointRequest(BaseModel):
    pos_x: int
    pos_y: int
