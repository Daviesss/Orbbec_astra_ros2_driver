from setuptools import setup

package_name = 'orbbecros2_driver'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Davies Iyanuoluwa Ogunsina',
    maintainer_email='Davisogunsina@gmail.com',
    description='A ROS 2 driver/wrapper package for Orbbec Astra Camera',
    license='MIT License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'orbbec_driver_node=orbbecros2_driver.ros2_orbbec_driver:main',
        ],
    },
)
