# Trajectory-with-RGBD-Camera
# Room Scanning with D435i Camera and ROS

This guide walks through the process of scanning a room using the D435i camera and saving the data as a ROS bag following the Intel RealSense tutorial.

## Scanning and Saving with D435i

To begin scanning the room with the D435i camera, follow the steps outlined in the Intel RealSense tutorial:

[SLAM with D435i](https://github.com/IntelRealSense/realsense-ros/wiki/SLAM-with-D435i)

## Replaying a Saved ROS Bag

After completing the tutorial and saving the room scan data, you can replay the saved ROS bag file. To do this, follow the instructions provided in the tutorial.

## Recording a New ROS Bag

While replaying the saved ROS bag file, open another terminal and execute the following command to record a new ROS bag with filtered odometry and transform data:

```bash
rosbag record -O your_bag_filename.bag /odometry/filtered /tf /tf_static /clock
