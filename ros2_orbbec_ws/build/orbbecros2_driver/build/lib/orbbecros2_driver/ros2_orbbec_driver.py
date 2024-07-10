# ros2 orbbec camera python driver/wrapper
import rclpy
import rclpy.publisher
from sensor_msgs.msg import Image
from rclpy.node import Node 



# implementation of Orbbec Astra camera driver/wrapper...
class Orbbec_driver(Node):
    def __init__(self):
        super().__init__("orbbec_camera_driver_wrapper")
        self.camera_image = rclpy.publisher(Image,"/camera/image_raw",10)
    
