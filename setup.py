#  it'll contain the genric info of our entire project
'''
The setup.py file is an essential part of packaging and distributing Python projects. It is used by setuptools (or distutils in older Python versions) to define the configuration of your project, such as its metadata, dependencies, and more.
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return a list of requirements
    from the 'requirements.txt' file.
    """
    requirement_lst: List[str] = []

    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                # Ignore empty lines and editable install
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("[ERROR] requirements.txt file not found.")

    return requirement_lst


# print(get_requirements())

setup(
    name="demo-networksecurity",
    version="0.0.1",
    author="Ankush Thakur",
    author_email="22bcs016@nith.ac.in",
    packages=find_packages(),
    install_requires=get_requirements()
    
    )