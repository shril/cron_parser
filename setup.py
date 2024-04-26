from setuptools import setup

setup(
    name="cron_parser",
    version="0.1",
    description="Cron Parsing Library",
    author_email="shril.iitdhn@gmail.com",
    packages=["cron_parser"],
    package_dir={"": "src"},
    entry_points={
        'console_scripts': [
            'cron_parser=cron_parser.__main__:main'],
    }
)
