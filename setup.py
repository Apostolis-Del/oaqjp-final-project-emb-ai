from setuptools import setup, find_packages

setup(
    name='EmotionDetection',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='Apostolos',
    author_email='your.email@example.com',
    description='A package for emotion detection using a specified API.',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
