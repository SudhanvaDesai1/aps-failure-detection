from setuptools import find_packages,setup

from typing import List

REQUIREMENT_FILE_NAME="requirements.txt"

eifan="-e ."
def get_requirements() -> List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]
        if eifan in requirement_list:
            requirement_list.remove(eifan)
        return requirement_list 

setup(
    name = "sensor",
    version = "0.0.1",
    author = "Sudhanva",
    email = "sudhanvadesai1121@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(),
)

