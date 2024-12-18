# mediatheory

```
∫ technology ⊙ λ media ≊ ∆ art
```

## 💾 🎰 - media [re]mixing interface

`mediatheory` is an open source toolkit for producing art: dicing, slicing, chopping, and remixing media. It accomplishes this by:

- providing a hands-on command line and programmatic interface to media transformation
- integrating generative AI APIs across image and video, like [`runway`](https://docs.dev.runwayml.com/) / [`luma`](https://lumalabs.ai/luma-api/client-docs/index.html) / [`fal`](https://fal.ai/) / [`replicate`](https://replicate.com/) / [`flux`](https://blackforestlabs.ai/), and more.
- leveraging multimedia transformation softwares like
    - [`FFmpeg`](https://github.com/FFmpeg/FFmpeg) - process multimedia content such as audio, video, subtitles and related metadata.
    - [`ImageMagick`](https://github.com/ImageMagick/ImageMagick) - for editing and manipulating digital images.
    - [`SoX`](https://github.com/chirlu/sox) - Swiss Army knife of sound processing.
    - [`gstreamer`](https://github.com/GStreamer/gstreamer) - a library for constructing graphs of media-handling components. 
    - [`MLT Framework`](https://github.com/mltframework/mlt) - multimedia framework designed for video editing.
    - [`OpenCV`](https://github.com/opencv/opencv) - a library of programming functions mainly for real-time computer vision.
    - and more.

## Demos

<p align-"center>
    <img src="./img/42833715.gif" width=49%>
    <img src="./img/02ba1cc4.gif" width=49%>
</p>
<p align-"center>
    <img src="./img/83eefe8c.gif" width=49%>
    <img src="./img/e3db4834.gif" width=49%>
</p>

<!-- ![](./img/42833715.gif) -->
<!-- ![](./img/02ba1cc4.gif) -->
<!-- ![](./img/83eefe8c.gif) -->

## Examples

Convert a video into a gif
```
gif video.mp4
```

Execute Runway's image-to-video API
```
runway image.jpg
runway image.jpg --prompt "camera dolly in"
```

## Setup

```
python3 -m venv venv
source venv/bin/activate
pip install poetry
poetry install
```

## Environment basics

```
# Add dependencies
poetry add requests  # for production
poetry add pytest --dev  # for development

# Run commands in virtual environment
poetry run python script.py
poetry run pytest

# Activate virtual environment
poetry shell

# Build package
poetry build

# Update dependencies
poetry update
```

## Contribution / Development 

**Install pre-commit format hooks**

```
poetry run pre-commit install
```


## Important Reading

*Media are all the interfaces between consciousness and reality, transforming both the message and the messenger. Media are any extension of human capability that shapes how we perceive, process, and project our world.*

*Media is the substrate through which human intention becomes sensory experience, encompassing all technologies that extend our ability to create, communicate, and comprehend.*

*Media is everything and everything is media.*

#### VISUAL

- Images / Photographs / Paintings / Drawings
- Charts / Diagrams / Graphs / Maps
- Logos / Icons / Symbols / Glyphs / Pictograms / Unicode

#### TEMPORAL

- Video / Film / Animation / Motion Pictures
- Live streams / Real-time feeds / Performance recordings
- Temporal sculptures / Time-based installations / 

#### AUDIBLE

- Sound / Music / Voice / Speech
- Samples / Field recordings / Radio
- Synthesis / Soundwaves / MIDI

#### TEXTUAL

- Written word / Literature / Poetry
- Code / Scripts / Documentation
- Notation systems / Mathematics / Algorithms

#### PHYSICAL

- Architectures / Sculptures / Materials
- Electronics / Robotics / Mechanical systems
- Biological / Plants / Bacterial cultures 

#### CONCEPTUAL

- Mental models / knowledge structures
- Systems / Networks / Protocols
- Databases / Information architecture

#### CULTURAL

- Memetics / Mimetics / Cultural artifacts
- Fashion / Style / Behavioral patterns
- Social networks / Communication mechanisms

#### INTERACTIVE

- Softwares / Applications / Command lines
- Video games / Virtual reality / Augmented reality
- Interactive installations / Responsive environments

## Miscellaneous

December 2024: SOTA OSS text to video, image to video:
- https://github.com/Lightricks/LTX-Video
- https://fal.ai/models/fal-ai/ltx-video/image-to-video
- https://huggingface.co/Lightricks/LTX-Video
