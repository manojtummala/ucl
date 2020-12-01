from setuptools import setup, find_packages
setup(
    name = 'sup-sathyabama',
    version = '0.1',
    author = 'Manoj Tummala',
    author_email = 'tummalamanoj2002@gmail.com',
    description = 'Fetches latest updates of news and events and Pretty prints it on terminal.',
    url='https://github.com/manojtummala/SUP',
    py_modules = ['sup'],
    install_requires=[
        'Click', 'requests', 'tabulate'
    ],
    entry_points='''
        [console_scripts]
        sup=source:get
    ''',
)