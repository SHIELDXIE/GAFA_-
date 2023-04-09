#GAFA校园网一键登录脚本
#ver:2.0
#项目地址:https://github.com/SHIELDXIE/GAFA_NetworkLoginScript
#python库：ping3;requests;win10toast;tkinter

from ping3 import ping
from datetime import datetime
import requests
from win10toast import ToastNotifier
import tkinter as tk

def ping_some_ip(host, src_addr=None):
    second = ping(host, src_addr=src_addr)
    return second

def notify(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, icon_path=None, duration=2.5, threaded=True)

def login(username, password):
    url = 'http://183.6.94.28/drcom/login?callback=dr1003&DDDDD={}%40GZARTS.GZ&upass={}&0MKKey=123456&R1=0&R3=0&R6=1&para=00&v6ip=&v=0000'.format(username, password)
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False

def on_login_click():
    username = username_entry.get()
    password = password_entry.get()
    if username and password:
        # ping校园网登录服务器，检测是否连接校园网
        host = '183.6.94.28'
        result = ping_some_ip(host)
        if result is None:
            notify("脚本运行失败", "未接入校园网，请检查网络")
        else:
            # 已连接校园网，登录
            if login(username, password):
                # 检测是否登陆成功，ping:'baidu.com'
                host = 'baidu.com'
                result = ping_some_ip(host)
                if result is None:
                    notify("脚本运行失败", "网络未接通，请检查网络")
                else:
                    notify("脚本运行成功", "校园网已连接")
                    # 保存账号密码
                    if remember_var.get() == 1:
                        with open('account.txt', 'w') as f:
                            f.write('{}\n{}'.format(username, password))
                    # 关闭窗口
                    window.destroy()
            else:
                notify("脚本运行失败", "登录失败，请检查账号密码是否正确")
    else:
        notify("脚本运行失败", "请输入账号和密码")

if __name__ == '__main__':
    # 创建窗口
    window = tk.Tk()
    window.title("GAFA校园网一键登录脚本")
    window.geometry("300x200")

    # 创建账号输入框
    username_label = tk.Label(window, text="账号：")
    username_label.pack()
    username_entry = tk.Entry(window)
    username_entry.pack()

    # 创建密码输入框
    password_label = tk.Label(window, text="密码：")
    password_label.pack()
    password_entry = tk.Entry(window, show="*")
    password_entry.pack()

    # 创建记住账号密码复选框
    remember_var = tk.IntVar()
    remember_checkbox = tk.Checkbutton(window, text="记住账号密码", variable=remember_var)
    remember_checkbox.pack()

    # 读取保存的账号密码
    try:
        with open('account.txt', 'r') as f:
            account = f.read().split('\n')
            username_entry.insert(0, account[0])
            password_entry.insert(0, account[1])
    except:
        pass

    # 创建登录按钮
    login_button = tk.Button(window, text="登录", command=on_login_click)
    login_button.pack()

    # 运行窗口
    window.mainloop()