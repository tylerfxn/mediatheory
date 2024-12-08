from setuptools import setup

setup(
    name="mediatheory",
    version="0.1.0",
    packages=["mediatheory"],
    entry_points={
        "console_scripts": [
            "mediatheory-system-installer=mediatheory.system.main:main",
            "gif=mediatheory.entrypoints.gif:main",
            "runway=mediatheory.entrypoints.runway:main",
        ]
    }
)
