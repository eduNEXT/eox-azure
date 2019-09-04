"""
AWS Django settings for eox_azure project.

Juniper release will remove aws.py file. https://openedx.atlassian.net/browse/DEPR-14
"""

from __future__ import unicode_literals

from .common import *  # pylint: disable=wildcard-import


def plugin_settings(settings):  # pylint: disable=function-redefined
    """
    Set of plugin settings used by the Open Edx platform.
    More info: https://github.com/edx/edx-platform/blob/master/openedx/core/djangoapps/plugins/README.rst
    """

    settings.AZURE_ACCOUNT_NAME = getattr(settings, 'AUTH_TOKENS', {}).get(
        'AZURE_ACCOUNT_NAME',
        None
    )

    settings.AZURE_ACCOUNT_KEY = getattr(settings, 'AUTH_TOKENS', {}).get(
        'AZURE_ACCOUNT_KEY',
        None
    )

    settings.AZURE_CONTAINER = getattr(settings, 'AUTH_TOKENS', {}).get(
        'AZURE_CONTAINER',
        None
    )

    if settings.AZURE_ACCOUNT_NAME and settings.AZURE_ACCOUNT_KEY and settings.AZURE_CONTAINER:

        settings.DEFAULT_FILE_STORAGE = getattr(settings, 'ENV_TOKENS', {}).get(
            'DEFAULT_FILE_STORAGE',
            'eox_azure.storage.AzureStorageExtended'
        )

        settings.ORA2_FILEUPLOAD_BACKEND = getattr(settings, 'AUTH_TOKENS', {}).get(
            'ORA2_FILEUPLOAD_BACKEND',
            'django'
        )

    # The azure version compatible with the django-storages version used in edx-platform at this moement
    # does not support large files

        settings.COURSE_IMPORT_EXPORT_STORAGE = getattr(settings, 'ENV_TOKENS', {}).get(
            'COURSE_IMPORT_EXPORT_STORAGE',
            'django.core.files.storage.FileSystemStorage'
        )

        settings.USER_TASKS_ARTIFACT_STORAGE = getattr(settings, 'ENV_TOKENS', {}).get(
            'USER_TASKS_ARTIFACT_STORAGE',
            'django.core.files.storage.FileSystemStorage'
        )
