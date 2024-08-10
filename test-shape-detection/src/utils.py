import csv
import matplotlib.pyplot as plt
import svgwrite
from typing import List, Tuple

def read_csv(file_path: str) -> List[Tuple[float, float]]:
    """Read CSV file and return a list of tuples (x, y) representing points."""
    points = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            x, y = map(float, row)
            points.append((x, y))
    return points

def plot_curve(points: List[Tuple[float, float]], title: str = "Curve"):
    """Plot a curve given a list of points."""
    x_vals, y_vals = zip(*points)
    plt.figure()
    plt.plot(x_vals, y_vals, marker='o')
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

def save_as_svg(points: List[Tuple[float, float]], file_path: str):
    """Save points as an SVG file."""
    dwg = svgwrite.Drawing(file_path, profile='tiny')
    dwg.add(dwg.polyline(points, stroke=svgwrite.rgb(10, 10, 16, '%'), fill='none'))
    dwg.save()

def save_as_png(svg_path: str, png_path: str):
    """Convert SVG to PNG format."""
    import cairosvg
    cairosvg.svg2png(url=svg_path, write_to=png_path)
