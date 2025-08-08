import os

class APZmediaImageFilename:
    """
    A node that extracts the filename from an image for use in naming operations.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("STRING", "STRING",)
    RETURN_NAMES = ("filename", "filename_without_ext",)

    FUNCTION = "extract_filename"
    CATEGORY = "APZmedia"

    def extract_filename(self, image):
        """
        Extracts the filename from the image metadata.
        """
        # Get the filename from the image metadata
        filename = ""
        filename_without_ext = ""
        
        # Check if the image has metadata with filename
        if hasattr(image, 'filename'):
            filename = image.filename
        elif hasattr(image, 'metadata') and 'filename' in image.metadata:
            filename = image.metadata['filename']
        else:
            # Try to get from the image object's attributes
            try:
                if hasattr(image, '_filename'):
                    filename = image._filename
                elif hasattr(image, 'name'):
                    filename = image.name
            except:
                pass
        
        # If we found a filename, extract the name without extension
        if filename:
            filename_without_ext = os.path.splitext(os.path.basename(filename))[0]
        else:
            filename = "unknown"
            filename_without_ext = "unknown"
        
        return (filename, filename_without_ext,) 