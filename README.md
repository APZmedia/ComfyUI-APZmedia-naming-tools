# APZmedia Naming Tools

## Overview
This package provides a comprehensive set of naming tools for ComfyUI that streamline text processing for VFX file naming, file path generation, and primitive value selection. The tools include the **Clean File Name Node**, **Generate File Path Node**, **APZmedia Standard Filename Builder**, and **Primitive Selector Nodes**, all designed to fit common conventions in VFX pipelines. These tools help sanitize text, create valid filenames, generate file paths, and provide primitive values for tagging and other operations.

## Features

### 1. **APZmedia Clean File Name Node**
- **Text Sanitization**: Removes invalid characters and replaces them with specified characters
- **Accent Handling**: Converts accented characters to their unaccented equivalents
- **Character Limit Control**: Truncates text to specified maximum length
- **Prefix Support**: Adds user-defined prefix to cleaned text
- **Customizable Replacement**: Specifies character to replace invalid characters

### 2. **APZmedia Generate File Path**
- **VFX Folder Structure**: Dynamically generates file paths based on project components
- **Toggle Components**: Each component can be included or excluded for flexible path generation
- **OS-Compatible Paths**: Automatically uses correct file path separators for the operating system
- **Flexible Structure**: Build paths like `/root/project/episode/shot/pass` based on your needs

### 3. **APZmedia Standard Filename Builder**
- **Customizable Segments**: Concatenate project, episode, shot, and pass names
- **Flexible Inclusion**: Toggle segments on/off to include only relevant components
- **Delimiter Control**: Specify custom delimiters (hyphen, underscore, etc.)
- **Standardized Naming**: Maintain consistent file naming across projects

### 4. **APZmedia Primitive**
- **Multiple Types**: Text, Number, and Date outputs
- **Date Formatting**: Multiple date formats (YYYY-MM-DD, MM-DD-YYYY, DD-MM-YYYY, YYYYMMDD)
- **Simple Interface**: Single node for all primitive value types
- **String Output**: All values output as strings for easy use in filenames

## Input and Output Types

### **APZmedia Clean File Name Node**
- **Input Types**:
  - `input_text` (STRING): The text to be cleaned
  - `replacement_char` (STRING): Character to replace invalid characters (default: `-`)
  - `invalid_chars` (STRING): Characters to be removed (default: ` #%&{}\\<>*?/ $!'\":@+`|=.`)
  - `prefix` (STRING): Prefix to prepend to the filename
  - `char_limit` (INT): Maximum length of the output string (default: 255)
  
- **Output Types**:
  - `cleaned_text` (STRING): The sanitized and truncated text string

### **APZmedia Generate File Path**
- **Input Types**:
  - `root_folder` (STRING): The root directory for the project (e.g., `/mnt/projects`)
  - `project_name` (STRING): The name of the VFX project or show (e.g., `Starwars`)
  - `episode_name` (STRING): The episode or sequence name (optional)
  - `shot_name` (STRING): The shot number or identifier (e.g., `0010`)
  - `pass_name` (STRING): The type of pass (e.g., compositing, animation)
  - `toggle_root_folder` (INCLUDE/EXCLUDE): Whether to include the root folder
  - `toggle_project_name` (INCLUDE/EXCLUDE): Whether to include the project name
  - `toggle_episode_name` (INCLUDE/EXCLUDE): Whether to include the episode name
  - `toggle_shot_name` (INCLUDE/EXCLUDE): Whether to include the shot name
  - `toggle_pass_name` (INCLUDE/EXCLUDE): Whether to include the pass type
  
- **Output Types**:
  - `generated_path` (STRING): The generated file path with correct OS separators

### **APZmedia Standard Filename Builder**
- **Input Types**:
  - `project_name` (STRING): The project or show name (optional)
  - `episode_name` (STRING): The episode or sequence name (optional)
  - `shot_name` (STRING): The shot number or identifier (e.g., `0010`)
  - `pass_name` (STRING): The type of pass (e.g., compositing, animation)
  - `delimiter` (STRING): The character to separate segments (default: `-`)
  - `toggle_project_name` (INCLUDE/EXCLUDE): Whether to include project name
  - `toggle_episode_name` (INCLUDE/EXCLUDE): Whether to include episode name
  - `toggle_shot_name` (INCLUDE/EXCLUDE): Whether to include shot name
  - `toggle_pass_name` (INCLUDE/EXCLUDE): Whether to include pass name
  
- **Output Types**:
  - `concatenated_name` (STRING): The concatenated filename with selected delimiter

### **APZmedia Primitive**
- **Input Types**:
  - `combo` (TEXT/NUMBER/DATE): Type of value to output (dropdown selection)
  - `text` (STRING): Text input for text type
  - `number` (INT): Number input (1-9999) for number type
  - `date_format` (YYYY-MM-DD/MM-DD-YYYY/DD-MM-YYYY/YYYYMMDD): Date format for date type
  
- **Output Types**:
  - `value` (STRING): The selected value as a string

## How They Work

### **APZmedia Clean File Name Node**
1. **Accent Conversion**: Converts accented characters to unaccented equivalents
2. **Space Replacement**: Replaces spaces with the specified replacement character
3. **Invalid Character Removal**: Removes characters defined in `invalid_chars`
4. **Consecutive Character Cleanup**: Removes duplicate replacement characters
5. **Prefix Addition**: Adds the user-defined prefix
6. **Length Truncation**: Ensures the final text doesn't exceed the character limit

### **APZmedia Generate File Path**
1. **Component Selection**: Evaluates which components should be included based on toggles
2. **Path Assembly**: Builds the path by concatenating selected components
3. **OS Path Joining**: Uses `os.path.join()` for correct path separators
4. **Output Generation**: Returns the complete file path

### **APZmedia Standard Filename Builder**
1. **Segment Evaluation**: Checks which segments should be included based on toggles
2. **Name Assembly**: Collects all enabled segments into a list
3. **Delimiter Application**: Joins segments using the specified delimiter
4. **Output Generation**: Returns the concatenated filename

### **APZmedia Primitive**
1. **Type Selection**: Determines the output based on the selected type
2. **Value Processing**: Handles text, number, or date logic
3. **String Conversion**: Converts all values to strings for filename use

## Use Cases

### **Filename Tagging**
- Use **Primitive** for date stamps: `2024-01-15`
- Use **Primitive** for version numbers: `1`, `2`
- Use **Clean File Name** to sanitize user input
- Use **Standard Filename Builder** for structured naming

### **Path Generation**
- Use **Generate File Path** for VFX pipeline structures
- Combine with **Primitive** for dynamic path components

### **Workflow Integration**
- Chain multiple nodes for complex naming systems
- Use primitive outputs as inputs to filename builders
- Combine with ComfyUI's image generation for automatic file naming

## Installation

1. **Clone or download** this repository to your ComfyUI `custom_nodes` directory
2. **Install dependencies**: `pip install -e .`
3. **Restart ComfyUI** to load the new naming tools
4. **Find tools** in the "APZmedia" category in the node menu

## Dependencies

- `unidecode`: For accent character conversion
- `ComfyUI`: The main application

## License

MIT License - See LICENSE file for details.

## Author

**Pablo Apiolazza** - [APZmedia](https://github.com/APZmedia)

## Support

For issues, feature requests, or questions, please visit the [GitHub repository](https://github.com/APZmedia/ComfyUI-APZmedia-cleanName-from-string).
