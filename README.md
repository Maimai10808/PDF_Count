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

不是装到某个“文件夹”里理解的，pip3 install pypdf 装的是你这台电脑当前 Python 环境里的包。

你现在最稳妥的理解是分两种：

第一种，装到当前系统/当前 Python 环境里。
你在终端直接运行：

pip3 install pypdf

它会装到你这台 Mac 的 python3 对应环境里。以后只要还是用这个同一个 python3，这个库一般就能用。

第二种，更推荐，装到项目自己的虚拟环境里。
这也是你前面已经碰到过的标准做法。好处是不会污染系统环境，每个项目自己管自己的依赖，更干净。

如果你是从 GitHub 下载一个项目，最标准流程是这样：

先进入这个项目文件夹。
比如你下载后项目在桌面：

cd ~/Desktop/你的项目文件夹

然后创建虚拟环境：

python3 -m venv .venv

激活它：

source .venv/bin/activate

激活后，你会看到命令行前面多了一个 (.venv)。

然后再安装：

pip install pypdf

注意这里已经不一定非写 pip3，因为你激活虚拟环境后，pip 就是在这个项目的小环境里安装。

最后运行：

python pdf_counter.py

这里我顺便解释你问的两个概念。

“项目路径”是什么意思？
就是你这个 GitHub 项目下载到你电脑上的那个文件夹位置。
例如你下载后放在桌面，文件夹叫 pdf-counter，那它的项目路径就是：

~/Desktop/pdf-counter

或者完整一点可能是：

/Users/你的用户名/Desktop/pdf-counter

“如果我在 GitHub 上看到它，下载下来后怎么弄？”
最简单就是按下面这套来：
	1.	在 GitHub 点 Download ZIP，下载并解压。
	2.	打开终端。
	3.	cd 到解压后的项目文件夹。
	4.	创建并激活虚拟环境。
	5.	安装依赖。
	6.	运行脚本。

完整示例：

cd ~/Desktop/pdf-counter
python3 -m venv .venv
source .venv/bin/activate
pip install pypdf
python pdf_counter.py /Volumes/material\ 1/听力/听力PDF文件/ETJ\ accent

你也可以拖文件夹进终端，就不用手敲路径。

你目前最适合的做法，我建议直接固定成这一套：

cd 项目文件夹
python3 -m venv .venv
source .venv/bin/activate
pip install pypdf
python pdf_counter.py [把文件夹拖进来]

这样以后任何 GitHub 上下载下来的 Python 小工具，你基本都可以按这个套路跑起来。

