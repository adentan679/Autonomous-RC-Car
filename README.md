# Autonomous RC Car: DonkeyCar, GPS, and ROS2 Navigation

A Raspberry Pi–based autonomous RC car developed for **UCSD ECE/MAE 148** using machine learning, RTK GPS waypoint navigation, and ROS2 computer vision.

![Autonomous RC Car](images/rc_car1.jpg)

## Overview

This project explored three approaches to autonomous driving using an RC car equipped with a Raspberry Pi 5, OAK-D Lite camera, Point One GPS receiver, VESC motor controller, brushless motor, and steering servo.

The project progressed through:

1. DonkeyCar neural-network driving
2. RTK GPS waypoint navigation
3. ROS2 camera-based lane following

The work involved hardware integration, data collection, machine-learning model training, computer vision, PID control, and vehicle calibration.

---

## My Contributions

- Integrated and tested the Raspberry Pi, OAK-D Lite, VESC, motor, steering servo, GPS receiver, and power hardware.
- Configured DonkeyCar for camera input, controller operation, data collection, and autonomous driving.
- Collected driving data and trained a TensorFlow steering and throttle model.
- Configured RTK GPS corrections and recorded waypoint paths.
- Calibrated ROS2 lane detection for yellow track markers.
- Tuned steering, throttle, and PID parameters through track testing.
- Debugged USB power, serial communication, camera, and motor-control issues.

---

## Autonomous Driving Systems

### 1. DonkeyCar Neural-Network Driving

The car was manually driven around a track using a Logitech F710 controller. During each drive, the OAK-D Lite recorded images paired with the corresponding steering and throttle inputs.

This data was used to train a TensorFlow model that predicted steering and throttle commands from live camera images. The trained model was then deployed on the Raspberry Pi for autonomous testing.

```text
OAK-D Lite Camera
        ↓
Images + Driving Inputs
        ↓
TensorFlow Model Training
        ↓
Steering and Throttle Predictions
        ↓
VESC Motor Controller
        ↓
Motor and Steering Servo
```
**Video Link** : HERHEHEHHEEH

### 2. RTK GPS Waypoint Navigation

The second system used a Point One Navigation GPS receiver with Polaris RTK corrections. RTK correction data provided more accurate positioning than standard GPS.

A path was recorded while the car was manually driven around a course. During autonomous playback, the car compared its current position to the saved GPS waypoints and used PID control to generate steering corrections.

```text
Point One GPS + RTK Corrections
        ↓
Vehicle Position
        ↓
Recorded GPS Waypoints
        ↓
Path and Heading Error
        ↓
PID Controller
        ↓
VESC Motor Controller
```
**Video Link**: HERERERER


### 3. ROS2 Lane Following

The final system used ROS2 and computer vision to navigate a track while keeping the car on the **right side of the lane**. The ROS2 environment ran inside Docker on the Raspberry Pi.

Images from the OAK-D Lite were converted into HSV color space to isolate the yellow center markers. The detected marker position was used as a reference for determining the car’s location within the lane. Instead of driving directly over the yellow markers, the camera alignment and lane-position target were calibrated so the car remained on their right side.

The difference between the car’s desired position and its detected position was converted into an error value. A PID controller used this error to continuously adjust the steering and throttle while keeping the car in the right-hand lane.

```text
OAK-D Lite Camera
        ↓
ROS2 Camera Node
        ↓
HSV Yellow-Marker Detection
        ↓
Right-Side Lane Position Error
        ↓
PID Controller
        ↓
ROS2 /cmd_vel
        ↓
VESC Motor Controller
        ↓
Motor and Steering Servo
```

**Video Link**: https://drive.google.com/file/d/1v_xSNbWWge-8-v76XIZwv80xZv-_OYFh/view?usp=sharing

---

## Hardware

- Raspberry Pi 5
- OAK-D Lite camera
- Point One Navigation GPS receiver and antenna
- VESC motor controller
- Brushless DC motor
- Steering servo
- Logitech F710 wireless controller
- Powered USB hub
- LiPo battery
- Anti-spark switch
- DC-DC converter
- Power-distribution hardware

---

## Hardware Architecture

![Hardware and Power Diagram](images/hardware_diagram.jpg)

Battery power was separated between the high-power drivetrain and the lower-voltage electronics. The VESC powered and controlled the drive motor, while a DC-DC converter supplied regulated power to the Raspberry Pi. The Raspberry Pi communicated with the camera, GPS receiver, controller, and VESC through USB connections.

---

## Software and Tools

- Python
- DonkeyCar
- ROS2 Foxy
- Docker
- TensorFlow/Keras
- OpenCV
- DepthAI
- Point One Polaris RTK
- VESC Tool
- Raspberry Pi OS/Linux
- Git and GitHub

---

## Testing and Calibration

Testing included:

- OAK-D Lite camera and USB communication
- VESC motor and steering control
- Controller input and manual driving
- Training-data collection and validation
- TensorFlow model training and deployment
- RTK GPS connection and waypoint recording
- HSV threshold and camera alignment calibration
- Steering, throttle, and PID tuning
- Autonomous track testing

---

## Challenges and Solutions

### Camera Stability

The OAK-D Lite occasionally disconnected because of insufficient USB power. A powered USB hub was used to improve the connection.

### GPS Accuracy

Accurate GPS navigation required a clear view of the sky and a continuous network connection for RTK correction data. The RTK fix was verified before recording or replaying a path.

### Lane Detection

Lighting and shadows affected the appearance of the yellow markers. HSV thresholds, contour filtering, image cropping, and camera alignment were adjusted directly on the track.

### Steering Oscillation

Early autonomous tests produced unstable steering. PID gains, steering limits, and vehicle speed were adjusted through repeated testing.

---

## Results

The completed platform supported:

- Manual wireless control
- Camera and driving-data collection
- TensorFlow model training and autonomous inference
- RTK GPS waypoint recording and playback
- ROS2 yellow-marker detection
- PID-based steering and throttle control
- VESC control of the motor and steering servo

---

## Code Availability

The code and configuration files in this repository are reconstructed examples based on course instructions. They are not the original files used to operate the vehicle, as those files are no longer accessible on the Raspberry Pi. Example values may differ from the final settings used during testing and have not been validated on the vehicle.

---
## Repository Structure

```text
autonomous-rc-car/
├── README.md
├── images/
│   ├── rc-car.jpg
│   └── hardware-diagram.png
├── donkeycar/
│   ├── myconfig.py
│   └── patches/
├── gps/
│   ├── config/
│   └── example-path.csv
├── ros2/
│   ├── nodes/
│   ├── config/
│   └── launch/
└── docs/
    └── troubleshooting.md
```

## Course Information

Developed for **UCSD ECE/MAE 148: Introduction to Autonomous Vehicles** using the UCSD Robocar platform and course-provided software.

This repository documents my hardware integration, configuration, testing, calibration, and autonomous-driving experience.