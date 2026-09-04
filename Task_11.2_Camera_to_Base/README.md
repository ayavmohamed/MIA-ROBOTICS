# Task 11.2 - Camera-to-Base Frame Transformation

## Overview
To convert 3D coordinates from the camera frame (camera_link) to the vehicle's base frame (base_link), two operations must be applied to each detected obstacle point:

1. Rotation around the Y-axis: Adjusts for the camera's tilt angle ($\theta = -15^\circ$).
2. Translation: Adjusts for the physical mounting offset of the camera relative to the center of the car ($t_x = 0.5\text{ m}$, $t_y = 0.0\text{ m}$, $t_z = 0.2\text{ m}$).

---

## Mathematical Equations

For any point $(x, y, z)$ in the camera frame:

* Rotated Coordinates:
  $$\text{rotated\_x} = x \cdot \cos(\theta) + z \cdot \sin(\theta)$$
  $$\text{rotated\_z} = -x \cdot \sin(\theta) + z \cdot \cos(\theta)$$

* Final Base Frame Coordinates:
  $$x_{\text{base}} = \text{rotated\_x} + t_x$$
  $$y_{\text{base}} = y + t_y$$
  $$z_{\text{base}} = \text{rotated\_z} + t_z$$

---

## Manual Calculations

Given constants:
* $\theta = -15^\circ \implies \cos(-15^\circ) \approx 0.9659, \quad \sin(-15^\circ) \approx -0.2588$
* Translation vector: $(t_x, t_y, t_z) = (0.5, 0.0, 0.2)$

### Obstacle 1: [2.0, 0.0, -0.2]
* $\text{rotated\_x} = (2.0 \times 0.9659) + (-0.2 \times -0.2588) = 1.9318 + 0.0518 = 1.9836$
* $x_{\text{base}} = 1.9836 + 0.5 = \mathbf{2.48}$
* $y_{\text{base}} = 0.0 + 0.0 = \mathbf{0.00}$
* $\text{rotated\_z} = -(2.0 \times -0.2588) + (-0.2 \times 0.9659) = 0.5176 - 0.1932 = 0.3244$
* $z_{\text{base}} = 0.3244 + 0.2 = \mathbf{0.52}$

### Obstacle 2: [3.5, 1.0, -0.3]
* $\text{rotated\_x} = (3.5 \times 0.9659) + (-0.3 \times -0.2588) = 3.3807 + 0.0776 = 3.4583$
* $x_{\text{base}} = 3.4583 + 0.5 = \mathbf{3.96}$
* $y_{\text{base}} = 1.0 + 0.0 = \mathbf{1.00}$
* $\text{rotated\_z} = -(3.5 \times -0.2588) + (-0.3 \times 0.9659) = 0.9058 - 0.2898 = 0.6160$
* $z_{\text{base}} = 0.6160 + 0.2 = \mathbf{0.82}$

### Obstacle 3: [1.5, -0.8, -0.1]
* $\text{rotated\_x} = (1.5 \times 0.9659) + (-0.1 \times -0.2588) = 1.4488 + 0.0259 = 1.4747$
* $x_{\text{base}} = 1.4747 + 0.5 = \mathbf{1.97}$
* $y_{\text{base}} = -0.8 + 0.0 = \mathbf{-0.80}$
* $\text{rotated\_z} = -(1.5 \times -0.2588) + (-0.1 \times 0.9659) = 0.3882 - 0.0966 = 0.2916$
* $z_{\text{base}} = 0.2916 + 0.2 = \mathbf{0.49}$

---

## Note on Expected Output Discrepancy

* Calculated Result for Obstacle 3: [1.97, -0.80, 0.49]
* Task Description Output: [1.97, -0.8, 0.29]

Reason:
The value 0.29 in the task prompt corresponds to rotated_z before adding the vertical camera translation offset ($t_z = 0.2\text{ m}$). 

Since the camera is physically mounted $0.2\text{ m}$ higher than the base frame center, adding $t_z$ is required for physical accuracy, which yields the final result of $0.49\text{ m}$.