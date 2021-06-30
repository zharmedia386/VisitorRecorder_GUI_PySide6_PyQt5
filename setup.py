import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['logo.ico']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="logo.ico"
)

# SETUP CX FREEZE
setup(
    name = "BookstoreApp",
    version = "1.0",
    description = "Modern GUI for Python applications",
    author = "Zharmedia",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)