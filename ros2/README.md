# ROS2 Lane Following and Camera Calibration

Developed for **UCSD ECE/MAE 148**, this project used a Raspberry Pi 5, OAK-D Lite camera, and VESC drivetrain to navigate a track while staying **to the right of the yellow lane markers**. The ROS2 software ran inside Docker.


## My Calibration Work

I adjusted the camera-processing and lane-tracking settings directly on the
track to establish a useful visual reference for the guidance controller.

- **HSV thresholds:** isolated yellow markers from the pavement and background.
- **Erosion and dilation:** reduced small artifacts in the detection mask.
- **Contour filtering:** adjusted marker-width limits and the number of segments considered.
- **Image cropping:** focused processing on the relevant section of road.
- **Centerline offset:** adjusted the tracking reference so the car stayed to the right of the yellow line.
- **Error threshold:** adjusted the tolerance before steering corrections were applied.

The goal was a clean mask with white marker regions on a black background,
followed by a consistent detected marker position. I checked the calibration
under actual track lighting and adjusted settings while observing the mask
and lane-detection overlays.

## How the System Worked

| Stage | Function |
| --- | --- |
| Camera input | Published OAK-D Lite images to ROS2 |
| HSV filtering | Selected pixels corresponding to yellow markers |
| Contour processing | Selected marker regions and calculated a representative position |
| Tracking reference | Compared the marker position with the calibrated reference |
| Lane guidance | Used lane error for PID steering and throttle scheduling |
| VESC interface | Converted control commands into motor and steering actuation |

The centerline offset was part of the perception/tracking calibration. It
was separate from the servo's straight-ahead calibration and the steering
limits. The exact final offset and its numerical convention were not recovered.

## Configuration Examples

| File | Contents |
| --- | --- |
| [node_config.example.yaml](config/node_config.example.yaml) | Course calibration-mode selection excerpt |
| [car_config.example.yaml](config/car_config.example.yaml) | OAK-D Lite and VESC selection excerpt |
| [vision_calibration.example.yaml](config/vision_calibration.example.yaml) | Documentation of the GUI settings adjusted during calibration |
| [ros_racer_calibration.example.yaml](config/ros_racer_calibration.example.yaml) | Course-reference PID and actuator settings |

## Code Availability and Credits

These examples were reconstructed from course instructions because the original Raspberry Pi files are unavailable. Numerical values are course references, not final vehicle calibration; `null` indicates an unrecovered value. The vision worksheet is documentation only, and the configuration examples have not been hardware-validated.

The UCSD Robocar framework provided the camera, lane-detection, guidance, and actuator software. This folder documents my configuration and calibration work.