# APZmedia Naming Tools

## Overview

Because apparently "untitled_final_FINAL_v3_USE_THIS_ONE.png" is not a valid pipeline strategy.

This is a set of ComfyUI nodes designed to help you name files like a professional instead of like someone who just tabs out of a Finder window and hopes for the best. Built for VFX pipelines, but useful for anyone who has ever lost a render because the filename had a space in it.

---

## Nodes

### 1. APZmedia Clean File Name Node
Takes whatever chaos you typed and turns it into something a filesystem will tolerate without passive-aggressively throwing an error at 3am.

- Replaces spaces and invalid characters with something sensible
- Strips accents, because as beautiful as "Ñoño" is, your NAS does not speak Spanish
- Enforces a character limit so you don't generate paths longer than the Lord of the Rings extended edition
- Adds a prefix if you're into that sort of thing

### 2. APZmedia Generate File Path
Builds a proper VFX folder path from its components, because `root/project/episode/shot/pass` doesn't assemble itself. (It doesn't. We checked.)

- Toggle each path component on or off
- Uses the correct OS path separator automatically, so it works on both Mac and Windows, which is more than can be said for most things

### 3. APZmedia Standard Filename Builder
Concatenates project, episode, shot, and pass names into a standardised filename. Like a filename assembly line, but without the union disputes.

- Toggle any segment on or off
- Custom delimiter support — hyphen, underscore, pipe, interpretive dance character, your call

### 4. APZmedia Read Widget
Takes a string. Outputs a string. Connects things together so you don't have to hardcode values like it's 2003.

It's humble. It does its job. It doesn't complain. We should all aspire to be more like the Read Widget.

### 5. APZmedia Image Filename
Extracts the original filename from a Load Image node, because "ComfyUI_00247_.png" tells you absolutely nothing about what you were doing when you made it.

- Returns full filename and filename without extension
- Gracefully handles cases where the filename is missing (returns "unknown", not a stack trace — you're welcome)

### 6. APZmedia Dictionary Based String Replacement
Finds and replaces strings based on a dictionary you define, line by line. Because search-and-replace is a solved problem, and yet here we all are, doing it manually like fools.

**Dictionary format:**
```
"old thing" | "new thing"
"client name" | "the client who shall not be named"
"final" | "v1"
```

Each line is one replacement rule. Quotes are required. The pipe is the separator. Any line that doesn't follow the format is silently ignored, much like your feedback in that last meeting.

- Accepts any input type and converts it to string
- Outputs the replaced text and a count of how many replacements were made, so you can feel appropriately satisfied

### 7. APZmedia Text To Hash
Converts any text or number into a short, deterministic hash string. Useful for generating unique IDs from prompts, stamping filenames, or just making your workflow look more intimidating to non-technical stakeholders.

- SHA-256 under the hood — serious cryptographic infrastructure for the extremely mundane task of naming a file
- Configurable output length: 1 to 64 characters
- Same input always produces the same hash. That's the whole point. That's what deterministic means.

---

## Installation

1. Clone this repo into your ComfyUI `custom_nodes` directory
2. Run `pip install -e .`
3. Restart ComfyUI
4. Find all nodes under the **APZmedia** category in the node menu

---

## Dependencies

- `unidecode` — for stripping accents from characters that are perfectly valid in human language but make filesystems cry
- `ComfyUI` — you presumably already have this

---

## License

MIT — do what you want, just don't blame us.

## Author

**Pablo Apiolazza** — [APZmedia](https://github.com/APZmedia)

## Support

Issues, feature requests, and existential questions about file naming conventions: [GitHub repository](https://github.com/APZmedia/ComfyUI-APZmedia-naming-tools)
