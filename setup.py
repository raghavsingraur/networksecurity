''' The `setup.py` file is a key script for packaging and distributing Python projects. It defines the 
project’s metadata (name, version, author, etc.), manages dependencies, and enables easy installation 
using commands like `python setup.py install`. It also supports creating distributable packages with
`python setup.py sdist` and allows defining entry points for command-line tools. While modern tools like
`pyproject.toml` are emerging, `setup.py` remains widely used for building and sharing Python packages.'''


from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """

    This function will return list of requirements.

    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # read lines from the file
            lines=file.readlines()
            ## Process each line

            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Kuwar raghvendra Singh",
    author_email="kuwarraghvendra.singh@gmail.com",
    packages=find_packages(),
    install_reuires=get_requirements()
)
