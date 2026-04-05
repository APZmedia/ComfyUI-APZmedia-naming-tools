import os

class GenerateFilePathNode:
    """
    Generates a file path from components with configurable path separator.
    Each segment can be toggled on or off.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "root_folder":          ("STRING", {"multiline": False, "default": ""}),
                "toggle_root_folder":   (["Include", "Exclude"],),
                "project_name":         ("STRING", {"multiline": False, "default": ""}),
                "toggle_project_name":  (["Include", "Exclude"],),
                "episode_name":         ("STRING", {"multiline": False, "default": ""}),
                "toggle_episode_name":  (["Include", "Exclude"],),
                "shot_name":            ("STRING", {"multiline": False, "default": ""}),
                "toggle_shot_name":     (["Include", "Exclude"],),
                "pass_name":            ("STRING", {"multiline": False, "default": ""}),
                "toggle_pass_name":     (["Include", "Exclude"],),
                "slash_type":           (["Auto", "Forward (/)", "Backslash (\\)"],),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("generated_path",)
    FUNCTION = "generate_path"
    CATEGORY = "APZmedia"

    def generate_path(self, root_folder, toggle_root_folder, project_name, toggle_project_name,
                      episode_name, toggle_episode_name, shot_name, toggle_shot_name,
                      pass_name, toggle_pass_name, slash_type):

        path_parts = []
        if toggle_root_folder == "Include" and root_folder:
            path_parts.append(root_folder)
        if toggle_project_name == "Include" and project_name:
            path_parts.append(project_name)
        if toggle_episode_name == "Include" and episode_name:
            path_parts.append(episode_name)
        if toggle_shot_name == "Include" and shot_name:
            path_parts.append(shot_name)
        if toggle_pass_name == "Include" and pass_name:
            path_parts.append(pass_name)

        if not path_parts:
            return ("",)

        generated_path = os.path.join(*path_parts)

        if slash_type == "Forward (/)":
            generated_path = generated_path.replace("\\", "/")
        elif slash_type == "Backslash (\\)":
            generated_path = generated_path.replace("/", "\\")
        else:  # Auto
            generated_path = generated_path.replace(os.sep, "/") if os.sep == "\\" else generated_path

        return (generated_path,)

    @classmethod
    def IS_CHANGED(s, **kwargs):
        return str(kwargs)
