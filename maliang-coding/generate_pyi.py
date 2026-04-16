"""
生成.pyi文件
"""

import ast
import os
import sys
from pathlib import Path

def extractTypeInfo(file_path: str) -> str:
    """
    提取类型信息，生成正确的.pyi格式
    """

    with open(file_path, 'r', encoding='utf-8') as f:
        source = f.read()
    
    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        print(f"  语法错误: {e}")
        return f'"""{os.path.basename(file_path)}的类型存根文件（解析错误）"""\n'
    
    lines = []
    
    # 提取模块级docstring
    module_docstring = ""
    if (tree.body and isinstance(tree.body[0], ast.Expr) and 
        isinstance(tree.body[0].value, ast.Constant) and
        isinstance(tree.body[0].value.value, str)):
        module_docstring = tree.body[0].value.value
    
    if module_docstring:
        lines.append(formatDocstring(module_docstring, 0))
    else:
        lines.append(formatDocstring(f"{os.path.basename(file_path)}的类型存根文件", 0))
    lines.append('')
    
    # 处理导入
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                lines.append(f"import {alias.name}")
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ''
            if node.level > 0:
                module = '.' * node.level + module
            if node.names[0].name == '*':
                lines.append(f"from {module} import *")
            else:
                names = ', '.join(alias.name for alias in node.names)
                lines.append(f"from {module} import {names}")
    
    # 添加空行（如果有导入）
    if any(line.startswith('import ') or line.startswith('from ') for line in lines[2:]):
        lines.append('')
    
    # 处理类定义
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            class_lines = []
            
            # 类定义
            bases = []
            for base in node.bases:
                try:
                    bases.append(ast.unparse(base))
                except:
                    bases.append("Any")
            
            class_def = f"class {node.name}"
            if bases:
                class_def += f"({', '.join(bases)})"
            class_def += ":"
            class_lines.append(class_def)
            
            # 类docstring
            docstring = extractDocstring(node)
            if docstring:
                # 添加docstring，确保后面有空行
                class_lines.append(formatDocstring(docstring, 1))
                class_lines.append('')
            
            # 类属性
            for item in node.body:
                if isinstance(item, ast.AnnAssign):
                    # 带类型注解的属性
                    try:
                        target = ast.unparse(item.target)
                        annotation = ast.unparse(item.annotation)
                        class_lines.append(f"    {target}: {annotation}")
                    except:
                        pass
                
                elif isinstance(item, ast.Assign):
                    # 不带类型注解的属性
                    for target in item.targets:
                        if isinstance(target, ast.Name):
                            try:
                                value = ast.unparse(item.value)
                                class_lines.append(f"    {target.id} = {value}")
                            except:
                                class_lines.append(f"    {target.id} = ...")
            
            # 类方法
            methods_added = False
            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    # 跳过私有方法（但不是特殊方法）
                    if item.name.startswith('_') and not (item.name.startswith('__') and item.name.endswith('__')):
                        continue
                    
                    # 检查装饰器
                    decorators = []
                    for decorator in item.decorator_list:
                        try:
                            decorator_str = ast.unparse(decorator)
                            if decorator_str == "classmethod":
                                decorators.append("@classmethod")
                            elif decorator_str == "staticmethod":
                                decorators.append("@staticmethod")
                            else:
                                decorators.append(f"@{decorator_str}")
                        except:
                            pass
                    
                    # 方法签名
                    try:
                        # 提取方法定义行
                        if isinstance(item, ast.AsyncFunctionDef):
                            def_line = f"async def {item.name}"
                        else:
                            def_line = f"def {item.name}"
                        
                        # 参数
                        args = []
                        for arg in item.args.posonlyargs:
                            args.append(formatArg(arg))
                        for arg in item.args.args:
                            args.append(formatArg(arg))
                        if item.args.vararg:
                            args.append(f"*{formatArg(item.args.vararg)}")
                        for arg in item.args.kwonlyargs:
                            args.append(formatArg(arg))
                        if item.args.kwarg:
                            args.append(f"**{formatArg(item.args.kwarg)}")
                        
                        def_line += f"({', '.join(args)})"
                        
                        # 返回类型
                        if item.returns:
                            returns = ast.unparse(item.returns)
                            def_line += f" -> {returns}"
                        
                        # 提取方法docstring
                        method_docstring = extractDocstring(item)
                        
                        # 添加装饰器和方法
                        for decorator in decorators:
                            class_lines.append(f"    {decorator}")
                        class_lines.append(f"    {def_line}:")
                        if method_docstring:
                            class_lines.append(formatDocstring(method_docstring, 2))
                        else:
                            class_lines.append("        ...")
                        methods_added = True
                        
                    except:
                        pass
            
            # 如果没有内容，添加省略号
            if len(class_lines) == 1 or (len(class_lines) == 2 and class_lines[1] == ''):
                class_lines.append("    ...")
            
            lines.extend(class_lines)
            lines.append('')
    
    # 处理模块级函数
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            # 检查是否在类中
            in_class = False
            for parent in ast.walk(tree):
                if isinstance(parent, ast.ClassDef) and node in parent.body:
                    in_class = True
                    break
            
            if not in_class and not node.name.startswith('_'):
                try:
                    # 函数签名
                    if isinstance(node, ast.AsyncFunctionDef):
                        def_line = f"async def {node.name}"
                    else:
                        def_line = f"def {node.name}"
                    
                    # 参数
                    args = []
                    for arg in node.args.posonlyargs:
                        args.append(formatArg(arg))
                    for arg in node.args.args:
                        args.append(formatArg(arg))
                    if node.args.vararg:
                        args.append(f"*{formatArg(node.args.vararg)}")
                    for arg in node.args.kwonlyargs:
                        args.append(formatArg(arg))
                    if node.args.kwarg:
                        args.append(f"**{formatArg(node.args.kwarg)}")
                    
                    def_line += f"({', '.join(args)})"
                    
                    # 返回类型
                    if node.returns:
                        returns = ast.unparse(node.returns)
                        def_line += f" -> {returns}"
                    
                    # 提取函数docstring
                    func_docstring = extractDocstring(node)
                    
                    lines.append(f"{def_line}:")
                    if func_docstring:
                        lines.append(formatDocstring(func_docstring, 1))
                    else:
                        lines.append("    ...")
                    lines.append('')
                    
                except:
                    pass
    
    return '\n'.join(lines)

def extractDocstring(node) -> str:
    """
    提取节点的docstring
    """

    if (node.body and isinstance(node.body[0], ast.Expr) and 
        isinstance(node.body[0].value, ast.Constant) and
        isinstance(node.body[0].value.value, str)):
        return node.body[0].value.value
    return ""

def formatDocstring(docstring: str, indent_level: int = 0) -> str:
    """
    格式化docstring为多行格式
    """
    if not docstring:
        return ""
    
    indent = " " * (indent_level * 4)
    lines = docstring.strip().split('\n')
    
    # 如果只有一行，直接返回多行格式
    if len(lines) == 1:
        return f'{indent}"""\n{indent}{lines[0]}\n{indent}"""'
    
    # 多行docstring
    result = [f'{indent}"""']
    for line in lines:
        result.append(f'{indent}{line}')
    result.append(f'{indent}"""')
    return '\n'.join(result)

def formatArg(arg) -> str:
    """
    格式化参数
    """

    try:
        return ast.unparse(arg)
    except:
        return arg.arg if hasattr(arg, 'arg') else str(arg)

def generatePyi():
    """
    生成所有正确的.pyi文件
    """
    
    base_dir = Path(__file__).parent.resolve()
    package_dir = Path(sys.executable).parent / "Lib" / "site-packages" / "maliang"
    output_dir = base_dir / "references/pyi"
    
    # 确保输出目录存在
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 查找所有Python文件
    python_files = list(package_dir.rglob("*.py"))
    
    print(f"找到 {len(python_files)} 个Python文件")
    
    for py_file in python_files:
        try:
            # 生成.pyi内容
            pyi_content = extractTypeInfo(str(py_file))
            
            # 确定输出路径
            rel_path = py_file.relative_to(package_dir)
            output_path = output_dir / rel_path.with_suffix('.pyi')
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            # 写入文件
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(pyi_content)
            
            print(f"已生成: {output_path}")
            
        except Exception as e:
            print(f"错误处理文件 {py_file}: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n完成!")

if __name__ == "__main__":
    generatePyi()