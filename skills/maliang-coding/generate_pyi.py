import pathlib
import sys

import pyi

def generate() -> None:
    """
    生成所有正确的.pyi文件。
    """
    
    print("正在生成.pyi文件……", end = "")
    base_dir = pathlib.Path(__file__).parent.resolve()
    package_dir = pathlib.Path(sys.executable).parent / "Lib" / "site-packages" / "maliang"
    output_dir = base_dir / "references/pyi"
    pyi.generatePyiByDir(package_dir, output_dir)
    print("完成")

if __name__ == "__main__":
    generate()