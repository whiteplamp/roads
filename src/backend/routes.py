from fastapi import APIRouter

from src.backend.schemas import PointRequest
from src.without_optimization.structures import Point

router = APIRouter()


points = []


@router.get("/points")
def get_points():
    return


@router.post("/points")
def create_point(point: PointRequest):
    max_id = max(points, key=lambda x: x['id'], default=0)
    points.append({
        "id": max_id,
        "point": Point(**point.model_dump())
    })
