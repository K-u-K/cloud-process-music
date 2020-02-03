from setuptools import setup, find_packages
from setuptools.command.install import install 
import shutil
import os

class PostInstallCommand(install):

    def run(self):
        install.run(self)
        if os.path.exists("build"):
            print("Removing build")
            shutil.rmtree('build')
        if os.path.exists("backend_clc.egg-info"):
            print("Removing backend_clc.egg-info")
            shutil.rmtree('backend_clc.egg-info')

setup(name='backend_clc',
    version='1.0',
    description='Backend for CLC3',
    author='Keller Patrick & Kocaj Alen',
    platforms = ["windows", "linux"],
    packages = find_packages(),
    cmdclass = { 'install':PostInstallCommand }
)