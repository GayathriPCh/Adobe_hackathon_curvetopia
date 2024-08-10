import numpy as np
from src.regularization import detect_straight_lines, detect_circle_ellipse
from src.utils import read_csv, plot_paths
from src.symmetry import detect_symmetry
from src.completion import complete_curves

def main():
    # Load paths from CSV
    input_path = 'data/isolated.csv'
    paths = read_csv(input_path)

    # Regularize straight lines and circles/ellipses
    paths = detect_straight_lines(paths)
    paths = detect_circle_ellipse(paths)
    paths = detect_symmetry(paths)
    paths = complete_curves(paths)
    # Plot and save the regularized paths
    output_svg = 'output/regularized_shapes.svg'
    plot_paths(paths, output_svg)

if __name__ == "__main__":
    main()
