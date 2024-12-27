from setuptools import setup

setup(
    name="mediatheory",
    version="0.1.0",
    packages=["mediatheory"],
    entry_points={
        "console_scripts": [
            "concat=mediatheory.entrypoints.concat:main",
            "gblur=mediatheory.entrypoints.gblur:main",
            "gif=mediatheory.entrypoints.gif:main",
            "invert=mediatheory.entrypoints.invert:main",
            "reverse=mediatheory.entrypoints.reverse:main",
            "runway=mediatheory.entrypoints.runway:main",
            "stitch=mediatheory.entrypoints.stitch:main",
            "system-installer=mediatheory.system.main:main",
        ]
    },
)
