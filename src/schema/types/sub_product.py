from graphene import ObjectType, Field, String, List

from .download import Download
from .sub_product_payee import SubProductPayee

class SubProduct(ObjectType):
    """SubProducts of a Product.  For example, if you purchase a game bundle, these would be the games."""
    machine_name=String(description="The machine readable name of this sub-product, for example 'highwayblossoms'")
    url=String(description="The URL for the sub product.  Note this is likely not the download URL, but the URL of the website for the product, for example 'https://sekaiproject.com/'")
    downloads=List(Field(Download), description="A list of downloads, usually URLs.  See the Download type for more information.")
    library_family_name=String(description="TODO: What is this?")
    payee= Field(SubProductPayee)
    human_name=String(description="The human readable name for this sub-product.  For example, 'Highway Blossoms'")
    custom_download_page_box_css=String(description="Any custom CSS used on the download page box for this sub-product.")
    custom_download_page_box_html=String(description="Any custom HTML used on the download page box for this sub-product.")
    icon=String(description="URL for the icon of this sub-product.  For example, 'https://hb.imgix.net/b0e26dc6f3fcae4991d7f795deef34562a28f2c2.png?auto=compress,format&s=0f97f01241b1d40b18e548b06f13a50f'")
