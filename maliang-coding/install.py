import pathlib
import shutil
import generate_pyi

base_dir = pathlib.Path(__file__).parent.resolve()

generate_pyi.generate()
shutil.copytree(
    base_dir, 
    base_dir.home() / ".agents" / "skills" / "maliang-coding", 
    dirs_exist_ok = True 
)