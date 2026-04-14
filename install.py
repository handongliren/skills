import pathlib
import shutil

base_dir = pathlib.Path(__file__).parent.resolve()

shutil.copytree(
    base_dir / "maliang-coding", 
    base_dir.home() / ".agents" / "skills" / "maliang-coding", 
    dirs_exist_ok = True 
)