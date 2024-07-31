from read_data import read_csv
from visualize import plot
from regularize_curves import regularize_curves
from symmetry_detection import detect_symmetry
from complete_curves import complete_curves

def main():
    # Load and visualize the initial data
    paths_XYs = read_csv('data/isolated.csv')
    plot(paths_XYs)
    
    # Regularize curves
    regularized_paths = regularize_curves(paths_XYs)
    plot(regularized_paths)
    
    # Detect symmetry
    symmetric_paths = detect_symmetry(regularized_paths)
    plot(symmetric_paths)
    
    # Complete curves
    completed_paths = complete_curves(symmetric_paths)
    plot(completed_paths)

if __name__ == "__main__":
    main()
