# Draw GIF

A simple Python tool that combines multiple images into an animated GIF, using [Pillow](https://python-pillow.org/) for image handling and [imageio](https://imageio.readthedocs.io/) for GIF creation.

## Features

- Combines any number of images into a single animated GIF
- Automatically resizes all frames to a consistent size
- Converts images to RGB for compatibility
- Configurable frame duration and loop behavior

## Requirements

- Python 3.7+
- Pillow
- imageio

Install dependencies:

```bash
pip install pillow imageio
```

## Usage

Place your image files in the project folder, then update the `filenames` list in the script:

```python
filenames = ['happy.png', 'sad.png']
```

Run the script:

```bash
python draw_gif.py
```

This produces a `team.gif` file in the same directory, cycling through the given images.

## How it works

1. Each image is opened, converted to RGB, and resized to 500x500 pixels so all frames match.
2. The resized frames are collected into a list.
3. `imageio.v3.imwrite` stitches the frames into an animated GIF, with each frame displayed for the given `duration` (in milliseconds) and looping indefinitely (`loop=0`).

## Example

| Input | Input | Output |
|-------|-------|--------|
| happy.png | sad.png | team.gif (animated) |

## Possible improvements

- Accept image filenames via command-line arguments
- Support a folder of images instead of a hardcoded list
- Preserve original aspect ratio instead of forcing a fixed size
- Add a `requirements.txt` for easier setup

## License

MIT
