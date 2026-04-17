import pathlib
import sys

import pyi

def generate() -> None:
    """
    生成所有正确的.pyi文件。
    
    :return: 无返回值
    :rtype: None
    """
    
    base_dir = pathlib.Path(__file__).parent.resolve()
    package_dir = pathlib.Path(sys.executable).parent / "Lib" / "site-packages" / "maliang"
    output_dir = base_dir / "references/pyi"
    pyi.generatePyiByDir(package_dir, output_dir)

if __name__ == "__main__":
    generate()