class APZmediaCycleInt:
    """
    Outputs an integer that cycles through a range each time the workflow runs.
    Useful for automating batches without touching the graph between runs.
    """

    def __init__(self):
        self._current = None

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "min_value": ("INT", {"default": 1,  "min": -999999, "max": 999999, "step": 1}),
                "max_value": ("INT", {"default": 10, "min": -999999, "max": 999999, "step": 1}),
                "step":      ("INT", {"default": 1,  "min": 1,       "max": 999999, "step": 1}),
                "direction": (["Increment", "Decrement"],),
            },
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("value",)
    FUNCTION = "get_value"
    CATEGORY = "APZmedia"

    def get_value(self, min_value, max_value, step, direction):
        # Tolerate min/max being swapped
        if min_value > max_value:
            min_value, max_value = max_value, min_value

        range_size = max_value - min_value + 1

        # First run: start at min (increment) or max (decrement)
        if self._current is None:
            self._current = min_value if direction == "Increment" else max_value
            return (self._current,)

        # If current is out of range (e.g. user changed min/max), reset
        if self._current < min_value or self._current > max_value:
            self._current = min_value if direction == "Increment" else max_value
            return (self._current,)

        # Advance with wrap-around
        offset = (self._current - min_value)
        if direction == "Increment":
            offset = (offset + step) % range_size
        else:
            offset = (offset - step) % range_size

        self._current = min_value + offset
        return (self._current,)

    @classmethod
    def IS_CHANGED(s, **kwargs):
        # Always re-execute so the counter advances every workflow run
        return float("nan")
