from setuptools import setup, find_packages


setup(
    name='cbf',
    version='0.0.1',
    packages=find_packages(),
    tests_require=[
        'fastapi==0.95.2',
    ],
    python_requires='>=3.11'
)
