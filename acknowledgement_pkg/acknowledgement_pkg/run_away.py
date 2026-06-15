import rclpy
from rclpy.node import Node
from yolo_msgs.msg import HallwayAck
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import time

# Any additional imports here

# Decide your node class name
class RunAway(Node):
    def __init__(self):

        self.saw_person = False
        self.obstacle_detected = False
        self.STOP_DIST = 0.3 # Meters
        self.turn_time = 10.0 # 1/10ths of a second?

        # Change to have your node name
        super().__init__('run_away_node')
        self.has_seen = False

        self.publisher = self.create_publisher(Twist, '/robot4/cmd_vel_unstamped', 10)
        self.ack_sub = self.create_subscription(HallwayAck, '/robot4/hallway_ack', self.hallway_cb, 10)
        self.subscriber = self.create_subscription(LaserScan, '/robot4/scan', self.scan_callback, 10)


        self.timer = self.create_timer(0.1, self.loop)
    
    def hallway_cb(self, msg):

        if msg.person_detected and msg.bbox_height > 80 and self.saw_person == False:
            self.saw_person = True
            self.turning = True
    
    def scan_callback(self, msg):

        for distance in msg.ranges[200:340]:
            if msg.range_min < distance < msg.range_max:
                if distance < self.STOP_DIST:
                    self.obstacle_detected = True
                    break

    def loop(self):

        twist = Twist()
        if not self.saw_person:
            twist.linear.x = 0.5
        elif not self.obstacle_detected and self.saw_person:
            if self.turning:
                twist.angular.z = 10.0
                twist.linear.x = 0.0
                time.sleep(self.turn_time)
            else:
                twist.linear.x = 0.5
                twist.angular.z = 0.0
        else:
            twist.linear.x = 0.0
            twist.angular.z = 0.0

        self.publisher.publish(twist)



def main(args=None):
    rclpy.init(args=args)

    # Change to be your node class name
    node = RunAway()

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()