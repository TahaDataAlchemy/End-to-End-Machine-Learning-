from setuptools import setup , find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirments(filepath:str)-> List[str]:
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements



setup(
     name = "ModularCoding",
     version="0.01",
     author="Taha",
     author_email="tahamehboob281@gmail.com",
     packages=find_packages(),
     install_requires = get_requirments('requirements.txt')

     )