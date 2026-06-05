import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from irobot_create_msgs.msg import AudioNoteVector, AudioNote
from builtin_interfaces.msg import Duration
# Any additional imports here

# Decide your node class name
class SoundTest(Node):
    def __init__(self):

        # Change to have your node name
        super().__init__('beep_node')

        self.vel_subscriber = self.create_subscription(Twist, '/robot4/cmd_vel_unstamped', self.callback, 10)
        self.vel_subscriber

        self.sound_pub = self.create_publisher(AudioNoteVector, '/robot4/cmd_audio', 10)

    def callback(self, msg):
        robot_fwd = msg.linear.x
        audio_msg = self.play_audio(robot_fwd)
        self.sound_pub.publish(audio_msg)

    def play_audio(self, x):
        audio_msg = AudioNoteVector()
        audio_note = AudioNote()
        if x > 0:
            time_play = Duration()
            time_play.sec = 1
            audio_note.frequency = 262
            audio_note.max_runtime = time_play
            audio_msg.notes.append(audio_note)
        return audio_msg

def main(args=None):
    rclpy.init(args=args)
    
    node = SoundTest()

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()