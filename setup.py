from setuptools import setup

with open('README.md') as README:
    long_description = README.read()
setup(
    name='pydl',
    version='0.1d',
    packages=['pydl', ],
    license='MIT',
    description='A Library to download music from Youtube , Soundcloud and many others sites',
    long_description=long_description,
    author='Ayan Bag',
    author_email='ayanbag9474@gmail.com',
    install_requires=[
        'requests',
        'youtube-dl',
    ],
    python_requires='>=3.4',
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points=dict(console_scripts=[
        'pydl = pydl.dlutil:main', ]),
    url='https://github.com/ayanbag/pydl',
)