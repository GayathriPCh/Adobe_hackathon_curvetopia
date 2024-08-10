import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def read_csv(file_path):
    """Read a CSV file and return the paths as a list of numpy arrays."""
    paths = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            points = np.array([float(x) for x in row]).reshape(-1, 2)
            paths.append(points)
    return paths

def plot_paths(paths, output_file):
    """Plot and save paths as an SVG file."""
    fig, ax = plt.subplots()
    for path in paths:
        polygon = Polygon(path, closed=True, fill=None, edgecolor='r')
        ax.add_patch(polygon)
    ax.set_aspect('equal', 'box')
    ax.autoscale()
    plt.axis('off')
    plt.savefig(output_file, format='svg', bbox_inches='tight')
    plt.close()

def save_svg(paths, output_file):
    """Save the regularized paths as an SVG file."""
    fig, ax = plt.subplots()
    for path in paths:
        ax.plot(path[:, 0], path[:, 1], 'r-', linewidth=2)
    ax.set_aspect('equal', 'box')
    plt.axis('off')
    plt.savefig(output_file, format='svg', bbox_inches='tight')
    plt.close()

def path_to_svg_string(path):
    """Convert a numpy path array to an SVG path string."""
    svg_path = "M " + " L ".join([f"{x},{y}" for x, y in path]) + " Z"
    return svg_path

def create_svg(paths):
    """Create an SVG content from paths."""
    svg_content = '<svg xmlns="http://www.w3.org/2000/svg" version="1.1">'
    for path in paths:
        svg_path_string = path_to_svg_string(path)
        svg_content += f'<path d="{svg_path_string}" stroke="black" fill="none"/>'
    svg_content += '</svg>'
    return svg_content

def save_svg_directly(paths, output_file):
    """Save paths directly to an SVG file."""
    svg_content = create_svg(paths)
    with open(output_file, 'w') as f:
        f.write(svg_content)
