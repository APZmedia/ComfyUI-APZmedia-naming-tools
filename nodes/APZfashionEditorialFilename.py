class APZmediaFashionEditorialFilename:
    """
    Builds a filename following fashion editorial / lookbook conventions.
    Format: season_collection_look_shot_version
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "season":           ("STRING", {"multiline": False, "default": ""}),
                "toggle_season":    (["Include", "Exclude"],),
                "collection":       ("STRING", {"multiline": False, "default": ""}),
                "toggle_collection":(["Include", "Exclude"],),
                "look":             ("STRING", {"multiline": False, "default": ""}),
                "toggle_look":      (["Include", "Exclude"],),
                "shot":             ("STRING", {"multiline": False, "default": ""}),
                "toggle_shot":      (["Include", "Exclude"],),
                "version":          ("STRING", {"multiline": False, "default": ""}),
                "toggle_version":   (["Include", "Exclude"],),
                "delimiter":        ("STRING", {"multiline": False, "default": "_"}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("filename",)
    FUNCTION = "build_filename"
    CATEGORY = "APZmedia/Naming"

    def build_filename(self, season, toggle_season, collection, toggle_collection,
                       look, toggle_look, shot, toggle_shot,
                       version, toggle_version, delimiter):
        parts = []
        if toggle_season == "Include" and season:
            parts.append(season)
        if toggle_collection == "Include" and collection:
            parts.append(collection)
        if toggle_look == "Include" and look:
            parts.append(look)
        if toggle_shot == "Include" and shot:
            parts.append(shot)
        if toggle_version == "Include" and version:
            parts.append(version)
        return (delimiter.join(parts),)

    @classmethod
    def IS_CHANGED(s, **kwargs):
        return str(kwargs)
