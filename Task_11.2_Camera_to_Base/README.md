# Task 11.2 - Camera-to-Base Frame Transformation

## Overview

To convert 3D coordinates from the camera frame (camera_link) to the vehicle's base frame (base_link), two operations are applied:

1. Rotation around the Y-axis using a tilt angle of -15 degrees.
2. Translation using the camera offset:
   - tx = 0.5 m
   - ty = 0.0 m
   - tz = 0.2 m

---

## Mathematical Equations

For each point (x, y, z):

### Rotation

rotated x = x × cos(theta) + z × sin(theta)

rotated z = -x × sin(theta) + z × cos(theta)

### Translation

base x = rotated x + tx

base y = y + ty

base z = rotated z + tz

---

## Step-by-Step Manual Calculations

Given:

- theta = -15 degrees
- cos(-15) ≈ 0.9659
- sin(-15) ≈ -0.2588
- tx = 0.5
- ty = 0.0
- tz = 0.2

### Obstacle 1: [2.0, 0.0, -0.2]

- rotated x = (2.0 × 0.9659) + (-0.2 × -0.2588) = 1.9836
- base x = 1.9836 + 0.5 = 2.48
- base y = 0.0 + 0.0 = 0.00
- rotated z = -(2.0 × -0.2588) + (-0.2 × 0.9659) = 0.3244
- base z = 0.3244 + 0.2 = 0.52

### Obstacle 2: [3.5, 1.0, -0.3]

- rotated x = (3.5 × 0.9659) + (-0.3 × -0.2588) = 3.4583
- base x = 3.4583 + 0.5 = 3.96
- base y = 1.0 + 0.0 = 1.00
- rotated z = -(3.5 × -0.2588) + (-0.3 × 0.9659) = 0.6160
- base z = 0.6160 + 0.2 = 0.82

### Obstacle 3: [1.5, -0.8, -0.1]

- rotated x = (1.5 × 0.9659) + (-0.1 × -0.2588) = 1.4747
- base x = 1.4747 + 0.5 = 1.97
- base y = -0.8 + 0.0 = -0.80
- rotated z = -(1.5 × -0.2588) + (-0.1 × 0.9659) = 0.2916
- base z = 0.2916 + 0.2 = 0.49

---

## Note on Expected Output Discrepancy

- Calculated Result for Obstacle 3: [1.97, -0.80, 0.49]
- Task Description Output: [1.97, -0.8, 0.29]

The value 0.29 in the task prompt is the rotated z value before adding the vertical translation tz = 0.2 m.

Since the camera is mounted 0.2 m higher than the base frame center, the translation must be added.

Therefore, the physically accurate result is:

[1.97, -0.80, 0.49]