import os.path
import json
import subprocess
from setuptools import setup, find_packages
from setuptools.command.install import install
from notebook import version_info
from notebook.nbextensions import (
    install_nbextension,
    install_nbextension_python
)
from jupyter_core.paths import jupyter_config_dir

JS_DIR = os.path.join(os.path.dirname(__file__), 'git_ext/static')


class InstallCommand(install):
    def run(self):
        install.run(self)

        install_nbextension(JS_DIR, overwrite=True, user=True)
        install_nbextension_python('git_ext')

        # enable notebook extension
        out = subprocess.run(
            'jupyter nbextension enable --py --sys-prefix git_ext',
            stdout=subprocess.PIPE,
            shell=True, check=True)

        # enable server extension
        configure_path = os.path.join(jupyter_config_dir(),
                                      'jupyter_notebook_config.json')
        try:
            configure = json.load(open(configure_path))
            if 'NotebookApp' not in configure:
                configure['NotebookApp'] = {}
            configure['NotebookApp'].update({
                'disable_check_xsrf': True
            })
            if 'nbserver_extensions' not in configure['NotebookApp']:
                configure['NotebookApp']['nbserver_extensions'] = {}
            configure['NotebookApp']['nbserver_extensions'].update({
                'git_ext': True
            })
        except FileNotFoundError:
            configure = {
                'NotebookApp': {
                    'nbserver_extensions': {
                        'git_ext': True
                    },
                    'disable_check_xsrf': True
                }
            }
        finally:
            json.dump(configure, open(configure_path, 'w'), indent=2)


setup(
    name='git_ext',
    version='0.0.1',
    description='Enable your jupyter notebook to operate git',
    author='Yujiro terazawa (TeraBytesMemory)',
    install_requires=[
        'jupyter>=1.0.0'
    ],
    url='https://github.com/TeraBytesMemory/jupyter-git-ext',
    license='MIT',
    packages=find_packages(),
    cmdclass={
        'install': InstallCommand
    }
)
