from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'


# creating a function to open and read the "requirements.txt" file and execute the list of packages named in it (like numpy, pandas etc.).

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:                     # To avoid installing << -e . >>
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='RegressorProject',
    version='0.0.1',
    author='Mayur',
    author_email='mayurssoni007@gmail.com',
    install_requires=["requirements.txt"],
    packages=find_packages()
)



