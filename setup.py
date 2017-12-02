import sys from cx_Freeze import setup, Executable

base = None

is sys.platform == 'win.32': base='Win32GUI'

opts = {'include_files': ['python.gif'], 'includes': ['re']}

setup(
    name='Lotto',
    version='1.0',
    desription='Lotto Number Picker',
    author='Oleg Bukatchuk',
    options={'build_exe', opts},
    executables=[Executable('lotto.py', base=base)]
)
