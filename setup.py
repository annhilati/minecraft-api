from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as readme:
    description = readme.read() 
   
setup(
    name="minecraft-api",
    version="0.0.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "mcstatus"
        ],
    author="Annhilati",
    description="Python API wrapper library for fetching information regarding Minecraft",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/annhilati/minecraft-api"
)
