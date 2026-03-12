import os
import sys
from pypdf import PdfReader


def is_valid_pdf_file(filename: str) -> bool:
    """判断是否为需要处理的 PDF 文件。"""
    lower_name = filename.lower()
    if not lower_name.endswith(".pdf"):
        return False
    if filename.startswith("._") or filename.startswith("."):
        return False
    return True


def count_pdf_pages(pdf_path: str) -> int:
    """读取单个 PDF 页数。"""
    reader = PdfReader(pdf_path)
    return len(reader.pages)


def scan_folder(root_folder: str):
    """递归扫描文件夹中的所有 PDF。"""
    total_pages = 0
    success_count = 0
    fail_count = 0

    print(f"\n开始扫描文件夹：{root_folder}")
    print("=" * 80)

    for current_root, _, files in os.walk(root_folder):
        for filename in files:
            if not is_valid_pdf_file(filename):
                continue

            pdf_path = os.path.join(current_root, filename)

            try:
                pages = count_pdf_pages(pdf_path)
                total_pages += pages
                success_count += 1

                relative_path = os.path.relpath(pdf_path, root_folder)
                print(f"[成功] {relative_path} -> {pages} 页")

            except Exception as e:
                fail_count += 1
                relative_path = os.path.relpath(pdf_path, root_folder)
                print(f"[失败] {relative_path} -> {e}")

    print("=" * 80)
    print("扫描完成")
    print(f"成功读取 PDF 数量：{success_count}")
    print(f"读取失败 PDF 数量：{fail_count}")
    print(f"PDF 总页数：{total_pages}")


def main():
    if len(sys.argv) < 2:
        print("用法：")
        print("python3 pdf_counter.py [把文件夹拖到这里]")
        print("\n例如：")
        print('python3 pdf_counter.py "/Volumes/material 1/听力/听力PDF文件/ETJ accent"')
        return

    folder_path = sys.argv[1].strip()

    if not os.path.exists(folder_path):
        print(f"路径不存在：{folder_path}")
        return

    if not os.path.isdir(folder_path):
        print(f"这不是文件夹：{folder_path}")
        return

    scan_folder(folder_path)


if __name__ == "__main__":
    main()
