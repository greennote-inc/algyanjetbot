import glob
import subprocess
from setuptools import setup, find_packages, Extension


def build_libs():
    subprocess.call(['cmake', '.'])
    subprocess.call(['make'])
    

build_libs()


setup(
    name='algyan jetbot',
    version='0.3.0a',
    description='ALGYAN AI Study Kit based on NVIDIA Jetbot and Jetson Nano',
    packages=find_packages(),
    install_requires=[
        'Adafruit_MotorHat',
        'Adafruit-SSD1306',
    ],
    package_data={'jetbot': ['ssd_tensorrt/*.so']},
)
