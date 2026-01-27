'''
The setup.py file is an essential part
of packaging and distributing python projects. 
It is used by setuptools (or distutils in older python 
versions) to define the configuration of your project,
such as its metadata, dependencies, and more 
'''

from setuptools import find_packages,setup #type:ignore
from typing import List 

def get_requirements():
    """
    This Function will return list of requirements 
    """
    requirement_lst: List[str] = []
    try:
        with open("requirements.txt", "r", encoding="utf-8") as file:
            for line in file:
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirement_lst


setup(
    name="NetworkSecurity",
    version="0.0.2",
    author="Madhav Kumar Yadav",
    author_email="Ymadhav081@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
 