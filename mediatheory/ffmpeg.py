import os
import uuid
from typing import Dict, List, Optional

from mediatheory.decorator import staticwrite
from mediatheory.sh import sh


class FFmpeg:
    @staticwrite
    def gif(path, width, height, fps):
        filename = path.split("/")[-1]
        no_ext = filename.split(".")[0]
        vf = f"scale={width}:{height},fps={fps}"
        sh(sh.ffmpeg, "-i", path, "-vf", vf, f"./{no_ext}.gif")

    @staticwrite
    def reverse(path: str):
        filename = path.split("/")[-1]
        no_ext, ext = filename.split(".")
        out = f"./{no_ext}-reverse.{ext}"
        sh(sh.ffmpeg, "-i", path, "-vf", "reverse", "-af", "reverse", out)

    @staticwrite
    def concat(
        input_files: List[str],
        output_file: str = None,
        reencode: bool = True,
        video_codec: str = "libx264",
        audio_codec: str = "aac",
        crf: int = 23,
        preset: str = "medium",
        extra_params: Optional[Dict[str, str]] = None
    ) -> None:
        """
        input_files: List of input video file paths
        output_file: Output video file path
        reencode: If True, re-encode videos instead of stream copy
        video_codec: Video codec to use when re-encoding
        audio_codec: Audio codec to use when re-encoding
        crf: Constant Rate Factor (0-51, lower is better quality)
        preset: x264 preset
            (ultrafast, superfast, veryfast, faster,
             fast, medium, slow, slower, veryslow)
        extra_params: Dictionary of additional ffmpeg parameters
        """
        # ffmpeg -f concat -safe 0 -i files.txt -c:v libx264 out.mp4
        tmp = "files.txt"

        try:
            with open(tmp, "w") as f:
                for file_path in input_files:
                    if not os.path.exists(file_path):
                        raise FileNotFoundError(f"File not found: {file_path}")
                    f.write(f"file '{file_path}'\n")

            cmd = [sh.ffmpeg, "-f", "concat", "-safe", "0", "-i", tmp]

            if reencode:
                cmd.extend([
                    "-c:v", video_codec,
                    "-c:a", audio_codec,
                    "-crf", str(crf),
                    "-preset", preset
                ])
            else:
                cmd.extend(["-c", "copy"])

            if extra_params:
                for key, value in extra_params.items():
                    cmd.extend([key, value])

            if not output_file:
                ext = input_files[0].split("/")[-1].split(".")[1]
                output_file = f"{uuid.uuid4()}.{ext}"

            sh(cmd, output_file)
        finally:
            if os.path.exists(tmp):
                os.remove(tmp)
