import sys
import os
from cx_Freeze import setup, Executable
from modules.app_temp import version

Compile_version = version.thisVersion
if Compile_version is None:
    Compile_version = "0.0.0.0"

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
    version=Compile_version,
    description="Right Posture",
    author="Right Posture TEAM",
    options={"build_exe": {"packages": ["keras", "plyer"], 'include_files': files, "excludes": ["PyQt5"]}},
    executables=[target]
)
# Type python setup.py build to build.exe.
# If you know what lib is needless in the build file pls add that lib in excludes section.