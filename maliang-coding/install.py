import pathlib
import shutil
import generate_pyi

base_dir = pathlib.Path(__file__).parent.resolve()

def install() -> None:
    generate_pyi.generate()
    print(f"正在复制skill文件夹到<{target}>……", end = "")
    shutil.copytree(
        base_dir, 
        target, 
        dirs_exist_ok = True 
    )
    print("完成")

while True:
    choice = input(
        "简易skill安装程序 Copyright © 寒冬利刃 2026.\n" \
        "将该插件安装至？\n" \
        "0. 退出\n" \
        "1. Claude Code\n" \
        "2. Cline\n" \
        f"<{base_dir}>\n" \
        "$ "
    )
    match choice:
        case "0":
            exit()
        case "1":
            target = base_dir.home() / ".claude" / "skills" / "maliang-coding"
            install()
        case "2":
            target = base_dir.home() / ".agents" / "skills" / "maliang-coding"
            install()
    print()
