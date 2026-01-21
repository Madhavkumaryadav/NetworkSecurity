'''
The setup.py file is an essential part
of packaging and distributing python projects. 
It is used by setuptools (or distutils in older python 
versions) to define the configuration of your project,
such as its metadata, dependencies, and more 
'''

from setuptools import find_packages,setup
from typing import List 

def get_requirements():
    """
    This Function will return list of requirements 
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # Read lines from the file
            lines=file.readlines()
            ## process each line
            for line in lines:
                requirement=line.strip()
                ## Ignore the empty lines -e.
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    
    except FileNotFoundError:
        print("requirements.txt file not found ")
    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Madhav Kumar Yadav",
    author_email="Ymadhav081@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
 