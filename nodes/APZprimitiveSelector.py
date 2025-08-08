import datetime

class APZmediaPrimitiveSelector:
    """
    A node that provides primitive selection functionality and outputs the current selection as a string.
    This can be used for tagging filenames and other text-based operations.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "selection_type": (["Text", "Number", "Date", "Custom"], {"default": "Text"}),
                "text_selection": ("STRING", {"multiline": False, "default": ""}),
                "number_selection": ("INT", {"default": 1, "min": 1, "max": 9999, "step": 1}),
                "date_format": (["YYYY-MM-DD", "MM-DD-YYYY", "DD-MM-YYYY", "YYYYMMDD"], {"default": "YYYY-MM-DD"}),
                "custom_options": ("STRING", {"multiline": False, "default": "option1,option2,option3"}),
                "custom_selection": ("STRING", {"multiline": False, "default": "option1"}),
                "prefix": ("STRING", {"multiline": False, "default": ""}),
                "suffix": ("STRING", {"multiline": False, "default": ""}),
                "separator": ("STRING", {"multiline": False, "default": "_"}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING",)
    RETURN_NAMES = ("selection_text", "formatted_text",)

    FUNCTION = "get_selection"

    CATEGORY = "APZmedia"

    def get_selection(self, selection_type, text_selection, number_selection, date_format, 
                     custom_options, custom_selection, prefix, suffix, separator):
        """
        Returns the current selection as a string and a formatted version with prefix/suffix.
        """
        # Get the base selection based on type
        if selection_type == "Text":
            base_selection = text_selection or "default"
        elif selection_type == "Number":
            base_selection = str(number_selection)
        elif selection_type == "Date":
            today = datetime.datetime.now()
            if date_format == "YYYY-MM-DD":
                base_selection = today.strftime("%Y-%m-%d")
            elif date_format == "MM-DD-YYYY":
                base_selection = today.strftime("%m-%d-%Y")
            elif date_format == "DD-MM-YYYY":
                base_selection = today.strftime("%d-%m-%Y")
            elif date_format == "YYYYMMDD":
                base_selection = today.strftime("%Y%m%d")
            else:
                base_selection = today.strftime("%Y-%m-%d")
        elif selection_type == "Custom":
            # Parse custom options and find the selected one
            options = [opt.strip() for opt in custom_options.split(",") if opt.strip()]
            if custom_selection in options:
                base_selection = custom_selection
            else:
                base_selection = options[0] if options else "default"
        else:
            base_selection = "default"
        
        # Create formatted text with prefix and suffix
        parts = []
        if prefix:
            parts.append(prefix)
        parts.append(base_selection)
        if suffix:
            parts.append(suffix)
        
        formatted_text = separator.join(parts) if separator else "".join(parts)
        
        return (base_selection, formatted_text,)

    @classmethod
    def IS_CHANGED(s, selection_type, text_selection, number_selection, date_format, 
                   custom_options, custom_selection, prefix, suffix, separator):
        """
        Determine if the node should be re-executed.
        """
        return f"{selection_type}_{text_selection}_{number_selection}_{date_format}_{custom_options}_{custom_selection}_{prefix}_{suffix}_{separator}" 