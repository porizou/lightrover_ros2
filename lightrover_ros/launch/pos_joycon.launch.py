import launch
import launch.actions
import launch.substitutions
import launch_ros.actions
import os
import ament_index_python.packages

def generate_launch_description():
    config_directory = os.path.join(
        ament_index_python.packages.get_package_share_directory('lightrover_ros'),
        'config')
    params = os.path.join(config_directory, 'joy-params.yaml')
    joy_node = launch_ros.actions.Node(package='joy',
                                       node_executable='joy_node',
                                       output='both',
                                       parameters=[params])
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='lightrover_ros', executable='i2c_controller', output='screen'),
        launch_ros.actions.Node(
            package='lightrover_ros', executable='odom_manager', output='screen'),
        launch_ros.actions.Node(
            package='lightrover_ros', executable='pos_controller', output='screen'),
        launch_ros.actions.Node(
            package='lightrover_ros', executable='rover_gamepad', output='screen'),
        joy_node
    ])
