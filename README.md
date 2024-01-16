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
```
The new ROS bag is compatible with any ROS workspace, which provides flexibility for further analysis or visualization in different environments.

## Review the Odometry with Rviz

In one terminal, run the following command to play the recorded ROS bag:
```bash
rosbag play your_bag_filename.bag
```
In another terminal, run 
```bash
rviz
```
and then, import the odom.rviz as the configuration file.  

## Extracting Odometry Data

You can extract odometry data from the new ROS bag in any ROS environment using the provided Python script. Execute the script as follows:
```bash
python3 script_name.py /path/to/your/bagfile.bag /path/to/output.csv
```
The script will output a CSV file named output.csv that contains the odometry data extracted from the ROS bag.
