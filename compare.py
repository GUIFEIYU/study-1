import os
import sys
import yaml
import pandas as pd
from pathlib import Path


def get_yml_files(folder: str) -> list:
    """获取文件夹中所有YAML文件路径"""
    yml_files = []
    for root, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(('.yml', '.yaml')):
                yml_files.append(os.path.join(root, file))
    return yml_files


def flatten_yaml(data: dict, parent_key: str = '', sep: str = '.') -> dict:
    """递归展开嵌套字典为扁平化键值对"""
    items = {}
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_yaml(v, new_key, sep))
        else:
            items[new_key] = v
    return items


def generate_comparison_table(folder_path: str, output_file: str = '对比结果.xlsx'):
    """生成配置差异对比表"""
    # 获取所有YAML文件
    yml_files = get_yml_files(folder_path)
    if not yml_files:
        raise ValueError("未找到YAML文件")

    # 解析文件并收集配置项
    all_keys = set()
    file_data = {}
    for file_path in yml_files:
        try:
            with open(file_path, 'r', encoding="utf-8") as f:
                data = yaml.safe_load(f) or {}
                flat_data = flatten_yaml(data)
                file_data[file_path] = flat_data
                all_keys.update(flat_data.keys())
        except yaml.YAMLError as e:
            print(f"⚠️ 解析失败: {os.path.basename(file_path)} - {str(e)}")

    # 构建对比表格
    rows = []
    for key in sorted(all_keys):
        row = {'配置项路径': key}
        for path in yml_files:
            value = file_data.get(path, {}).get(key, '❌ 不存在')
            row[os.path.basename(path)] = value
        rows.append(row)

    # 导出Excel
    df = pd.DataFrame(rows)
    df.to_excel(output_file, index=False)
    print(f"✅ 对比结果已保存至: {output_file}")

def get_user_input() -> tuple:
    """获取用户输入的文件夹路径和输出文件名"""
    print("📂 请输入配置文件所在文件夹路径：")
    folder = input().strip('"')
    print("\n📝 请输入差异对比表文件名（无需后缀）：")
    output = input().strip() + ".xlsx"
    return folder, output

def validate_path(folder: str) -> None:
    """验证路径有效性"""
    if not os.path.isdir(folder):
        print(f"❌ 路径无效: {folder}")
        sys.exit(1)


def main():
    # 用户交互输入
    folder, output_file = get_user_input()
    validate_path(folder)

    # 原对比逻辑（保持不变）
    generate_comparison_table(folder, output_file)
    print(f"\n✅ 操作完成！文件已保存至: {os.path.abspath(output_file)}")


# 使用示例
if __name__ == "__main__":
    main()