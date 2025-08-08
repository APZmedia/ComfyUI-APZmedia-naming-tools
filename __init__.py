from .nodes.APZnamefromtext import CleanFileNameNode
from .nodes.APZgeneratePathNode import GenerateFilePathNode
from .nodes.APZfileNameBuilder import APZmediaStandardFilenameBuilder
from .nodes.APZprimitiveSelector import APZmediaPrimitiveSelector
from .nodes.APZsimplePrimitive import APZmediaSimplePrimitive

NODE_CLASS_MAPPINGS = {
    "CleanFileNameNode": CleanFileNameNode,
    "APZmediaGenerateFilePath": GenerateFilePathNode,
    "APZmediaStandardFilenameBuilder": APZmediaStandardFilenameBuilder,
    "APZmediaPrimitiveSelector": APZmediaPrimitiveSelector,
    "APZmediaSimplePrimitive": APZmediaSimplePrimitive,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CleanFileNameNode": "APZmedia Clean File Name Node",
    "APZmediaGenerateFilePath": "APZmedia Generate File Path",
    "APZmediaStandardFilenameBuilder": "APZmedia Standard Filename Builder",
    "APZmediaPrimitiveSelector": "APZmedia Primitive Selector",
    "APZmediaSimplePrimitive": "APZmedia Simple Primitive",
}
