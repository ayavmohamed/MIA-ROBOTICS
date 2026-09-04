import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node

import xacro


def generate_launch_description():

    # Get the package path
    package_path = get_package_share_directory(
        'race_car_description'
    )

    # Get the XACRO file
    xacro_file = os.path.join(
        package_path,
        'urdf',
        'race_car.xacro'
    )

    # Convert XACRO to URDF
    robot_description = xacro.process_file(xacro_file).toxml()

    # Launch Gazebo Harmonic
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('ros_gz_sim'),
                'launch',
                'gz_sim.launch.py'
            )
        ),
        launch_arguments={
            'gz_args': '-r empty.sdf'
        }.items()
    )

    # Publish robot state and TF
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[
            {'robot_description': robot_description}
        ]
    )

    # Publish joint states
    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher'
    )

    # Spawn robot in Gazebo
    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-topic',
            'robot_description',
            '-name',
            'race_car',
            '-z',
            '0.3'
        ],
        output='screen'
    )


    # Bridge ROS 2 topics with Gazebo
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
    '/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist',
    '/odom@nav_msgs/msg/Odometry[gz.msgs.Odometry',
    '/camera/image@sensor_msgs/msg/Image[gz.msgs.Image',
    '/camera/camera_info@sensor_msgs/msg/CameraInfo[gz.msgs.CameraInfo'
],
        output='screen'
    )

    # RViz
    rviz_config = os.path.join(
        package_path,
        'rviz',
        'race_car.rviz'
    )

    rviz = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', rviz_config],
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        joint_state_publisher,
        spawn_robot,
        bridge,
        rviz
    ])