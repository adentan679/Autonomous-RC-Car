# -----------------------------------------------------------
# Image Processing
# -----------------------------------------------------------

TRANSFORMATIONS = ["RESIZE"]

RESIZE_WIDTH = 160
RESIZE_HEIGHT = 120

IMAGE_W = 160
IMAGE_H = 120
IMAGE_DEPTH = 3  # RGB image


# -----------------------------------------------------------
# Drive Loop
# -----------------------------------------------------------

DRIVE_LOOP_HZ = 20
MAX_LOOPS = None


# -----------------------------------------------------------
# OAK-D Lite Camera
# -----------------------------------------------------------

CAMERA_TYPE = "OAKD"
CAMERA_FRAMERATE = DRIVE_LOOP_HZ
CAMERA_INDEX = 0

CAMERA_VFLIP = False
CAMERA_HFLIP = False

OAKD_RGB = True
OAKD_DEPTH = False
OAKD_ID = None


# -----------------------------------------------------------
# VESC Drivetrain
# -----------------------------------------------------------

DRIVE_TRAIN_TYPE = "VESC"

# Verify the port before launching.
# It may change to /dev/ttyACM1 depending on connected devices.
VESC_SERIAL_PORT = "/dev/ttyACM0"

VESC_BAUDRATE = 115200
VESC_TIMEOUT = 0.05

VESC_HAS_SENSOR = True
VESC_START_HEARTBEAT = True

# Start conservatively during testing.
VESC_MAX_SPEED_PERCENT = 0.30

# Maps DonkeyCar steering values to the VESC steering range.
VESC_STEERING_SCALE = 0.5
VESC_STEERING_OFFSET = 0.5


# -----------------------------------------------------------
# Logitech F710 Controller
# -----------------------------------------------------------

USE_JOYSTICK_AS_DEFAULT = True
CONTROLLER_TYPE = "F710"

JOYSTICK_DEVICE_FILE = "/dev/input/js0"
JOYSTICK_DEADZONE = 0.01

JOYSTICK_MAX_THROTTLE = 0.5
JOYSTICK_STEERING_SCALE = 1.0
JOYSTICK_THROTTLE_DIR = -1.0

AUTO_RECORD_ON_THROTTLE = True

USE_NETWORKED_JS = False
NETWORK_JS_SERVER_IP = None


# -----------------------------------------------------------
# Web Camera Stream
# -----------------------------------------------------------

USE_FPV = False