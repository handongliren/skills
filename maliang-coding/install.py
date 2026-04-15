import pathlib
import shutil
import os
import sys

base_dir = pathlib.Path(__file__).parent.resolve()

os.system('call "' + sys.executable + '" "' + str(base_dir / "generate_pyi.py") + '"')
shutil.copytree(
    base_dir, 
    base_dir.home() / ".agents" / "skills" / "maliang-coding", 
    dirs_exist_ok = True 
)