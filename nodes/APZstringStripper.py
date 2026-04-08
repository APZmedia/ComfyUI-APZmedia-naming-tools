import re


class APZmediaStringStripper:
    """
    Extracts specific segments from a string based on a naming pattern.
    Supports Simple (delimiter-based) and Regex modes.
    Falls back to the original string if the pattern does not match.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input_text": ("STRING", {"multiline": False, "default": ""}),
                "mode": (["Simple", "Regex"],),
                "pattern": ("STRING", {"multiline": False, "default": "project-episode-shot-pass"}),
                "terms_to_keep": ("STRING", {"multiline": False, "default": "shot"}),
                "output_delimiter": ("STRING", {"multiline": False, "default": "-"}),
            },
        }

    RETURN_TYPES = ("STRING", "BOOLEAN")
    RETURN_NAMES = ("result", "matched")

    FUNCTION = "strip_string"

    CATEGORY = "APZmedia"

    def strip_string(self, input_text, mode, pattern, terms_to_keep, output_delimiter):
        if mode == "Simple":
            return self._simple_mode(input_text, pattern, terms_to_keep, output_delimiter)
        else:
            return self._regex_mode(input_text, pattern, terms_to_keep, output_delimiter)

    def _detect_delimiter(self, pattern):
        match = re.search(r'[^a-zA-Z0-9]', pattern)
        return match.group(0) if match else None

    def _simple_mode(self, input_text, pattern, terms_to_keep, output_delimiter):
        delimiter = self._detect_delimiter(pattern)
        if not delimiter:
            return (input_text, False)

        slot_names = pattern.split(delimiter)
        input_parts = input_text.split(delimiter)

        if len(slot_names) != len(input_parts):
            return (input_text, False)

        slot_map = dict(zip(slot_names, input_parts))
        keep = [t.strip() for t in terms_to_keep.split(",") if t.strip()]

        result_parts = []
        for term in keep:
            if term not in slot_map:
                return (input_text, False)
            result_parts.append(slot_map[term])

        return (output_delimiter.join(result_parts), True)

    def _regex_mode(self, input_text, pattern, terms_to_keep, output_delimiter):
        try:
            match = re.search(pattern, input_text)
        except re.error:
            return (input_text, False)

        if not match:
            return (input_text, False)

        keep = [t.strip() for t in terms_to_keep.split(",") if t.strip()]

        result_parts = []
        for term in keep:
            try:
                group = match.group(int(term)) if term.isdigit() else match.group(term)
                if group is None:
                    return (input_text, False)
                result_parts.append(group)
            except (IndexError, re.error):
                return (input_text, False)

        return (output_delimiter.join(result_parts), True)

    @classmethod
    def IS_CHANGED(s, input_text, mode, pattern, terms_to_keep, output_delimiter):
        return f"{input_text}_{mode}_{pattern}_{terms_to_keep}_{output_delimiter}"
