from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name="cron_parser",
    version="0.1",
    description="Cron Parsing Library",
    author_email="shril.iitdhn@gmail.com",
    packages=["cron_parser"],
    package_dir={"": "src"},
    entry_points={
        'console_scripts': [
            'cron_parser=cron_parser.main:main'],
    }
)
