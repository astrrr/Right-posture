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
    name = "Right Posture",
    version = "1.0",
    description = "Right Posture",
    author = "Yuul B. Alwright",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
)
# Type python setup.py build to build.exe
# Don't forget to delete PyQt5 on build/lib to reduce file size for 100+MB