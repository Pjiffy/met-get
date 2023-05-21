from setuptools import setup, find_packages

setup(
    name='met_get_package',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'met-get = met_get_package.bin.met_get:main'
        ]
    },
    install_requires=[
        'requests'
    ],
)

