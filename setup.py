from setuptools import setup, find_packages

setup(
    name='ourtask_task',
    use_scm_version=True,
    setup_requires=['setuptools>=42', 'setuptools_scm'],
    packages=find_packages(),
    description='A simple JSON processing package',
    author='Willem van Heemstra',
    author_email='wvanheemstra@icloud.com',
    url='https://github.com/OurTask/task',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
