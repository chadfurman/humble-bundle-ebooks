from graphene import String, ObjectType, List, Field, Boolean

from .download_struct import DownloadStruct
from .options_dict import OptionsDict

class Download(ObjectType):
    """Download contains the metadata for a single download instance of a sub-product"""
    machine_name=String(description="The machine readable name of a download, for example 'highwayblossoms_windows'")
    platform=String(description="The platform for this download.  For example 'windows', 'mac', 'linux'.  TODO: make this an enum?  Check this for ebooks?")
    download_struct=List(Field(DownloadStruct), description="A list of the download structures.  These contain the URLs of the downloads.")
    options_dict=Field(OptionsDict, description="TODO: What is this?  It's an object, but what's inside of it?")
    download_identifier=String(description="TODO: What is this?")
    android_app_only=Boolean(description="Whether or not this is only an android app, I assume.  TODO: verify this property")
    download_version_number=String(description="TODO: What's the format of this?")