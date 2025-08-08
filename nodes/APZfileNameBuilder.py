class APZmediaStandardFilenameBuilder:
    """
    A node that concatenates project, episode, shot, and pass names based on the inclusion selectors.
    The user can select a delimiter to separate each segment, with a hyphen as the default.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "project_name": ("STRING", {"multiline": False, "default": ""}),
                "episode_name": ("STRING", {"multiline": False, "default": ""}),
                "shot_name": ("STRING", {"multiline": False, "default": ""}),
                "pass_name": ("STRING", {"multiline": False, "default": ""}),
                "delimiter": ("STRING", {"multiline": False, "default": "-"}),
                "toggle_project_name": (["Include", "Exclude"], {"default": "Include"}),
                "toggle_episode_name": (["Include", "Exclude"], {"default": "Include"}),
                "toggle_shot_name": (["Include", "Exclude"], {"default": "Include"}),
                "toggle_pass_name": (["Include", "Exclude"], {"default": "Include"}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("concatenated_name",)

    FUNCTION = "concatenate_names"

    CATEGORY = "APZmedia"

    def concatenate_names(self, project_name, episode_name, shot_name, pass_name, delimiter,
                          toggle_project_name, toggle_episode_name, toggle_shot_name, toggle_pass_name):
        """
        Concatenates the names based on the selected inclusion and delimiter.
        """
        # Prepare the list to store each valid name component
        name_parts = []
        
        # Append each part based on the corresponding dropdown value and non-empty string
        if toggle_project_name == "Include" and project_name:
            name_parts.append(project_name)
        if toggle_episode_name == "Include" and episode_name:
            name_parts.append(episode_name)
        if toggle_shot_name == "Include" and shot_name:
            name_parts.append(shot_name)
        if toggle_pass_name == "Include" and pass_name:
            name_parts.append(pass_name)
        
        # Join the parts using the selected delimiter
        concatenated_name = delimiter.join(name_parts)

        return (concatenated_name,)

    @classmethod
    def IS_CHANGED(s, project_name, episode_name, shot_name, pass_name, delimiter, 
                   toggle_project_name, toggle_episode_name, toggle_shot_name, toggle_pass_name):
        """
        Determine if the node should be re-executed.
        """
        return f"{project_name}_{episode_name}_{shot_name}_{pass_name}_{delimiter}_{toggle_project_name}_{toggle_episode_name}_{toggle_shot_name}_{toggle_pass_name}"
