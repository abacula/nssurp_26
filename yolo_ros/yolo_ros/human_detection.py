import rclpy
from rclpy.node import Node

from yolo_msgs.msg import Detection
from yolo_msgs.msg import DetectionArray
from irobot_create_msgs.msg import LightringLeds
# Any additional imports here

# Decide your node class name
class HumanDetectionNode(Node):
    def __init__(self):

        # Change to have your node name
        super().__init__('human_detection')
        self.human_detection_sub = self.create_subscription(DetectionArray, '/yolo/detections', self.human_cb, 10)
        self.lightring_pub = self.create_publisher(LightringLeds, '/robot4/cmd_lightring',10)
    
    def human_cb(self, detections_msg):
        human_detected = False
        for msg in detections_msg.detections:
            if msg.class_name == 'person' and msg.score > 0.6:
                human_detected = True
                break

        if human_detected:
            self.get_logger().info("Human detected")
            self.lightring_pub.publish(self.create_lightring_msg(128, 0, 128))
        else:
            self.lightring_pub.publish(self.create_lightring_msg(0, 255, 0))
        
    def create_lightring_msg(self, r:int, g:int, b:int):
        msg = LightringLeds()
        msg.override_system = True
        self.get_logger().info("Lightring changed")
        for i in range(6):
            msg.leds[i].red = r
            msg.leds[i].green = g
            msg.leds[i].blue = b
        return msg
def main(args=None):
    rclpy.init(args=args)

    # Change to be your node class name
    node = HumanDetectionNode()

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()