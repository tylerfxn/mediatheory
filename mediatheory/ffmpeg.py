from mediatheory.decorator import staticwrite
from mediatheory.sh import sh


class FFmpeg:
    @staticwrite
    def gif(path):
        filename = path.split("/")[-1]
        no_ext = filename.split(".")[0]
        sh(sh.ffmpeg, "-i", path, f"./{no_ext}.gif")
