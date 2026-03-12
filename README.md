# PDF_Count


这是一个可以一次性批量统计一个文件夹里包括子文件夹里的PDF的页数的python文件


This Python script batches and counts the total number of pages in all PDF files within a folder and its subfolders.


これは、フォルダ内およびサブフォルダ内のPDFファイルのページ数を一度にバッチ処理で統計するPythonスクリプトです。

那就写一个极简版 README.md 就够了。

你直接用这个：

# PDF Page Counter

递归统计文件夹里所有 PDF 的页数，支持子文件夹。

## 先做一次安装

```bash
pip3 install pypdf

运行方法

先进入项目目录：

cd /你的项目路径

然后运行：

python3 pdf_counter.py

接着把你要统计的文件夹直接拖到终端里，按回车即可。

例如：

python3 pdf_counter.py /Volumes/material\ 1/听力/听力PDF文件/ETJ\ accent

说明
	•	支持嵌套子文件夹
	•	会在终端里打印每个 PDF 的页数
	•	会自动统计总页数
	•	会跳过 ._xxx.pdf 这类无效文件

如果你还想更省事，我建议把脚本文件名固定成：

```bash
pdf_counter.py

这样你以后看到仓库，基本就只需要记住两步：

pip3 install pypdf

python3 pdf_counter.py [把文件夹拖进终端]

