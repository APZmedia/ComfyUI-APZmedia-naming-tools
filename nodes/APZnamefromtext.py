import re
import unidecode

class CleanFileNameNode:
    """
    A node that cleans file names by replacing spaces with a specified character,
    removing invalid characters and line breaks, adding a prefix, and truncating the result to a specified length.
    Additionally, it substitutes accented characters with their corresponding unaccented characters.

    Class methods
    -------------
    INPUT_TYPES (dict): 
        Defines the input parameters of the node.
    IS_CHANGED:
        Optional method to control when the node is re-executed.

    Attributes
    ----------
    RETURN_TYPES (`tuple`): 
        The type of each element in the output tuple.
    RETURN_NAMES (`tuple`):
        Optional: The name of each output in the output tuple.
    FUNCTION (`str`):
        The name of the entry-point method. For example, if `FUNCTION = "execute"` then it will run CleanFileNameNode().execute()
    OUTPUT_NODE ([`bool`]):
        If this node is an output node that outputs a result/image from the graph. Assumed to be False if not present.
    CATEGORY (`str`):
        The category the node should appear in the UI.
    execute(s) -> tuple || None:
        The entry point method. The name of this method must be the same as the value of property `FUNCTION`.
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input_text": ("STRING", {"multiline": False, "default": ""}),
                "replacement_char": ("STRING", {"multiline": False, "default": "-"}),
                "invalid_chars": ("STRING", {"multiline": False, "default": r" #%&{}\\<>*?/ $!'\":@+`|=."}),
                "prefix": ("STRING", {"multiline": False, "default": ""}),
                "char_limit": ("INT", {
                    "default": 255, 
                    "min": 1, 
                    "max": 4096, 
                    "step": 1, 
                    "display": "number"
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("cleaned_text",)

    FUNCTION = "clean_text"

    CATEGORY = "APZmedia"

    def clean_text(self, input_text, replacement_char, invalid_chars, prefix, char_limit):
        if not replacement_char:
            replacement_char = "-"
        
        # Compile the invalid characters into a regular expression
        invalid_chars_re = re.compile(f"[{re.escape(invalid_chars)}]")
        
        # Substitute accented characters with their unaccented equivalents
        cleaned_text = unidecode.unidecode(input_text)
        
        # Replace spaces with the replacement character
        cleaned_text = cleaned_text.replace(" ", replacement_char)
        
        # Remove line breaks
        cleaned_text = cleaned_text.replace("\n", "").replace("\r", "")
        
        # Remove invalid characters
        cleaned_text = invalid_chars_re.sub(replacement_char, cleaned_text)
        
        # Remove any consecutive replacement characters
        cleaned_text = re.sub(f'{replacement_char}+', replacement_char, cleaned_text)

        # Add the prefix
        final_text = prefix + cleaned_text
        
        # Ensure the final text length does not exceed the character limit
        final_text = final_text[:char_limit]
        
        return (final_text,)

    @classmethod
    def IS_CHANGED(s, input_text, replacement_char, invalid_chars, prefix, char_limit):
        return f"{input_text}_{replacement_char}_{invalid_chars}_{prefix}_{char_limit}"
