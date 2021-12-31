from graphene import List, String, Int, Boolean, ObjectType

@dataclass
class Tpkd(ObjectType):
    """A Humble Bundle TPKD, which is like a product key (TODO: What's a TPKD, exactly?)"""
    exclusive_countries=List(String(), description="List of countries where this product is available. TODO: What is the format of a country?")
    machine_name=String(description="Machine-readable name for this tpkd.  For example, '2danimation_softwarebundle_bt1_reallusion'")
    gamekey=String(description="Key used to access this product.  For example, '2AZm2qDRvVUesbKY'")
    custom_instructions_html=String(description="""String of raw HTML used to display instructions for this product.  For example: <div class=\"instructions_html overgrowthspf_instruct\" style=\"text-align: center;\">\r\n\t<center>\r\n\t\t<p style=\"font-size: 15px\">\r\n\t\t\t <a href=\"https://support.humblebundle.com/hc/en-us/articles/360038790114\" target=\"_blank\">Redemption Instructions</a>.\r\n\t\t</p>\r\n\t</center>\r\n</div>""")
    disallowed_countries=List(String(), description="List of countries where this product is not allowed. TODO: What's the format of a country here?")
    show_custom_instructions_in_user_libraries=Boolean(description="A flag informing the Humble Bundle API if the custom_instructions_html should be shown or not")
    key_type=String(description="TODO: make this an enum with the types of keys.  For example, 'generic'")
    visible=Boolean(description="A flag indicating whether or not this product is visible.  TODO: What impact does this have?")
    sold_out=Boolean(description="A flag indicating whether or not this product is sold out.  TODO: What impact does this have?")
    display_separately=Boolean(description="A flag indicating whether this product should be displayed separately.  TODO: What impact does this have?")
    instructions_html=String(description="""HTML used to display instructions.  For example, <a href='https://support.humblebundle.com/hc/articles/204008710-How-To-Redeem-Steam-Keys' target='_blank'>Steam Instructions</a>""")
    key_type_human_name=String(description="The type of key this is.  For example, 'Steam', 'other', ... etc.  TODO: Make this an enum"),
    steam_app_id=Int(description="TODO: What's this field for?")
    human_name=String(description="The human readable name of this tpkd.  For example '2D Animation $1 Tier' -- TODO what's a TPKD")
    preinstruction_text=String(description="Text to display before the other instructions.  For example, 'Copy this key into the Steam client, or click Redeem to redeem in-browser.'")
    css_class=String(description="The CSS class to apply to the key button.  For example, 'steambutton', 'genericbutton', etc.  TODO: Make this an enum")
    disclaimer=String(description="Disclaimer text for use with this key.  For example, 'Steam will not provide extra giftable copies of games you already own.'")
    direct_redeem=Boolean(description="Whether or not this key can be directly redeemed.  TODO: What are the implications of this?")
    keyindex=Int(description="The ordering for this key.  Starts at 0.")
    auto_expand=Boolean(description="A flag indicating if this key should be automatically expanded.")
    is_expired=Boolean(description="A flag indicating if this key is expired or not.")
    num_days_until_expired=Int(description="The number of days until this key expires.  -1 means it does not expire.")
