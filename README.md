# APZmedia Naming Tools

## Overview

Because apparently "untitled_final_FINAL_v3_USE_THIS_ONE.png" is not a valid pipeline strategy.

This is a set of ComfyUI nodes designed to help you name files like a professional instead of like someone who just tabs out of a Finder window and hopes for the best. Built for VFX pipelines but expanded to cover the naming conventions of advertising, fashion, and e-commerce — because every industry has independently invented its own way to almost get this right.

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/pabloapz)

---

## Nodes

### Utilities

#### APZmedia Clean File Name Node
Takes whatever chaos you typed and turns it into something a filesystem will tolerate without passive-aggressively throwing an error at 3am.

- Replaces spaces and invalid characters with something sensible
- Strips accents, because as beautiful as "Ñoño" is, your NAS does not speak Spanish
- Enforces a character limit so you don't generate paths longer than the Lord of the Rings extended edition
- Adds a prefix if you're into that sort of thing

#### APZmedia Generate File Path
Builds a folder path from components with full control over what goes in and how it gets separated.

- Toggle each component on or off
- Slash type selector: **Auto** (detects your OS), **Forward (/)**, or **Backslash (\\)** — for when you need to hand a path to something that has opinions
- Components: root folder, project, episode, shot, pass

#### APZmedia Standard Filename Builder
The original general-purpose filename assembler. Project, episode, shot, pass — toggle what you need, set your delimiter, get a string.

#### APZmedia Read Widget
Takes a string. Outputs a string. Connects things that would otherwise refuse to talk to each other.

It's humble. It does its job. It doesn't complain. We should all aspire to be more like the Read Widget.

#### APZmedia Load Image with Filename
A drop-in replacement for ComfyUI's built-in Load Image node that also tells you what the file is actually called. Because the standard node discards that information the moment it has what it wants, like a contractor who stops returning calls after the deposit clears.

- Same image picker and upload behaviour as the built-in Load Image
- Outputs `IMAGE` and `MASK` exactly as before — existing wires still work
- Also outputs `filename` and `filename_without_ext` as strings
- Works because it intercepts the path *before* the tensor is built, which is the only moment the filename still exists

#### APZmedia Dictionary Based String Replacement
Finds and replaces strings based on a dictionary you define, line by line. Because search-and-replace is a solved problem, and yet here we all are, doing it manually.

**Format:**
```
"old thing" | "new thing"
"client name" | "the client who shall not be named"
"final" | "v1"
```

- Accepts any input type, converts to string
- Outputs replaced text and a replacement count, so you know it actually did something

#### APZmedia Cycle Int
Outputs an integer that steps through a range every time the workflow runs. Set a min, a max, a step size, and a direction — it cycles forever, wrapping back around when it hits the end. Designed for batch automation so you don't have to manually change a number between runs like some kind of intern.

- Increment or decrement
- Configurable step size
- Wraps cleanly on both ends
- Resets to min (or max, if decrementing) when ComfyUI restarts — it's a session counter, not a life commitment
- Each node instance cycles independently — two Cycle Int nodes in the same workflow have separate counters
- First run outputs the starting value, then advances from there on every subsequent run
- If you change min/max mid-session and the current value falls outside the new range, it resets to the new starting point rather than doing something dramatic

#### APZmedia Text To Hash
Converts any text or number into a short, deterministic hash string. Useful for stamping filenames with a unique ID derived from prompt content, or for making your workflow look more serious than it is.

- SHA-256 under the hood
- Configurable output length: 1–64 characters
- Same input always produces the same output. That's what deterministic means.

#### APZmedia String Stripper
Extracts one or more segments from a filename string based on a naming pattern. Designed to pair with **APZmedia Load Image with Filename** — feed in the `filename_without_ext` output, define the pattern, get back the part you actually need.

If the input doesn't match the pattern, the node passes the original string through unchanged and sets `matched` to `False`, so the rest of your workflow doesn't silently break.

**Two modes, toggled per node:**

**Simple** — define the pattern using your actual delimiter. The node auto-detects the delimiter from the pattern, splits both pattern and input on it, maps slot names to values, and returns the ones you asked for.

```
pattern:        project-episode-shot-pass
input:          ACME-EP01-SH010-beauty
terms_to_keep:  episode,shot
output_delim:   -
→ result:       EP01-SH010   matched: True

# Segment count mismatch → passthrough
input:          ACME-EP01-beauty
→ result:       ACME-EP01-beauty   matched: False
```

**Regex** — supply a regex with capture groups, reference them by number (1-based) or by name if using named groups (`(?P<name>...)`).

```
pattern:        ^(.+?)-v(\d+)-(.+)$
terms_to_keep:  1,2
input:          hero_shot-v003-final
output_delim:   -
→ result:       hero_shot-v003   matched: True
```

- `output_delimiter` is independent of the source delimiter — you can extract with `-` and rejoin with `_`
- Multiple terms are joined in the order you list them
- Named capture groups work: `terms_to_keep: ver` with `(?P<ver>\d+)`
- Invalid regex or optional groups that didn't match → passthrough + `matched: False`

---

### Industry Naming Nodes

All naming nodes follow the same pattern: free text fields for every segment, a toggle per segment, and a delimiter you can change. Numbers, version codes, and padding are your responsibility — these nodes don't assume what format you want.

#### APZmedia VFX Filename
**Standard:** VFX / film pipeline conventions
**Fields:** `show` · `sequence` · `shot` · `pass` · `version`
**Example:** `MYSHOW_SQ010_SH0050_beauty_v003`

#### APZmedia Ad Filename
**Standard:** Digital advertising (Meta, Google, programmatic)
**Fields:** `brand` · `campaign` · `format` · `placement` · `ratio` · `version`
**Example:** `NIKE_SS24_VIDEO_FEED_9x16_v02`

The ratio field is free text because `9x16`, `9:16`, and `916` are all in active use simultaneously across platforms and nobody is going to fix that.

#### APZmedia Fashion Editorial Filename
**Standard:** Fashion lookbook / editorial photography
**Fields:** `season` · `collection` · `look` · `shot` · `version`
**Example:** `SS25_RTW_LOOK03_SHOT02_v01`

#### APZmedia Fashion E-com Filename
**Standard:** Fashion e-commerce product photography
**Fields:** `brand` · `sku` · `colorcode` · `view` · `sequence`
**Example:** `ACNE_AB1234_BLK_FRONT_01`

#### APZmedia E-com Filename
**Standard:** General e-commerce product photography
**Fields:** `brand` · `product` · `variant` · `view` · `sequence`
**Example:** `BRAND_PRODUCTNAME_RED-XL_FRONT_01`

---

## Installation

1. Clone this repo into your ComfyUI `custom_nodes` directory
2. Run `pip install -e .`
3. Restart ComfyUI
4. Find all nodes under the **APZmedia** category in the node menu — industry naming nodes are grouped under **APZmedia/Naming**

---

## Dependencies

- `unidecode` — for stripping accents from characters that are perfectly valid in human language but make filesystems cry
- `ComfyUI` — you presumably already have this

---

## License

MIT — do what you want, just don't blame us.

## Author

**Pablo Apiolazza** — [APZmedia](https://github.com/APZmedia)

## ☕ Support

If you find these nodes useful, consider buying me a coffee — it helps me keep building and maintaining free tools for the ComfyUI community.

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/pabloapz)

Issues, feature requests, and existential questions about file naming conventions: [GitHub repository](https://github.com/APZmedia/ComfyUI-APZmedia-naming-tools)
