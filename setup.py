from setuptools import setup

setup(
    name='moviereview',
    version='1.0.0',
    description='Fetches movie ratings and review data from Times of India.',
    author='Shantanu Gupta',
    author_email='shantanu@programmer.net',
    url='https://github.com/gupta-shantanu/moviereview',
    packages=['moviereview'],
    install_requires=[
        "beautifulsoup4",
    ]
    )
