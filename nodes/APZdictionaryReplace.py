import re


class APZmediaDictionaryReplace:
    """
    A node that performs string replacements based on a dictionary.
    The dictionary input is a multiline string where each line follows the format:
        "key" | "value"
    All occurrences of each key are replaced with the corresponding value.
    Accepts any input type and converts it to string before processing.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input_text": ("*", {}),
                "dictionary": ("STRING", {
                    "multiline": True,
                    "default": '"key" | "value"\n"another key" | "another value"',
                }),
            },
        }

    INPUT_IS_LIST = False
    RETURN_TYPES = ("STRING", "INT")
    RETURN_NAMES = ("replaced_text", "replacement_count")
    FUNCTION = "replace_text"
    CATEGORY = "APZmedia"

    def replace_text(self, input_text, dictionary):
        # Convert any input type to string
        text = str(input_text)

        # Parse the dictionary string
        replacements = []
        for line in dictionary.splitlines():
            line = line.strip()
            if not line:
                continue
            # Match: "key" | "value" — quotes are required, pipe is the separator
            match = re.match(r'^"((?:[^"\\]|\\.)*)"\s*\|\s*"((?:[^"\\]|\\.)*)"$', line)
            if match:
                key = match.group(1)
                value = match.group(2)
                replacements.append((key, value))

        total_count = 0
        result = text
        for key, value in replacements:
            if not key:
                continue
            count = result.count(key)
            if count > 0:
                result = result.replace(key, value)
                total_count += count

        return (result, total_count)

    @classmethod
    def IS_CHANGED(s, input_text, dictionary):
        return f"{input_text}_{dictionary}"
