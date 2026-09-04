# Task 11.1 - Build Your Own Robot

## Overview

In this task, I built a 4-wheel race car using ROS 2, XACRO, Gazebo Harmonic, and RViz.

The robot has a base, four wheels, a front camera, and a differential drive system controlled using /cmd_vel.

## Robot Model

The robot was created using XACRO in:
urdf/race_car.xacro

It contains:
- Base link.
- Four wheels with continuous joints.
- XACRO wheel macro to avoid repeating code.
- Front camera (camera_link).
- Visual and collision geometry.
- Mass and inertia properties.
- Different materials for the robot parts.
- Differential drive plugin.

## Launch File

The launch file is:
launch/race_car.launch.py

It starts:
- Gazebo Harmonic.
- robot_state_publisher.
- joint_state_publisher.
- The robot in Gazebo.
- ROS-Gazebo bridge.
- RViz with the saved configuration.

## RViz

The RViz configuration is:
rviz/race_car.rviz

It shows:
- Robot Model.
- Camera frame.
- TF frames.

## Problems and Solutions

### 1. Gazebo Plugin Problem
The task specifies:
libgazebo_ros_diff_drive.so

This plugin is for Gazebo Classic, but I was using Gazebo Harmonic. Because of this, the Classic plugin could not be used.

Solution:
I replaced it with the Gazebo Harmonic DiffDrive plugin:
libgz-sim-diff-drive-system.so

The car was then able to move using /cmd_vel.

### 2. ROS 2 and Gazebo Topics
At first, /cmd_vel and /odom were not visible in the ROS 2 topic list even though the Gazebo plugin was working. The reason was that Gazebo Transport topics and ROS 2 topics are separate.

Solution:
I added ros_gz_bridge to the launch file to bridge the required topics between Gazebo and ROS 2.

This made the following topics available:
- /cmd_vel
- /odom
- /camera/image
- /camera/camera_info

### 3. RViz Configuration
The robot model was visible in RViz, but the required Camera frame and TF visualization were not configured.

Solution:
I added the TF display, made the camera_link frame visible, and saved the RViz configuration.

## Motion Verification

The robot was tested using:
ros2 topic pub --once /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.5}, angular: {z: 0.2}}"

The car successfully moved forward and turned.

## Final Result

The 4-wheel race car was successfully simulated in Gazebo Harmonic and RViz with:
- [x] 4 wheels.
- [x] Front camera.
- [x] XACRO wheel macro.
- [x] Physical properties.
- [x] Differential drive.
- [x] /cmd_vel control.
- [x] Camera and TF frames.
- [x] ROS 2-Gazebo communication.
