try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from fencsv import __version__

setup(
    name='fencsv',
    author='Garrett Berg',
    author_email='vitiral@gmail.com',
    version=__version__,
    py_modules=['fencsv'],
    license='MIT',
    install_requires=[
        'six',
    ],
    description="convert fen strings into human readable csv and back",
    url="https://github.com/vitiral/fencsv",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ]
)
