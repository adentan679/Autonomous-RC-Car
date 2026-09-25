# ROS2 Lane Following and Camera Calibration

A camera-based autonomous driving system developed for **UCSD ECE/MAE 148**, using a Raspberry Pi 5, OAK-D Lite camera, and VESC drivetrain. The UCSD Robocar framework ran inside Docker and provided the ROS2 camera, lane-detection, guidance, and actuator software.

Our task was to navigate the track while staying **to the right of the yellow lane markers**. No LiDAR was used.

## My Contributions

My work focused on camera and lane-tracking calibration, hardware integration, and on-track testing. I used the calibration interface to observe the detection mask and lane overlays, then evaluated the car’s behavior during autonomous runs.

The course framework supplied the underlying software. This folder documents my configuration, calibration, and testing experience.

## How the System Worked

| Stage | Function |
| --- | --- |
| Camera input | Published OAK-D Lite images to ROS2 |
| HSV filtering | Isolated yellow marker pixels from the pavement and background |
| Contour processing | Selected valid marker regions and calculated a representative image position |
| Tracking reference | Compared the detected marker position with a calibrated image reference to calculate lane error |
| Lane guidance | Used PID steering and error-based throttle scheduling |
| VESC interface | Converted `/cmd_vel` commands into motor and steering-servo actuation |

The tracking reference was adjusted so the car traveled to the right of the yellow markers rather than directly over them. This image reference was separate from the steering servo’s straight-ahead calibration and mechanical steering limits.

PID control adjusted steering in response to lane error. Throttle scheduling reduced speed as the error increased, helping the car negotiate turns.

## Camera and Lane Calibration

The calibration interface provided the following controls:

| Control | Purpose |
| --- | --- |
| HSV thresholds | Selected yellow marker pixels while excluding other colors and background regions |
| Erosion and dilation | Removed small artifacts and adjusted marker regions in the binary mask |
| Contour-width limits | Rejected regions that were too narrow or too wide to be useful markers |
| Number of segments | Selected how many detected segments contributed to the representative marker position |
| Image cropping | Selected the portion of the camera image analyzed for lane detection |
| Camera centerline / tracking reference | Defined the reference position used to calculate lane error |
| Error threshold | Established a dead band around the reference to reduce small steering corrections |

The calibration goal was a clean mask showing white marker regions against a black background, followed by a stable detected marker position. Track testing was necessary to evaluate detection through curves as well as on straight sections.

The exact final settings and the numerical convention used for the tracking offset were not retained.

## Results and Observations

The car ultimately demonstrated successful autonomous lane following after calibration and track testing.

During earlier runs, we observed intermittent loss of lane-marker detection during turns, along with the car stopping partway through a turn. The exact cause of the stopping behavior and the specific parameter changes that resolved the issue were not retained.

The final calibrated setup followed the track successfully. This experience emphasized the importance of evaluating camera coverage and lane detection throughout turns, where marker positions change within the image.

## Configuration Examples

The YAML files in `config/` are reconstructed examples and documentation worksheets. They are not a complete, runnable copy of the vehicle’s ROS2 configuration.

- **Node selection:** illustrates selection of calibration or autonomous navigation mode.
- **Hardware selection:** illustrates enabling the OAK-D camera and VESC interface.
- **Calibration documentation:** records relevant vision, guidance, or actuator settings where available.

Consult each file’s comments for its scope and limitations. Course-reference values are starting examples, not recovered final vehicle settings. A value of `null` indicates an unknown or unrecovered setting and should not be loaded directly as a ROS2 parameter.

## Code Availability and Credits

The original Raspberry Pi files are no longer available. These examples were reconstructed from course instructions and have not been validated on the vehicle.

The **UCSD Robocar framework** provided the camera drivers, lane-detection pipeline, guidance controller, and actuator interface. My contributions centered on hardware integration, configuration, calibration, and testing.

This repository serves as a portfolio record of that work.