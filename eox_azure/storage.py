"""
Module that defines the AzureStorage Wrapper.
"""
from datetime import datetime, timedelta

import pytz
from azure.storage import AccessPolicy, SharedAccessPolicy
from storages.backends.azure_storage import AzureStorage


class AzureStorageExtended(AzureStorage):  # pylint: disable=abstract-method
    """
    A wrapper around the django-stores implementation for Azure blob storage
    so that it is fully comptaible. The version in the library's repository
    is out of date
    """

    def __init__(self, container=None, url_expiry_secs=None, *args, **kwargs):  # pylint: disable=keyword-arg-before-vararg
        """
        Override base implementation so that we can accept a container
        parameter and an expiration on urls
        """

        super(AzureStorageExtended, self).__init__()
        self._connection = None

        self.url_expiry_secs = url_expiry_secs

        if container:
            self.azure_container = container

    def url(self, name):
        """
        Override this method so that we can add SAS authorization tokens
        """

        sas_token = None
        if self.url_expiry_secs:
            now = datetime.utcnow().replace(tzinfo=pytz.utc)
            expire_at = now + timedelta(seconds=self.url_expiry_secs)

            policy = AccessPolicy()
            # generate an ISO8601 time string and use split() to remove the sub-second
            # components as Azure will reject them. Plus add the timezone at the end.
            policy.expiry = expire_at.isoformat().split('.')[0] + 'Z'
            policy.permission = 'r'

            sas_token = self.connection.generate_shared_access_signature(
                self.azure_container,
                blob_name=name,
                shared_access_policy=SharedAccessPolicy(access_policy=policy),
            )

        return self.connection.make_blob_url(
            container_name=self.azure_container,
            blob_name=name,
            protocol=self.azure_protocol,
            sas_token=sas_token
        )

    def listdir(self, path):
        """
        The base implementation does not have a definition for this method
        which Open edX requires
        """
        if not path:
            path = None

        blobs = self.connection.list_blobs(
            container_name=self.azure_container,
            prefix=path,
        )
        results = []
        for f in blobs:
            name = f.name
            if path:
                name = name.replace(path, '')
            results.append(name)

        return ((), results)
