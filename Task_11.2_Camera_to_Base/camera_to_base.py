import math
 # Given 
points = [ [2.0, 0.0, -0.2],[3.5, 1.0, -0.3],[1.5, -0.8, -0.1] ]
tx = 0.5
ty = 0.0
tz = 0.2
theta = math.radians(-15)

# Calculations
cos_theta = math.cos(theta)
sin_theta = math.sin(theta)

print("Transformed Coordinates in Base Frame:")

for i in range(len(points)):
    x, y, z = points[i]

    # Apply rotation around the Y-axis
    rotated_x = x * cos_theta + z * sin_theta
    rotated_z = -x * sin_theta + z * cos_theta

    # Apply translation from camera frame to base frame
    base_x = rotated_x + tx
    base_y = y + ty
    base_z = rotated_z + tz

    print(f"Obstacle {i+1}: [{base_x:.2f}, {base_y:.2f}, {base_z:.2f}]")