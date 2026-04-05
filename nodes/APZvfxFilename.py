class APZmediaVFXFilename:
    """
    Builds a filename following VFX/film pipeline conventions.
    Format: show_sequence_shot_pass_version
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "show":             ("STRING", {"multiline": False, "default": ""}),
                "toggle_show":      (["Include", "Exclude"],),
                "sequence":         ("STRING", {"multiline": False, "default": ""}),
                "toggle_sequence":  (["Include", "Exclude"],),
                "shot":             ("STRING", {"multiline": False, "default": ""}),
                "toggle_shot":      (["Include", "Exclude"],),
                "pass_name":        ("STRING", {"multiline": False, "default": ""}),
                "toggle_pass":      (["Include", "Exclude"],),
                "version":          ("STRING", {"multiline": False, "default": ""}),
                "toggle_version":   (["Include", "Exclude"],),
                "delimiter":        ("STRING", {"multiline": False, "default": "_"}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("filename",)
    FUNCTION = "build_filename"
    CATEGORY = "APZmedia/Naming"

    def build_filename(self, show, toggle_show, sequence, toggle_sequence,
                       shot, toggle_shot, pass_name, toggle_pass,
                       version, toggle_version, delimiter):
        parts = []
        if toggle_show == "Include" and show:
            parts.append(show)
        if toggle_sequence == "Include" and sequence:
            parts.append(sequence)
        if toggle_shot == "Include" and shot:
            parts.append(shot)
        if toggle_pass == "Include" and pass_name:
            parts.append(pass_name)
        if toggle_version == "Include" and version:
            parts.append(version)
        return (delimiter.join(parts),)

    @classmethod
    def IS_CHANGED(s, **kwargs):
        return str(kwargs)
