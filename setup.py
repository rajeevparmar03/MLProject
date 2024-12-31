from setuptools import find_packages ,setup
from typing import List 

HYPEN_E_DOT ='-e'

def get_requirements(file_path: str )-> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readline()
        requirements = [req.replace("\n", "") for req in requirements]


setup(
    name= "MLProject",
    version='1.1.0',
    author= 'Rajeev',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)