"""
Maliang动画演示 - 简单的带动画界面demo

这个demo展示了maliang库的动画功能，包括：
1. 移动动画（MoveWidget）
2. 按钮点击动画效果
3. 进度条动画
4. 动画控制开关
"""

import maliang
from maliang.animation import animations, controllers


def main():
    # 创建主窗口
    root = maliang.Tk(
        size=(800, 600),
        position=None,  # 自动居中
        title="Maliang动画演示",
        icon=None
    )
    
    # 创建画布
    canvas = maliang.Canvas(
        master=root,
        expand="",  # 不扩展
        auto_zoom=False,
        keep_ratio=None,
        free_anchor=False,
        auto_update=None,
        zoom_all_items=False
    )
    canvas.place(x = 0, y = 0, width = 800, height = 600)
    
    # 创建标题文本
    title = maliang.Text(
        master=canvas,
        position=(400, 50),
        size=None,
        text="Maliang动画演示",
        family=None,
        fontsize=24,
        weight='bold',
        slant='roman',
        underline=False,
        overstrike=False,
        justify='center',
        wrap_length=None,
        anchor='center',
        capture_events=None,
        gradient_animation=None,
        auto_update=None,
        style=None
    )
    
    # 创建移动的按钮
    moving_button = maliang.Button(
        master=canvas,
        position=(100, 150),
        size=(150, 50),
        text="移动按钮",
        family=None,
        fontsize=14,
        weight='normal',
        slant='roman',
        underline=False,
        overstrike=False,
        justify='center',
        command=lambda: print("移动按钮被点击了！"),
        image=None,
        anchor='center',
        capture_events=None,
        gradient_animation=None,
        auto_update=None,
        style=None
    )
    
    # 创建移动动画（左右移动）
    move_animation = animations.MoveWidget(
        widget=moving_button,
        offset=(100, 0),  # 向右移动500像素
        duration=500,  # 3秒
        controller=controllers.linear,  # 线性动画
        end=None,
        fps=60,
        repeat=0,  # 无限重复
        repeat_delay=0
    )
    
    # 创建第二个按钮（有弹跳效果）
    bounce_button = maliang.Button(
        master=canvas,
        position=(100, 250),
        size=(150, 50),
        text="弹跳按钮",
        family=None,
        fontsize=14,
        weight='normal',
        slant='roman',
        underline=False,
        overstrike=False,
        justify='center',
        command=lambda: start_bounce_animation(),
        image=None,
        anchor='center',
        capture_events=None,
        gradient_animation=None,
        auto_update=None,
        style=None
    )
    
    # 弹跳动画
    bounce_animation = None
    
    def start_bounce_animation():
        nonlocal bounce_animation
        if bounce_animation and bounce_animation.active:
            bounce_animation.stop()
        
        # 创建上下弹跳动画
        bounce_animation = animations.MoveWidget(
            widget=bounce_button,
            offset=(0, 100),  # 向下移动100像素
            duration=500,  # 0.5秒
            controller=controllers.rebound,  # 反弹效果
            end=lambda: return_bounce_animation(),
            fps=60,
            repeat=0,
            repeat_delay=0
        )
        bounce_animation.start()
    
    def return_bounce_animation():
        # 返回原位的动画
        return_animation = animations.MoveWidget(
            widget=bounce_button,
            offset=(0, -100),  # 向上移动100像素
            duration=500,  # 0.5秒
            controller=controllers.rebound,  # 反弹效果
            end=None,
            fps=60,
            repeat=0,
            repeat_delay=0
        )
        return_animation.start()
    
    # 创建进度条
    progress_bar = maliang.ProgressBar(
        master=canvas,
        position=(300, 400),
        size=(200, 30),
        default=0.0,  # 初始进度为0
        command=lambda value: print(f"进度: {value:.2f}"),
        image=None,
        anchor='center',
        capture_events=None,
        gradient_animation=None,
        auto_update=None,
        style=None
    )
    
    # 创建进度条动画
    progress_value = 0.0
    progress_direction = 1  # 1表示增加，-1表示减少
    
    def update_progress():
        nonlocal progress_value, progress_direction
        progress_value += 0.01 * progress_direction
        
        # 反转方向当到达边界
        if progress_value >= 1.0:
            progress_value = 1.0
            progress_direction = -1
        elif progress_value <= 0.0:
            progress_value = 0.0
            progress_direction = 1
        
        progress_bar.set(progress_value, callback=False)
        # 每100ms更新一次
        canvas.after(100, update_progress)
    
    # 创建控制开关
    switch = maliang.Switch(
        master=canvas,
        position=(400, 500),
        length=60,
        default=True,  # 默认开启
        command=lambda state: toggle_animations(state),
        image=None,
        anchor='center',
        capture_events=None,
        gradient_animation=None,
        auto_update=None,
        style=None
    )
    
    # 创建开关标签
    switch_label = maliang.Text(
        master=canvas,
        position=(400, 470),
        size=None,
        text="动画开关",
        family=None,
        fontsize=14,
        weight='normal',
        slant='roman',
        underline=False,
        overstrike=False,
        justify='center',
        wrap_length=None,
        anchor='center',
        capture_events=None,
        gradient_animation=None,
        auto_update=None,
        style=None
    )
    
    # 动画状态
    animations_active = True
    
    def toggle_animations(state):
        nonlocal animations_active
        animations_active = state
        if state:
            print("动画已开启")
            move_animation.start()
            canvas.after(100, update_progress)
        else:
            print("动画已暂停")
            move_animation.stop()
    
    # 创建说明文本
    instructions = maliang.Text(
        master=canvas,
        position=(400, 550),
        size=None,
        text="点击'弹跳按钮'查看弹跳效果，开关控制移动和进度条动画",
        family=None,
        fontsize=12,
        weight='normal',
        slant='roman',
        underline=False,
        overstrike=False,
        justify='center',
        wrap_length=400,
        anchor='center',
        capture_events=None,
        gradient_animation=None,
        auto_update=None,
        style=None
    )
    
    # 启动动画
    move_animation.start()
    canvas.after(100, update_progress)
    
    # 运行主循环
    root.mainloop()


if __name__ == "__main__":
    main()