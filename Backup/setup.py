import sys
import os
from cx_Freeze import setup, Executable

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name="Right Posture",
    version="1.0",
    description="Right Posture",
    author="Yuul B. Alwright",
    executables=[target]
)

options = {
    'build_exe': {
        'build_exe': './/build'
    }
}
# Type python setup.py build to build.exe