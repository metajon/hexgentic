from setuptools import setup, find_packages

setup(
    name='hexgen',
    packages=find_packages(),
    python_requires='>=3.10',
    install_requires=[
        'Pillow>=10.0,<13.0',
        'numpy>=1.26,<3.0',
    ],
)
