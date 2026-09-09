# -----------------------------------------------------------
# GPS Configuration
# -----------------------------------------------------------

# GPS port used by DonkeyCar to receive NMEA position data.
#
# This must be different from the port used by runner.py.
# For example:
#   runner.py uses /dev/ttyUSB1
#   DonkeyCar uses /dev/ttyUSB0
GPS_SERIAL = "/dev/ttyUSB0"

# Point One GPS NMEA output baud rate.
GPS_SERIAL_BAUDRATE = 460800

# Print GPS coordinates and status information for debugging.
# Change to False after confirming the GPS works.
GPS_DEBUG = True

# Enable live GPS input.
HAVE_GPS = True

# Used only when replaying GPS data from a saved NMEA file.
# Leave as None when using the physical GPS receiver.
GPS_NMEA_PATH = None


# -----------------------------------------------------------
# GPS Path-Following PID Controller
# -----------------------------------------------------------

# Proportional gain:
# Controls how strongly the car reacts to its current path error.
PID_P = 0.15

# Derivative gain:
# Reduces side-to-side oscillation and steering overshoot.
PID_D = 0.60

# Integral gain:
# Corrects persistent long-term drift.
PID_I = 0.0


# -----------------------------------------------------------
# VESC Drivetrain
# -----------------------------------------------------------

DRIVE_TRAIN_TYPE = "VESC"

# Start at 30% for initial testing.
# Increase toward 0.50 after confirming stable operation.
VESC_MAX_SPEED_PERCENT = 0.30

# Verify this port before starting DonkeyCar.
VESC_SERIAL_PORT = "/dev/ttyACM0"

VESC_BAUDRATE = 115200
VESC_TIMEOUT = 0.05

VESC_HAS_SENSOR = True
VESC_START_HEARTBEAT = True

# Steering calibration.
VESC_STEERING_SCALE = 0.5
VESC_STEERING_OFFSET = 0.5


# -----------------------------------------------------------
# Controller
# -----------------------------------------------------------

USE_JOYSTICK_AS_DEFAULT = True

# Change this to "ps4" if you used a PS4 controller.
CONTROLLER_TYPE = "F710"

JOYSTICK_DEVICE_FILE = "/dev/input/js0"
JOYSTICK_MAX_THROTTLE = 0.5
JOYSTICK_DEADZONE = 0.01

JOYSTICK_STEERING_SCALE = 1.0
JOYSTICK_THROTTLE_DIR = -1.0

USE_NETWORKED_JS = False
NETWORK_JS_SERVER_IP = None


# -----------------------------------------------------------
# GPS Path Button Mappings
# -----------------------------------------------------------

# Save the recorded waypoints to path.csv.
SAVE_PATH_BTN = "R1"

# Load path.csv for autonomous playback.
LOAD_PATH_BTN = "X"

# Set the current GPS position as the local (0, 0) origin.
RESET_ORIGIN_BTN = "B"

# Delete the waypoints currently stored in memory.
ERASE_PATH_BTN = "Y"

# Start or stop waypoint recording.
TOGGLE_RECORDING_BTN = "L1"

# Disable controller-based PID adjustment.
INC_PID_D_BTN = None
DEC_PID_D_BTN = None
INC_PID_P_BTN = None
DEC_PID_P_BTN = None


# -----------------------------------------------------------
# Camera
# -----------------------------------------------------------

# GPS path following does not require the camera.
CAMERA_TYPE = "MOCK"