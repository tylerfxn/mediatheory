from mediatheory.system.dir import Directory
from mediatheory.system.ffmpeg import install as install_ffmpeg


def install_all():
    install_ffmpeg()


def main():
    Directory.setup_dirs()
    install_all()
