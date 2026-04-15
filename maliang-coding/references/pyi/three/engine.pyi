"""
Core codes of 3D
"""

from __future__ import annotations
import array
import math
import statistics
import tkinter
import typing
import typing_extensions
from maliang.core import configs, containers

class Canvas(containers.Canvas):
    """
    Base class of 3D Canvas
    """

    def __init__(self, master: containers.Tk | containers.Toplevel | containers.Canvas | None, expand: typing.Literal['', 'x', 'y', 'xy'], auto_zoom: bool, keep_ratio: typing.Literal['min', 'max'] | None, free_anchor: bool, **kwargs) -> None:
        ...
    @property
    def components(self) -> tuple[Component, ...]:
        """
        Return all `Component` of this Canvas
        """
    @property
    def geometries(self) -> tuple[Geometry, ...]:
        """
        Return all `Geometry` of this Canvas
        """
    def space_sort(self) -> None:
        """
        Sort the contextual relationship between the spatial positions of the components
        """

class Space(Canvas):
    """
    A canvas where you can view 3D objects
    """

    def __init__(self, master: containers.Tk | containers.Toplevel | containers.Canvas | None, expand: typing.Literal['', 'x', 'y', 'xy'], auto_zoom: bool, keep_ratio: typing.Literal['min', 'max'] | None, free_anchor: bool, **kwargs) -> None:
        ...

class Component:
    """
    3D 对象基类
    """

    def __init__(self, *coordinates):
        ...
    def translate(self, dx, dy, dz):
        """
        平移对象本身
        
                * `dx`: x 方向位移长度
                * `dy`: y 方向位移长度
                * `dz`: z 方向位移长度
        """
    @typing.overload
    def rotate(self, dx, dy, dz, center):
        ...
    @typing.overload
    def rotate(self, dx, axis):
        ...
    def rotate(self, dx, dy, dz, center, axis):
        """
        旋转对象本身
        
                * `dx`: x 方向逆时针旋转弧度，或者绕旋转轴线的旋转弧度
                * `dy`: y 方向逆时针旋转弧度
                * `dz`: z 方向逆时针旋转弧度
                * `center`: 旋转中心，默认为原点
                * `axis`: 旋转轴线，无默认值
        """
    def scale(self, kx, ky, kz, center):
        """
        缩放对象本身
        
                * `kx`: x 方向缩放比例
                * `ky`: y 方向缩放比例
                * `kz`: z 方向缩放比例
                * `center`: 缩放中心，默认为几何中心
        """
    def center(self):
        """
        几何中心
        """
    def update(self) -> None:
        """
        Update
        """

class Point(Component):
    """
    点
    """

    def __init__(self, canvas, coords, size, width, fill, outline, markuptext, markupdelta, markupfont, markupfill, markupjustify):
        """
        * `canvas`: 父画布
                * `coords`: 点的空间坐标
                * `size`: 点的大小
                * `width`: 点轮廓的宽度
                * `fill`: 点内部的填充颜色
                * `outline`: 点轮廓的颜色
                * `markuptext`: 标记文本
                * `markupdelta`: 标记文本显示位置的偏移量
                * `markupfont`: 标记文本字体
                * `markupfill`: 标记文本颜色
                * `markupjustify`: 标记文本多行对齐方式
        """
    def update(self):
        """
        更新对象的显示
        """

class Line(Component):
    """
    线
    """

    def __init__(self, canvas, point_start, point_end, width, fill):
        """
        * `canvas`: 父画布
                * `point_start`: 起点坐标
                * `point_end`: 终点坐标
                * `width`: 线的宽度
                * `fill`: 线的颜色
        """
    def update(self):
        """
        更新对象的显示
        """

class Plane(Component):
    """
    面
    """

    def __init__(self, canvas, *points, width, fill, outline):
        """
        * `canvas`: 父画布
                * `points`: 各点的空间坐标
                * `width`: 面轮廓的宽度
                * `fill`: 面内部的填充颜色
                * `outline`: 面轮廓的颜色
        """
    def update(self):
        """
        更新对象的显示
        """

class Text3D(Component):
    """
    三维文本
    """

    def __init__(self, canvas, coords, text, font, justify, fill):
        """
        * `canvas`: 父画布
                * `coords`: 点的空间坐标
                * `text`: 显示的文本
                * `size`: 点的大小
                * `font`: 点轮廓的宽度
                * `justify`: 多行文本对齐方式
                * `fill`: 点内部的填充颜色
        """
    def update(self):
        """
        更新对象的显示
        """

class Geometry:
    """
    几何体
    """

    def __init__(self, canvas, *sides):
        """
        * `canvas`: 父画布
                * `sides`: 组成几何体的面
        """
    def translate(self, dx, dy, dz):
        """
        平移几何体中的所有 3D 对象
        
                * `dx`: x 方向位移长度
                * `dy`: y 方向位移长度
                * `dz`: z 方向位移长度
        """
    @typing.overload
    def rotate(self, dx, dy, dz, center):
        ...
    @typing.overload
    def rotate(self, dx, axis):
        ...
    def rotate(self, dx, dy, dz, center, axis):
        """
        旋转几何体中的所有 3D 对象
        
                * `dx`: x 方向逆时针旋转弧度，或者绕旋转轴线的旋转弧度
                * `dy`: y 方向逆时针旋转弧度
                * `dz`: z 方向逆时针旋转弧度
                * `center`: 旋转中心，默认为原点
                * `axis`: 旋转轴线，无默认值
        """
    def scale(self, kx, ky, kz, center):
        """
        缩放几何体中的所有 3D 对象
        
                * `kx`: x 方向缩放比例
                * `ky`: y 方向缩放比例
                * `kz`: z 方向缩放比例
                * `center`: 缩放中心，默认为几何中心
        """
    def center(self):
        """
        几何中心
        """
    def update(self):
        """
        更新几何体
        """
    def append(self, *sides):
        """
        给几何体添加更多新的面
        
                * `sides`: `Side` 类
        """

def translate(coordinate: tuple[float, float, float], dx: float, dy: float, dz: float) -> None:
    """
    将一个三维空间中的点进行平移
    
        * `coordinate`: 点的空间坐标
        * `dx`: x 方向位移长度
        * `dy`: y 方向位移长度
        * `dz`: z 方向位移长度
    """

def rotate(coordinate, dx, dy, dz, center):
    ...

def rotate(coordinate, dx, axis):
    ...

def rotate(coordinate, dx, dy, dz, center, axis):
    """
    将一个三维空间中的点以一个点或线为参照进行旋转（实现方式为欧拉角）
    
        * `coordinate`: 点的空间坐标
        * `dx`: x 方向逆时针旋转弧度，或者绕旋转轴线的旋转弧度
        * `dy`: y 方向逆时针旋转弧度
        * `dz`: z 方向逆时针旋转弧度
        * `center`: 旋转中心的空间坐标
        * `axis`: 旋转轴线的空间坐标
    """

def scale(coordinate, kx, ky, kz, center):
    """
    将一个三维空间中的点以另一个点为缩放中心进行缩放
    
        * `coordinate`: 点的空间坐标
        * `kx`: x 方向缩放比例
        * `ky`: y 方向缩放比例
        * `kz`: z 方向缩放比例
        * `center`: 缩放中心的空间坐标
    """

def project(coordinate, distance):
    """
    将一个三维空间中的点投影到指定距离的正向平面上，并返回在该平面上的坐标
    
        * `coordinate`: 点的空间坐标
        * `distance`: 正向平面的距离（平面正对着我们）
    """
