from setuptools import setup, find_packages

setup(
    name="comfyui-apzmedia-naming-tools",
    version="1.6.5",  # Updated version to match pyproject.toml
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'unidecode',
    ],
    entry_points={
        'comfyui.nodes': [
            'clean_file_name_node = nodes.APZnamefromtext:CleanFileNameNode',
            'generate_file_path_node = nodes.APZgeneratePathNode:GenerateFilePathNode',  # Corrected this line
            'standard_name_node = nodes.APZfileNameBuilder:APZmediaStandardFilenameBuilder',
            'primitive_selector_node = nodes.APZprimitiveSelector:APZmediaPrimitiveSelector',
            'simple_primitive_node = nodes.APZsimplePrimitive:APZmediaSimplePrimitive'
        ],
    },
    author="Pablo Apiolazza",
    author_email="info@apzmedia.com",
    description="A comprehensive set of naming tools for ComfyUI to build, sanitize, and manage file names and paths.",
    url="https://github.com/apzmedia/ComfyUI-APZmedia-cleanName-from-string",
    python_requires='>=3.6',
)
