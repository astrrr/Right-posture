import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico', 'themes/', 'bin/']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name="Right Posture",
    version="1.1.0",
    description="Right Posture",
    author="Right Posture TEAM",
    options={"build_exe": {"packages": ["keras"], 'include_files': files, "excludes": ["PyQt5"]}},
    executables=[target]
)
# Type python setup.py build to build.exe.
# If you know what lib is needless in the build file pls add that lib in excludes section.