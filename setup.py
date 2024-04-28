from setuptools import setup, find_packages


def get_requirements(filepath: str):
    with open(filepath, 'r') as f :
        a = [i.replace("\n", "") for i in f.readlines() if i!="-e ."]
        return a
    
setup(name = "E2E_ML_Project1",version="0.0.0", author = "Vagheesh",
      packages= find_packages(), install_requires = get_requirements('requirements.txt'))

