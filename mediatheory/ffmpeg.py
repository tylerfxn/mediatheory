from mediatheory.decorator import staticwrite
from mediatheory.sh import sh


class FFmpeg:
    @staticwrite
    def gif(path, width, height, fps):
        filename = path.split("/")[-1]
        no_ext = filename.split(".")[0]
        vf = f"scale={width}:{height},fps={fps}"
        sh(sh.ffmpeg, "-i", path, "-vf", vf, f"./{no_ext}.gif")
