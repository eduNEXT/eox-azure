"""
App configuration for eox_azure.
"""

from __future__ import unicode_literals

from django.apps import AppConfig


class EoxAzureConfig(AppConfig):
    """
    Open edX Azure Plugin configuration.
    """
    name = 'eox_azure'
    verbose_name = 'Open edX Azure Plugin'

    plugin_app = {
        'settings_config': {
            'lms.djangoapp': {
                'common': {'relative_path': 'settings.common'},
                'test': {'relative_path': 'settings.test'},
                'aws': {'relative_path': 'settings.aws'},
            },
            'cms.djangoapp': {
                'common': {'relative_path': 'settings.common'},
                'test': {'relative_path': 'settings.test'},
                'aws': {'relative_path': 'settings.aws'},
            },
        }
    }
