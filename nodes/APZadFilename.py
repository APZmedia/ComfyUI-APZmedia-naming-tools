class APZmediaAdFilename:
    """
    Builds a filename following digital advertising conventions (Meta, Google, etc.).
    Format: brand_campaign_format_placement_ratio_version
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "brand":            ("STRING", {"multiline": False, "default": ""}),
                "toggle_brand":     (["Include", "Exclude"],),
                "campaign":         ("STRING", {"multiline": False, "default": ""}),
                "toggle_campaign":  (["Include", "Exclude"],),
                "format_type":      ("STRING", {"multiline": False, "default": ""}),
                "toggle_format":    (["Include", "Exclude"],),
                "placement":        ("STRING", {"multiline": False, "default": ""}),
                "toggle_placement": (["Include", "Exclude"],),
                "ratio":            ("STRING", {"multiline": False, "default": ""}),
                "toggle_ratio":     (["Include", "Exclude"],),
                "version":          ("STRING", {"multiline": False, "default": ""}),
                "toggle_version":   (["Include", "Exclude"],),
                "delimiter":        ("STRING", {"multiline": False, "default": "_"}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("filename",)
    FUNCTION = "build_filename"
    CATEGORY = "APZmedia/Naming"

    def build_filename(self, brand, toggle_brand, campaign, toggle_campaign,
                       format_type, toggle_format, placement, toggle_placement,
                       ratio, toggle_ratio, version, toggle_version, delimiter):
        parts = []
        if toggle_brand == "Include" and brand:
            parts.append(brand)
        if toggle_campaign == "Include" and campaign:
            parts.append(campaign)
        if toggle_format == "Include" and format_type:
            parts.append(format_type)
        if toggle_placement == "Include" and placement:
            parts.append(placement)
        if toggle_ratio == "Include" and ratio:
            parts.append(ratio)
        if toggle_version == "Include" and version:
            parts.append(version)
        return (delimiter.join(parts),)

    @classmethod
    def IS_CHANGED(s, **kwargs):
        return str(kwargs)
