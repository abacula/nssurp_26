import rclpy
import time
from rclpy.node import Node
from yolo_msgs.msg import HallwayAck
from geometry_msgs.msg import Twist

# Any additional imports here

# Decide your node class name
class Wave(Node):
    def __init__(self):

        self.saw_person = False

        # Change to have your node name
        super().__init__('wave_node')
        self.has_seen = False

        self.publisher = self.create_publisher(Twist, '/robot4/cmd_vel_unstamped', 10)
        self.ack_sub = self.create_subscription(HallwayAck, '/robot4/hallway_ack', self.hallway_cb, 10)

        self.timer = self.create_timer(0.1, self.loop)

    
    def hallway_cb(self, msg):

        if msg.person_detected and msg.bbox_height > 80:
            self.saw_person = True
            self.wave()

    def wave(self):

        twist = Twist()
        twist.linear.x = 0.0
        
        twist.angular.z = 5.0
        self.publisher.publish(twist)
        time.sleep(1)
        
        twist.angular.z = -10.0
        self.publisher.publish(twist)
        time.sleep(1)

        twist.angular.z = 5.0
        self.publisher.publish(twist)
        time.sleep(1)
        
        twist.angular.z = 0.0
        self.publisher.publish(twist)
        
        self.saw_person = False

    def loop(self):
        
        twist = Twist()
        
        if not self.saw_person:
            twist.linear.x = 0.5
            self.publisher.publish(twist)

def main(args=None):
    rclpy.init(args=args)

    # Change to be your node class name
    node = Wave()

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()