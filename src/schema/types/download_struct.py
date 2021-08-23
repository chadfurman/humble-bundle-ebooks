from graphene import ObjectType, String, Field, Int, Date

from .download_struct_url import DownloadStructUrl

class DownloadStruct(ObjectType):
    """DownloadStruct contains checksums, URLs, sizes, etc for a SubProduct's downloads"""
    uploaded_at=Date(description="A date and time this file was made available for download.  For example, '2019-03-26T21:28:00.117829'"),
    sha1=String(description="The SHA1 checksum of this file, for example '38c6e8afe3f2e74569cc24845ca29cf6b218603e' Note: both SHA1 and MD5 may not be present")
    name=String(description="The name, for example 'Download' TODO: Why is the name Download?  What is this field?")
    url=Field(DownloadStructUrl)
    human_size=String(description="Human Readable file size, for example '677.1 MB'")
    file_size=Int(description="Machine readable file size in bytes.  For example 709940417")
    small=Int(description="Likely a flag of some sort.  Example Value: 0 -- TODO: What is the purpose of this?")
    md5=String(description="The MD5 Checksum of this file, for example 'dedcc64717a853644d54cfabe4413d06' Note: both SHA1 and MD5 may not be present")
