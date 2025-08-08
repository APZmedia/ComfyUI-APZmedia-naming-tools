class APZmediaSimplePrimitive:
    """
    A simple primitive node that outputs text values for use in filename tagging and other operations.
    Follows standard ComfyUI primitive node patterns.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text_value": ("STRING", {"multiline": False, "default": ""}),
                "number_value": ("INT", {"default": 1, "min": 1, "max": 9999, "step": 1}),
                "float_value": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1000.0, "step": 0.1}),
                "boolean_value": ("BOOLEAN", {"default": True}),
            },
        }

    RETURN_TYPES = ("STRING", "INT", "FLOAT", "STRING",)
    RETURN_NAMES = ("text_output", "number_output", "float_output", "boolean_text",)

    FUNCTION = "get_values"

    CATEGORY = "APZmedia"

    def get_values(self, text_value, number_value, float_value, boolean_value):
        """
        Returns the input values as outputs for use in other nodes.
        """
        # Convert boolean to text representation
        boolean_text = "true" if boolean_value else "false"
        
        return (text_value, number_value, float_value, boolean_text,)

    @classmethod
    def IS_CHANGED(s, text_value, number_value, float_value, boolean_value):
        """
        Determine if the node should be re-executed.
        """
        return f"{text_value}_{number_value}_{float_value}_{boolean_value}" 