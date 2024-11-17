from src.without_optimization.structures import Point, Road


def test_size():
    points = [
        Point(0, 1),
        Point(0, 0),
        Point(1, 0),
        Point(1, 1),
    ]

    results = [
        {
            "points": [0, 1],
            "value": 1
        },
        {
            "points": [0, 2],
            "value": 1.41
        },
        {
            "points": [0, 3],
            "value": 1
        },
        {
            "points": [1, 2],
            "value": 1
        },
        {
            "points": [1, 3],
            "value": 1.41
        },
        {
            "points": [2, 3],
            "value": 1
        },
    ]

    for result in results:
        road = Road(
            a=points[result['points'][0]],
            b=points[result['points'][1]],
        )
        assert round(road.size, 2) == round(result['value'], 2)


