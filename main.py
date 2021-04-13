import webbrowser
from tkinter import ttk, messagebox
import os
import requests
from bs4 import BeautifulSoup
from placeholder import *
import tkinter as tk


window = tk.Tk()
title = window.title("网页源码获取")
# 设置窗口大小
width = 400
height = 200
# 获取屏幕大小
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
# 计算出x, y的值
x = (screenwidth - width) / 2
y = (screenheight - height) / 2
window.geometry("%dx%d+%d+%d" % (width, height, x, y))
# 锁定窗口大小
window.resizable(width=False, height=False)
# 设置窗口图标
window.iconbitmap('./favicon.ico')


# 所有按钮点击事件
# -------------------------------------------------------------------------
def app_version():
    app_version_app()


def about_author():
    url = "https://qm.qq.com/cgi-bin/qm/qr?k=oP4HmGxuq9LNxdxZrt1VJmBI0OehhHw0&noverify=0"
    webbrowser.open(url, new=0, autoraise=True)


def communication_group():
    url = "https://jq.qq.com/?_wv=1027&k=laoNxIRL"
    webbrowser.open(url, new=0, autoraise=True)


def official_website():
    url = "http://bbs.xfxyfs.top/"
    webbrowser.open(url, new=0, autoraise=True)


def get_source_code():
    url_head = url_header.get()
    url_foot = url_input.get()
    if url_head == "请选择":
        messagebox.showinfo("温馨提示", "url头没有选择")
    if url_foot == "请输入网址":
        messagebox.showinfo("温馨提示", "请填写网址")
    url = url_head + url_foot
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    s = r.text
    soup = BeautifulSoup(s, "html.parser")
    s = soup.prettify()
    dir_file = os.getcwd()
    xhtml = open(dir_file + "\\" + "code.html", 'w', encoding='utf-8')
    xhtml.write(s)


def download_file():
    messagebox.showinfo("温馨提醒", "文件已经保存本地，查看打开后的目录中的“index.html”文件")
    start_directory = os.getcwd()
    os.system("explorer.exe %s" % start_directory)


# -------------------------------------------------------------------------
# 主窗口内部组件
# 分界线
# -------------------------------------------------------------------------
url_label = tk.Label(window, font="楷体", text="网址:", fg="#6D65DD")
url_label.place(x=5, y=5)
url_header = ttk.Combobox(window, width=10)
url_header.place(x=50, y=5)
url_header['value'] = ('请选择', 'http://', 'https://')
url_header.current(0)
url_input = Entryplaceholer(window, "请输入网址")
url_input.place(x=150, y=5, width=238)
url_gety_btn = tk.Button(window, font="楷体", text="获取源码", width=10, command=get_source_code)
url_gety_btn.place(x=10, y=50)
url_gety_btn = tk.Button(window, font="楷体", text="下载文件", width=10, command=download_file)
url_gety_btn.place(x=290, y=50)
# 顶部菜单按钮
top_menu_fri = tk.Menu(window)
top_menu_one = tk.Menu(top_menu_fri, tearoff=0)
top_menu_fri.add_cascade(label="关于软件", menu=top_menu_one)
top_menu_one.add_command(label="软件信息", command=app_version)
top_menu_one.add_command(label="联系作者", command=about_author)
top_menu_one.add_command(label="交流群", command=communication_group)
top_menu_one.add_command(label="官网", command=official_website)

window.config(menu=top_menu_fri)


# 软件信息子窗口
# ---------------------------------------------------

def app_version_app():
    app_version_root = tk.Tk()
    app_version_root.title("软件信息")
    app_version_root.geometry("300x200")
    # ----------------------------
    tk.Label(app_version_root, text="软件名称:WEB学习工具", font="楷体", fg="#5254FF").pack()
    tk.Label(app_version_root, text="软件版本号:1.4121.2207", font="楷体", fg="#5254FF").pack()
    tk.Label(app_version_root, text="原创作者:天域工作室", font="楷体", fg="#5254FF").pack()
    tk.Label(app_version_root, text="交流群号:925494462:", font="楷体", fg="#5254FF").pack()
    tk.Label(app_version_root, text="官网:http://bbs.xfxyfs.top/", font="楷体", fg="#5254FF").pack()
    tk.Label(app_version_root, text="开源:https://github.com/cnxyya/app", font="楷体", fg="#5254FF").pack()
    # ----------------------------
    app_version_root.mainloop()


# ---------------------------------------------------

window.mainloop()
