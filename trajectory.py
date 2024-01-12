import rosbag
import csv
import argparse
from tf.transformations import euler_from_quaternion

# Set up argument parser
parser = argparse.ArgumentParser(description='Extract odometry data from a ROS bag file and save it to a CSV file.')
parser.add_argument('bag_path', help='Path to the ROS bag file')
parser.add_argument('csv_path', help='Path to the output CSV file')
args = parser.parse_args()

with rosbag.Bag(args.bag_path, 'r') as bag, open(args.csv_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Time', 'Position_X', 'Position_Y', 'Position_Z', 'Orientation_Roll', 'Orientation_Pitch', 'Orientation_Yaw'])

    for topic, msg, t in bag.read_messages(topics=['/odometry/filtered']):
        # Extract position data
        position = msg.pose.pose.position
        x, y, z = position.x, position.y, position.z
        
        # Extract orientation data
        orientation_q = msg.pose.pose.orientation
        orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
        roll, pitch, yaw = euler_from_quaternion(orientation_list)
        
        # Write to CSV
        writer.writerow([t, x, y, z, roll, pitch, yaw])
