from setuptools import setup, find_packages
setup(
    name = 'sathyabama-updates',
    version = '0.1',
    author = 'Manoj Tummala',
    author_email = 'tummalamanoj2002@gmail.com',
    description = 'Fetches latest updates of news and events and Pretty prints it on terminal.',
    url='https://github.com/manojtummala/ucl',
    install_requires=[
        'Click', 'requests', 'tabulate'
    ],
    py_modules=['sathya'],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        sathya=source:get
    ''',
)