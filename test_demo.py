"""
测试maliang demo的基本功能
"""

import maliang
from maliang.animation import animations, controllers

print("测试maliang导入...")
print(f"Maliang版本: {maliang.__version__ if hasattr(maliang, '__version__') else 'unknown'}")
print(f"动画模块: {animations}")
print(f"控制器模块: {controllers}")

# 测试基本容器创建
print("\n测试容器创建...")
try:
    root = maliang.Tk(
        size=(400, 300),
        position=None,
        title="测试窗口",
        icon=None
    )
    print("✓ Tk窗口创建成功")
    
    canvas = maliang.Canvas(
        master=root,
        expand="",
        auto_zoom=False,
        keep_ratio=None,
        free_anchor=False,
        auto_update=None,
        zoom_all_items=False
    )
    print("✓ Canvas创建成功")
    
    # 测试widget创建
    button = maliang.Button(
        master=canvas,
        position=(100, 100),
        size=(100, 40),
        text="测试按钮",
        family=None,
        fontsize=12,
        weight='normal',
        slant='roman',
        underline=False,
        overstrike=False,
        justify='center',
        command=lambda: print("按钮点击"),
        image=None,
        anchor='center',
        capture_events=None,
        gradient_animation=None,
        auto_update=None,
        style=None
    )
    print("✓ Button创建成功")
    
    # 测试动画创建
    move_anim = animations.MoveWidget(
        widget=button,
        offset=(100, 0),
        duration=1000,
        controller=controllers.linear,
        end=None,
        fps=60,
        repeat=0,
        repeat_delay=0
    )
    print("✓ MoveWidget动画创建成功")
    
    # 测试控制器函数
    print(f"\n测试控制器函数:")
    print(f"  linear(0.5) = {controllers.linear(0.5)}")
    print(f"  smooth(0.5) = {controllers.smooth(0.5)}")
    print(f"  rebound(0.5) = {controllers.rebound(0.5)}")
    print(f"  ease_in(0.5) = {controllers.ease_in(0.5)}")
    print(f"  ease_out(0.5) = {controllers.ease_out(0.5)}")
    
    print("\n所有测试通过！")
    print("注意：这是一个非GUI测试，窗口不会显示。")
    
    # 清理
    root.destroy()
    
except Exception as e:
    print(f"✗ 测试失败: {e}")
    import traceback
    traceback.print_exc()