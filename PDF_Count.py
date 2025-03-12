import os
from PyPDF2 import PdfReader  # 使用新的 PdfReader 类


# 定义计算文件夹中所有 PDF 文件总页数的函数（包括子文件夹）
def count_total_pages_in_pdfs(folder_path):
    total_pages = 0  # 初始化总页数为 0

    # 遍历文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(folder_path):  # 使用 os.walk 遍历文件夹及其子文件夹
        for filename in files:
            if filename.lower().endswith('.pdf'):  # 只处理 PDF 文件，忽略大小写
                pdf_path = os.path.join(root, filename)  # 获取 PDF 文件的完整路径

                print(f"处理文件: {pdf_path}")  # 调试信息，查看正在处理哪个文件

                try:
                    # 打开 PDF 文件并读取
                    with open(pdf_path, 'rb') as pdf_file:
                        pdf_reader = PdfReader(pdf_file)  # 使用新的 PdfReader 类
                        total_pages += len(pdf_reader.pages)  # 获取当前 PDF 的页数并加到总页数中
                except Exception as e:
                    print(f"无法读取文件 {filename}: {e}")

    return total_pages


# 设置文件夹路径
folder_path = '/Users/mac/Downloads/2025年1-4月安娜口语素材'  # 请替换为实际的文件夹路径

# 确保路径是正确的
if not os.path.exists(folder_path):
    print(f"路径 {folder_path} 不存在，请检查路径是否正确。")
else:
    # 计算并打印总页数
    total_pages = count_total_pages_in_pdfs(folder_path)
    print(f"文件夹中的所有 PDF 总共 {total_pages} 页。")