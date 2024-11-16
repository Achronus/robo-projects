from setuptools import find_packages, setup
import xml.etree.ElementTree as ET
import os
from glob import glob


tree = ET.parse("package.xml")
package = tree.getroot()


package_info = {
    "name": package.find("name").text,
    "version": package.find("version").text,
    "description": package.find("description").text,
    "maintainer": {
        "name": package.find("maintainer").text,
        "email": package.find("maintainer").attrib.get("email")
    },
    "license": package.find("license").text,
}

package_name = package_info["name"]

setup(
    name=package_name,
    version=package_info["version"],
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer=package_info["maintainer"]["name"],
    maintainer_email=package_info["maintainer"]["email"],
    description=package_info["description"],
    license=package_info["license"],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
