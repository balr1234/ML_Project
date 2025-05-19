from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'
requirements=[]
def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements
setup(

name="MLPROJECT", 
version='0.0.1',
author="balram",
author_email="balram9947@gmail.com",
packages=find_packages(),
Install_requires=get_requirements("requirements.txt ")#this function for get our librarys

)