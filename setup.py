from distutils.core import setup
import py2exe

options = {
    "py2exe": {
        "dll_excludes": ["MSVCP90.dll"],
        "compressed": 1,
        "optimize": 2,
        "ascii": 0,
        "bundle_files": 1
    }
}
setup(console=['ytDownloader.py'],
      options=options,
      zipfile=None)