# EOX azure

eox-azure is a [django app plugin](https://github.com/edx/edx-platform/tree/master/openedx/core/djangoapps/plugins) for adding compatibilities with Azure (storage) for the [edx-platform](https://github.com/edx/edx-platform).

## Usage

1) Make sure that the config files are properly configured, i.e. lms.env.json ( /edx/etc/lms.yml), lms.auth.json, cms.env.json( /edx/etc/cms.yml ), cms.auth.json.

lms.auth.json and cms.auth.json should have 

```json
    "AZURE_ACCOUNT_KEY": "<Azure account storage key>", 
    "AZURE_ACCOUNT_NAME": "<Azure account storage name>", 
    "AZURE_CONTAINER": "<default container_name>", 
    ...
    "DEFAULT_FILE_STORAGE": "eox_azure.storage.AzureStorageExtended",
```

and the lms.env.json and cms.env.json should have:

```json
    "GRADES_DOWNLOAD": {
        "BUCKET": "", 
        "ROOT_PATH": "", 
        "STORAGE_CLASS": "eox_azure.storage.AzureStorageExtended", 
        "STORAGE_KWARGS": {
            "container": "<private container for grades>", 
            "url_expiry_secs": 300
        }, 
        "STORAGE_TYPE": ""
    }, 

    ...
    "DEFAULT_FILE_STORAGE": "eox_azure.storage.AzureStorageExtended",

    "PROFILE_IMAGE_BACKEND": {
        "class": "eox_azure.storage.AzureStorageExtended", 
        "options": {}
    }, 
    ...
    "VIDEO_IMAGE_SETTINGS": {
        "DIRECTORY_PREFIX": "video-images/", 
        "STORAGE_KWARGS": {
            "container": "<container for video-images>"
        }, 
        "VIDEO_IMAGE_MAX_BYTES": 2097152, 
        "VIDEO_IMAGE_MIN_BYTES": 2048
    }, 
    ...
    "VIDEO_TRANSCRIPTS_SETTINGS": {
        "DIRECTORY_PREFIX": "video-transcripts/", 
        "STORAGE_KWARGS": {
            "container": "<container for video-transcripts>"
        }, 
        "VIDEO_TRANSCRIPTS_MAX_BYTES": 3145728
    }, 

```

## Installation
- Create an edx hawthorn/ironwood instance if it doesn't exist already:
- Install plugin

Using the bash:
```bash
source /edx/app/edxapp/venvs/edxapp/bin/activate
pip install git+https://github.com/eduNEXT/eox-azure.git@x.x.x#egg=eox-azure==x.x.x # Change x.x.x for the actual release value.
```

If the edx-platform is installed using ansible, use the following variables to install the plugin:

```yaml
EDXAPP_EXTRA_REQUIREMENTS:
    - name: 'git+https://github.com/eduNEXT/eox-azure.git@x.x.x#egg=eox-azure==x.x.x'

# Basic definition of azure variables
EDXAPP_AZURE_ACCOUNT_NAME:  '<Azure account storage name>'
EDXAPP_AZURE_ACCOUNT_KEY: '<Azure account storage key>'
EDXAPP_AZURE_CONTAINER: '<default container_name>'

EDXAPP_AUTH_EXTRA:
  AZURE_ACCOUNT_NAME: "{{ EDXAPP_AZURE_ACCOUNT_NAME  }}"
  AZURE_ACCOUNT_KEY: "{{ EDXAPP_AZURE_ACCOUNT_KEY }}"
  AZURE_CONTAINER:  "{{ EDXAPP_AZURE_CONTAINER }}"


# Time interval in which the link with the report is available.
REPORTS_EXPIRATION_TIME: 300 #seconds
EDXAPP_AZURE_CONTAINER_PRIVATE: "<private container for grades>"
EDXAPP_GRADE_STORAGE_CLASS: 'eox_azure.storage.AzureStorageExtended'
EDXAPP_GRADE_STORAGE_KWARGS:
    url_expiry_secs:  "{{ REPORTS_EXPIRATION_TIME }}"
    container: "{{ EDXAPP_AZURE_CONTAINER_PRIVATE }}"


EDXAPP_PROFILE_IMAGE_BACKEND:
  class: 'eox_azure.storage.AzureStorageExtended'
  options: {}

EDXAPP_VIDEO_IMAGE_SETTINGS:
  VIDEO_IMAGE_MAX_BYTES : 2097152
  VIDEO_IMAGE_MIN_BYTES : 2048
  STORAGE_KWARGS:
    container: "{{ EDXAPP_AZURE_CONTAINER }}"
  DIRECTORY_PREFIX: 'video-images/'

EDXAPP_VIDEO_TRANSCRIPTS_SETTINGS:
  VIDEO_TRANSCRIPTS_MAX_BYTES : 3145728
  STORAGE_KWARGS:
    container: "{{ EDXAPP_AZURE_CONTAINER }}"
  DIRECTORY_PREFIX: 'video-transcripts/'

```


