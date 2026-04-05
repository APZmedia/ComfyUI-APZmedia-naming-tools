from .nodes.APZnamefromtext import CleanFileNameNode
from .nodes.APZgeneratePathNode import GenerateFilePathNode
from .nodes.APZfileNameBuilder import APZmediaStandardFilenameBuilder
from .nodes.APZreadWidget import APZmediaReadWidget
from .nodes.APZloadImageWithFilename import APZmediaLoadImageWithFilename
from .nodes.APZdictionaryReplace import APZmediaDictionaryReplace
from .nodes.APZtextToHash import APZmediaTextToHash

NODE_CLASS_MAPPINGS = {
    "CleanFileNameNode": CleanFileNameNode,
    "APZmediaGenerateFilePath": GenerateFilePathNode,
    "APZmediaStandardFilenameBuilder": APZmediaStandardFilenameBuilder,
    "APZmediaReadWidget": APZmediaReadWidget,
    "APZmediaLoadImageWithFilename": APZmediaLoadImageWithFilename,
    "APZmediaDictionaryReplace": APZmediaDictionaryReplace,
    "APZmediaTextToHash": APZmediaTextToHash,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CleanFileNameNode": "APZmedia Clean File Name Node",
    "APZmediaGenerateFilePath": "APZmedia Generate File Path",
    "APZmediaStandardFilenameBuilder": "APZmedia Standard Filename Builder",
    "APZmediaReadWidget": "Read Widget",
    "APZmediaLoadImageWithFilename": "APZmedia Load Image with Filename",
    "APZmediaDictionaryReplace": "APZmedia Dictionary Based String Replacement",
    "APZmediaTextToHash": "APZmedia Text To Hash",
}
