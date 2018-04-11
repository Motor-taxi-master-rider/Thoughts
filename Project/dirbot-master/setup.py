from setuptools import find_packages, setup

setup(
    name='dirbot',
    version='1.0',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = dirbot.settings']},
)
