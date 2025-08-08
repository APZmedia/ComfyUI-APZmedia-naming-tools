import datetime

class APZmediaPrimitive:
    """
    A primitive node that outputs different types of values for use in filename tagging and other operations.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "combo": (["text", "number", "date"], {"default": "text"}),
                "text": ("STRING", {"multiline": False, "default": ""}),
                "number": ("INT", {"default": 1, "min": 1, "max": 9999, "step": 1}),
                "date_format": (["YYYY-MM-DD", "MM-DD-YYYY", "DD-MM-YYYY", "YYYYMMDD"], {"default": "YYYY-MM-DD"}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "get_value"
    CATEGORY = "APZmedia"

    def get_value(self, combo, text, number, date_format):
        if combo == "text":
            return (text,)
        elif combo == "number":
            return (str(number),)
        elif combo == "date":
            today = datetime.datetime.now()
            if date_format == "YYYY-MM-DD":
                return (today.strftime("%Y-%m-%d"),)
            elif date_format == "MM-DD-YYYY":
                return (today.strftime("%m-%d-%Y"),)
            elif date_format == "DD-MM-YYYY":
                return (today.strftime("%d-%m-%Y"),)
            elif date_format == "YYYYMMDD":
                return (today.strftime("%Y%m%d"),)
            else:
                return (today.strftime("%Y-%m-%d"),)
        else:
            return ("",) 