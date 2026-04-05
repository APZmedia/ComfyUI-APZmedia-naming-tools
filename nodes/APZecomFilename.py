class APZmediaEcomFilename:
    """
    Builds a filename following general e-commerce product photography conventions.
    Format: brand_product_variant_view_sequence
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "brand":            ("STRING", {"multiline": False, "default": ""}),
                "toggle_brand":     (["Include", "Exclude"],),
                "product":          ("STRING", {"multiline": False, "default": ""}),
                "toggle_product":   (["Include", "Exclude"],),
                "variant":          ("STRING", {"multiline": False, "default": ""}),
                "toggle_variant":   (["Include", "Exclude"],),
                "view":             ("STRING", {"multiline": False, "default": ""}),
                "toggle_view":      (["Include", "Exclude"],),
                "sequence":         ("STRING", {"multiline": False, "default": ""}),
                "toggle_sequence":  (["Include", "Exclude"],),
                "delimiter":        ("STRING", {"multiline": False, "default": "_"}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("filename",)
    FUNCTION = "build_filename"
    CATEGORY = "APZmedia/Naming"

    def build_filename(self, brand, toggle_brand, product, toggle_product,
                       variant, toggle_variant, view, toggle_view,
                       sequence, toggle_sequence, delimiter):
        parts = []
        if toggle_brand == "Include" and brand:
            parts.append(brand)
        if toggle_product == "Include" and product:
            parts.append(product)
        if toggle_variant == "Include" and variant:
            parts.append(variant)
        if toggle_view == "Include" and view:
            parts.append(view)
        if toggle_sequence == "Include" and sequence:
            parts.append(sequence)
        return (delimiter.join(parts),)

    @classmethod
    def IS_CHANGED(s, **kwargs):
        return str(kwargs)
