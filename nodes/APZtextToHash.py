import hashlib


class APZmediaTextToHash:
    """
    Converts any text or numerical input to a hash string.
    The hash length can be controlled via a widget (up to 64 characters for SHA-256).
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input_value": ("*", {}),
                "hash_length": ("INT", {
                    "default": 8,
                    "min": 1,
                    "max": 64,
                    "step": 1,
                    "display": "number",
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("hash",)
    FUNCTION = "compute_hash"
    CATEGORY = "APZmedia"

    def compute_hash(self, input_value, hash_length):
        text = str(input_value)
        full_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
        return (full_hash[:hash_length],)

    @classmethod
    def IS_CHANGED(s, input_value, hash_length):
        return f"{input_value}_{hash_length}"
