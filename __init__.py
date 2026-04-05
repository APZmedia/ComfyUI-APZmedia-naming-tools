from .nodes.APZnamefromtext import CleanFileNameNode
from .nodes.APZgeneratePathNode import GenerateFilePathNode
from .nodes.APZfileNameBuilder import APZmediaStandardFilenameBuilder
from .nodes.APZreadWidget import APZmediaReadWidget
from .nodes.APZloadImageWithFilename import APZmediaLoadImageWithFilename
from .nodes.APZdictionaryReplace import APZmediaDictionaryReplace
from .nodes.APZtextToHash import APZmediaTextToHash
from .nodes.APZvfxFilename import APZmediaVFXFilename
from .nodes.APZadFilename import APZmediaAdFilename
from .nodes.APZfashionEditorialFilename import APZmediaFashionEditorialFilename
from .nodes.APZfashionEcomFilename import APZmediaFashionEcomFilename
from .nodes.APZecomFilename import APZmediaEcomFilename

NODE_CLASS_MAPPINGS = {
    "CleanFileNameNode": CleanFileNameNode,
    "APZmediaGenerateFilePath": GenerateFilePathNode,
    "APZmediaStandardFilenameBuilder": APZmediaStandardFilenameBuilder,
    "APZmediaReadWidget": APZmediaReadWidget,
    "APZmediaLoadImageWithFilename": APZmediaLoadImageWithFilename,
    "APZmediaDictionaryReplace": APZmediaDictionaryReplace,
    "APZmediaTextToHash": APZmediaTextToHash,
    "APZmediaVFXFilename": APZmediaVFXFilename,
    "APZmediaAdFilename": APZmediaAdFilename,
    "APZmediaFashionEditorialFilename": APZmediaFashionEditorialFilename,
    "APZmediaFashionEcomFilename": APZmediaFashionEcomFilename,
    "APZmediaEcomFilename": APZmediaEcomFilename,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CleanFileNameNode": "APZmedia Clean File Name Node",
    "APZmediaGenerateFilePath": "APZmedia Generate File Path",
    "APZmediaStandardFilenameBuilder": "APZmedia Standard Filename Builder",
    "APZmediaReadWidget": "Read Widget",
    "APZmediaLoadImageWithFilename": "APZmedia Load Image with Filename",
    "APZmediaDictionaryReplace": "APZmedia Dictionary Based String Replacement",
    "APZmediaTextToHash": "APZmedia Text To Hash",
    "APZmediaVFXFilename": "APZmedia VFX Filename",
    "APZmediaAdFilename": "APZmedia Ad Filename",
    "APZmediaFashionEditorialFilename": "APZmedia Fashion Editorial Filename",
    "APZmediaFashionEcomFilename": "APZmedia Fashion E-com Filename",
    "APZmediaEcomFilename": "APZmedia E-com Filename",
}
