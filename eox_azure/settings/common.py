"""
Common Django settings for eox_azure project.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

from __future__ import unicode_literals

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'secret-key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TIME_ZONE = 'UTC'

# This key needs to be defined so that the check_apps_ready passes and the
# AppRegistry is loaded
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}


def plugin_settings(settings):
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
        settings.DEFAULT_FILE_STORAGE = 'eox_azure.storage.AzureStorageExtended'
        settings.ORA2_FILEUPLOAD_BACKEND = "django"

        settings.COURSE_IMPORT_EXPORT_STORAGE = 'django.core.files.storage.FileSystemStorage'

        settings.USER_TASKS_ARTIFACT_STORAGE = settings.COURSE_IMPORT_EXPORT_STORAGE
