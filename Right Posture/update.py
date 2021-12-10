import glob
import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico', 'themes/', 'bin/']

mplBackendsPath = os.path.join(os.path.split(sys.executable)[0], "Lib/site-packages/*")

fileList = glob.glob(mplBackendsPath)

moduleList = ["PyQt5", "tensorflow", "PySide6", "tensorboard",
              "pandas", "numpy", "tensorflow_estimator"]

for mod in fileList:
    modules = os.path.splitext(os.path.basename(mod))[0]
    if not modules == "win32_setctime.py":
        moduleList.append(modules)

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
    options={"build_exe": {"packages": ["win32_setctime.py"], 'include_files': files, "excludes": ["PyQt5"] + moduleList}},
    executables=[target]
)
# Type python setup.py build to build.exe.
# If you know what lib is needless in the build file pls add that lib in excludes section.