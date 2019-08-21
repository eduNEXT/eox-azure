"""
Setup file for eox_azure Django plugin.
"""

from __future__ import print_function

import os
import re

from setuptools import setup


def get_version(*file_paths):
    """
    Extract the version string from the file at the given relative path fragments.
    """
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


VERSION = get_version('eox_azure', '__init__.py')


setup(
    name='eox-azure',
    version=VERSION,
    description='Open edX Azure Plugin',
    author='eduNEXT',
    author_email='contact@edunext.co',
    packages=[
        'eox_azure'
    ],
    include_package_data=True,
    install_requires=['azure-storage==v0.20.3'],
    zip_safe=False,
    entry_points={
        "lms.djangoapp": [
            'eox_azure = eox_azure.apps:EoxAzureConfig',
        ],
        "cms.djangoapp": [
            'eox_azure = eox_azure.apps:EoxAzureConfig',
        ],
    }
)
