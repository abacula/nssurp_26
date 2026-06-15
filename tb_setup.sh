source /opt/ros/jazzy/setup.sh
source ~/turtlebot4_ws/install/setup.sh
source /home/nguyena/.local/bin/env
export RMW_IMPLEMENTATION=rmw_fastrtps_cpp
[ -t 0 ] && export ROS_SUPER_CLIENT=True || export ROS_SUPER_CLIENT=False
export ROS_DOMAIN_ID=0
export ROS_DISCOVERY_SERVER=10.5.113.104:11811
