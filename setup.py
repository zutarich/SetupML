from setuptools import find_packages,setup


HYPEN_E_DOT='-e .'

from typing import List

def get_requirements(file_path:str)->List[str]:
    '''this function returns the list of requirements'''
    requirement=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='ML Project',
    version='0.0.1',
    author='Snehlata',
    author_email='atalhens201@gmail.com',
    packages=find_packages(),
    #sometimes we require 100's of these packages thus installing it this way is not feasible thus we are creating a function so a sto make it feasible
    # install_requires=['pandas','numpy','seaborn']
    install_requires=get_requirements('requirements.txt')
)