from setuptools import find_packages, setup
import xml.etree.ElementTree as ET

from pydantic import BaseModel


tree = ET.parse("package.xml")
package = tree.getroot()


class Maintainer(BaseModel):
    name: str
    email: str


class PackageInfo(BaseModel):
    format: str
    name: str
    version: str
    desc: str
    maintainer: Maintainer
    license: str


package_info = PackageInfo(
    format=package.attrib.get("format"),
    name=package.find("name").text,
    version=package.find("version").text,
    desc=package.find("description").text,
    maintainer=Maintainer(
        name=package.find("maintainer").text,
        email=package.find("maintainer").attrib.get("email")
    ),
    license=package.find("license").text,
)

package_name = package_info.name

setup(
    name=package_name,
    version=package_info.version,
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer=package_info.maintainer.name,
    maintainer_email=package_info.maintainer.email,
    description=package_info.desc,
    license=package_info.license,
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
