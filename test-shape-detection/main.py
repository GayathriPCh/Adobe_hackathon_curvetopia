from src.utils import read_csv, plot_curve, save_as_svg, save_as_png

# Step 1: Read the CSV file
points = read_csv('tests/csv/test_curve.csv')

# Step 2: Plot the curve
plot_curve(points, title="Test Curve")

# Step 3: Save the curve as SVG
save_as_svg(points, 'tests/svg/test_curve.svg')

# Step 4: Convert SVG to PNG
save_as_png('tests/svg/test_curve.svg', 'tests/png/test_curve.png')
