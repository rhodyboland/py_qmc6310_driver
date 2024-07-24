from setuptools import find_packages, setup

package_name = 'py_qmc6310_driver'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
         ('share/' + package_name + '/launch', ['launch/qmc6310.launch.py'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rhody',
    maintainer_email='rhodyboland@hotmail.com',
    description='ROS 2 QMC6310 driver',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'magnetometer_node = py_qmc6310_driver.magnetometer_node:main'
        ],
    },
)
