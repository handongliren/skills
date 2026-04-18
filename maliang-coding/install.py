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
        "4. WindSurf\n" \
        "5. Bloop\n" \
        "6. Sourcegraph Cody\n" \
        "7. Codeium\n" \
        "8. Tabnine\n" \
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
            # WindSurf: ~/.windsurf/plugins
            target = base_dir.home() / ".windsurf" / "plugins" / "maliang-coding"
            install()
        case "5":
            # Bloop: ~/.bloop/skills
            target = base_dir.home() / ".bloop" / "skills" / "maliang-coding"
            install()
        case "6":
            # Sourcegraph Cody: ~/.cody/skills
            target = base_dir.home() / ".cody" / "skills" / "maliang-coding"
            install()
        case "7":
            # Codeium: ~/.codeium/skills
            target = base_dir.home() / ".codeium" / "skills" / "maliang-coding"
            install()
        case "8":
            # Tabnine: ~/.tabnine/skills
            target = base_dir.home() / ".tabnine" / "skills" / "maliang-coding"
            install()
    print()
