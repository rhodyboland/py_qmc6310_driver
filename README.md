# py_qmc6310_driver
### ROS2 qmc6310 driver using piicodev libraries

Basic implementation of using the piico dev provided libraries for the QMC6310 in a ros2 driver. Publishes sensor_msgs/MagneticField messages containing X,Y,Z uT values.  No covariance yet.

### Install
```
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone git@github.com:rhodyboland/py_qmc6310_driver.git
cd ..
rosdep install --from-paths src -y --ignore-src
pip install PiicoDev_QMC6310 PiicoDev_Unified
colcon build
source install/setup.bash
ros2 launch py_qmc6310_driver qmc6310.launch.py
```
