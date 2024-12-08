import os

from mediatheory.decorator import staticwrite

MEDIA_INPUT = "./media/in"
MEDIA_OUTPUT = "./media/out"

class Directory:
    @staticwrite
    def setup_dirs():
        os.makedirs(MEDIA_INPUT, exist_ok=True)
        os.makedirs(MEDIA_OUTPUT, exist_ok=True)
