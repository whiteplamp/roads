from src.without_optimization.generator import Generator
from src.without_optimization.visualizer import Visualizer

generator = Generator(points=12, roads=0, map_size_x=800, map_size_y=600)


_map = generator.generate_map_with_all_roads()

print(_map)


visualizer = Visualizer(_map=_map)

visualizer.draw()
