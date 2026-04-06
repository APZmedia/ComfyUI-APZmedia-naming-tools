import os

class GenerateFilePathNode:
    """
    A node that generates a file path based on various input segments (root folder, project name, episode name, shot name, and pass).
    Each segment can be toggled on or off using a dropdown menu. The node generates paths with the correct separator for the operating system.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "root_folder":          ("STRING", {"multiline": False, "default": ""}),
                "project_name":         ("STRING", {"multiline": False, "default": ""}),
                "episode_name":         ("STRING", {"multiline": False, "default": ""}),
                "shot_name":            ("STRING", {"multiline": False, "default": ""}),
                "pass_name":            ("STRING", {"multiline": False, "default": ""}),
                "slash_type":           (["Forward (/)", "Backslash (\\)", "Auto"],),
                "toggle_root_folder":   (["Include", "Exclude"], {"default": "Include"}),
                "toggle_project_name":  (["Include", "Exclude"], {"default": "Include"}),
                "toggle_episode_name":  (["Include", "Exclude"], {"default": "Include"}),
                "toggle_shot_name":     (["Include", "Exclude"], {"default": "Include"}),
                "toggle_pass_name":     (["Include", "Exclude"], {"default": "Include"}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("generated_path",)
    FUNCTION = "generate_path"
    CATEGORY = "APZmedia"

    def generate_path(self, root_folder, project_name, episode_name, shot_name, pass_name,
                      slash_type, toggle_root_folder, toggle_project_name, toggle_episode_name,
                      toggle_shot_name, toggle_pass_name):

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
            generated_path = generated_path.replace("\\", "/")

        return (generated_path,)

    @classmethod
    def IS_CHANGED(s, root_folder, project_name, episode_name, shot_name, pass_name,
                   slash_type, toggle_root_folder, toggle_project_name, toggle_episode_name,
                   toggle_shot_name, toggle_pass_name):
        return f"{root_folder}_{project_name}_{episode_name}_{shot_name}_{pass_name}_{slash_type}_{toggle_root_folder}_{toggle_project_name}_{toggle_episode_name}_{toggle_shot_name}_{toggle_pass_name}"
