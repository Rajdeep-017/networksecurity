"""
setup.py because it

is an essential part of packaging and distributing Python projects.

It is used by Setuptools to define the configuration of a project such as its metadata dependency,
there will be some information about that particular project, such as metadata, dependencies,
It is responsible of entirely packaging and distributing your entire Python project.

It is also defining the configuration of your projects such as metadata, dependencies and more.
"""
#find_packages will consider the folder with __init__ considered as package
# the setup because this setup is responsible to provide all the information regarding the projects over here.
from setuptools import find_packages,setup
from typing import List
def get_requirments()->List[str]:
    """this fxn will return list of requirments"""
    requirment_list:List[str]=[]
    try:
        with open('requirments.txt','r') as file:
            #read line from file
            lines=file.readlines()
            #process each line
            for line in lines:
                requirment=line.strip()
                #ignore the .e and empty lines
                if requirment and requirment!='-e .':
                    requirment_list.append(requirment)
    except FileNotFoundError:
        print("reqiuirments.txt not found")
    
    return requirment_list

print(get_requirments())

setup(
    name='networksecurity',
    version='0.0.0.0',
    author='raj',
    author_email='rajdeepmatrix2004@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments()
)

