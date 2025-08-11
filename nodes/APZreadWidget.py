class APZmediaReadWidget:
    """
    A node that reads string values from other nodes' widgets.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": False, "default": ""}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "get_text"
    CATEGORY = "APZmedia"

    def get_text(self, text):
        """
        Returns the text input as a string output.
        """
        return (text,) 