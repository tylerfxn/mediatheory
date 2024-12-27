import platform
from subprocess import CalledProcessError

from mediatheory.log import logging
from mediatheory.sh import sh


def install():
    if platform.system() == "Darwin":
        logging.info("Installing ffmpeg - this may take a while...")
        logging.info("Output will be delayed but installation is in progress")
        sh(sh.brew, "install", "ffmpeg")
    else:
        logging.error("Unknown platform")


def find():
    try:
        sh(sh.which, "ffmpeg")
        return True
    except CalledProcessError:
        return False


if __name__ == "__main__":
    install()
