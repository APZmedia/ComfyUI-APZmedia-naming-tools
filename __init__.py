from .nodes.APZnamefromtext import CleanFileNameNode
from .nodes.APZgeneratePathNode import GenerateFilePathNode
from .nodes.APZfileNameBuilder import APZmediaStandardFilenameBuilder
from .nodes.APZprimitive import APZmediaPrimitive
from .nodes.APZimageFilename import APZmediaImageFilename

NODE_CLASS_MAPPINGS = {
    "CleanFileNameNode": CleanFileNameNode,
    "APZmediaGenerateFilePath": GenerateFilePathNode,
    "APZmediaStandardFilenameBuilder": APZmediaStandardFilenameBuilder,
    "APZmediaPrimitive": APZmediaPrimitive,
    "APZmediaImageFilename": APZmediaImageFilename,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CleanFileNameNode": "APZmedia Clean File Name Node",
    "APZmediaGenerateFilePath": "APZmedia Generate File Path",
    "APZmediaStandardFilenameBuilder": "APZmedia Standard Filename Builder",
    "APZmediaPrimitive": "Primitive",
    "APZmediaImageFilename": "APZmedia Image Filename",
}
