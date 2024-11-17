from fastapi import APIRouter
from starlette import status

from schemas import PointRequest
from roadmap import Point

router = APIRouter()

# Пока что используем заглушку для того чтобы написать основной функционал без бд.
# После есть варианты чтобы было по типу redis или можно по фастику mysql файлом хранить бдшку
# чтобы было минимальное количество сервисов для развертки проектов

points = []


@router.get("/points")
def get_points():
    return points


@router.post("/points")
def create_point(point: PointRequest):
    max_id = max(points, key=lambda x: x['id'], default=0)
    points.append({
        "id": max_id,
        "point": Point(**point.model_dump())
    })

    return status.HTTP_200_OK
