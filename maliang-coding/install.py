import pathlib
import shutil
import generate_pyi

base_dir = pathlib.Path(__file__).parent.resolve()

def install() -> None:
    generate_pyi.generate()
    # 确保目标目录的父目录存在
    target.parent.mkdir(parents=True, exist_ok=True)
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
        "3. Cursor\n" \
        "4. Qwen Code（通义千问）\n" \
        "5. 通义灵码（阿里）\n" \
        "6. DeepSeek Coder\n" \
        "7. 智谱清言（智谱AI）\n" \
        "8. 扣子（字节跳动）\n" \
        f"<{base_dir}>\n" \
        "$ "
    )
    match choice:
        case "0":
            exit()
        case "1":
            # Claude Code: ~/.claude/skills
            target = base_dir.home() / ".claude" / "skills" / "maliang-coding"
            install()
        case "2":
            # Cline: ~/.agents/skills
            target = base_dir.home() / ".agents" / "skills" / "maliang-coding"
            install()
        case "3":
            # Cursor: ~/.cursor/skills or ~/.cursor/plugins
            cursor_path = base_dir.home() / ".cursor"
            if (cursor_path / "skills").exists():
                target = cursor_path / "skills" / "maliang-coding"
            elif (cursor_path / "plugins").exists():
                target = cursor_path / "plugins" / "maliang-coding"
            else:
                target = cursor_path / "skills" / "maliang-coding"
            install()
        case "4":
            # Qwen Code（通义千问）: ~/.qwen-code/skills
            target = base_dir.home() / ".qwen-code" / "skills" / "maliang-coding"
            install()
        case "5":
            # 通义灵码（阿里）: ~/.lingma/skills（基于阿里云产品命名）
            target = base_dir.home() / ".lingma" / "skills" / "maliang-coding"
            install()
        case "6":
            # DeepSeek Coder: ~/.deepseek/skills
            target = base_dir.home() / ".deepseek" / "skills" / "maliang-coding"
            install()
        case "7":
            # 智谱清言（智谱AI）: ~/.zhipu/skills
            target = base_dir.home() / ".zhipu" / "skills" / "maliang-coding"
            install()
        case "8":
            # 扣子（字节跳动）: ~/.coze/skills
            target = base_dir.home() / ".coze" / "skills" / "maliang-coding"
            install()
    print()
