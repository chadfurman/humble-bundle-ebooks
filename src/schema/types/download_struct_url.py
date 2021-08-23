from graphene import ObjectType, String

class DownloadStructUrl(ObjectType):
    """DownloadStructUrl contains the links to download the file."""
    web=String(description="A URL for directly downloading the file from humble bundle.  ")
    bittorrent = String(description="A URL for downloading the torrent from humble bundle for use in a BT client")
