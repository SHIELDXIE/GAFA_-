#GAFA校园网一键登录脚本
#ver:1.1
#项目地址:https://github.com/SHIELDXIE/GAFA_NetworkLoginScript
#python库：ping3;requests;win10toast
from ping3 import ping, verbose_ping
import time
from datetime import datetime

def ping_some_ip(host,src_addr=None):
    second = ping(host,src_addr=src_addr)
    return second
    
if __name__ == '__main__': #ping校园网登录服务器，检测是否连接校园网
    host = '183.6.94.28'
    src_addr = None
    # 简单用法 ping地址即可，超时会返回None 否则返回耗时，单位默认是秒
    while True:
        print('ping @ {}'.format(datetime.now()))
        result = ping_some_ip(host,src_addr)
        if result is None:
            print(result)
            from win10toast import ToastNotifier #未连接校园网，通知
            toaster = ToastNotifier()
            toaster.show_toast("脚本运行失败",
                    "未接入校园网，请检查网络",
                   icon_path=None,
                   duration=5,
                   threaded=True)                   
            while toaster.notification_active(): time.sleep(0.1)# 等待提示框关闭
            break
        else: #已连接校园网，登录
            import time
            import requests
            #get_url
            response = requests.get('') #⬅在此处填入URL
            print(response.headers)

            from ping3 import ping, verbose_ping
            import time
            from datetime import datetime

            def ping_some_ip(host,src_addr=None):
                second = ping(host,src_addr=src_addr)
                return second

            if __name__ == '__main__': #检测是否登陆成功，ping:'baidu.com'
                host = 'www.baidu.com'
                src_addr = None
            
                while True:
                    print('ping @ {}'.format(datetime.now()))
                    result = ping_some_ip(host,src_addr)
                    if result is None:
                        print(result)
                        from win10toast import ToastNotifier #连接失败，通知
                        toaster = ToastNotifier()
                        toaster.show_toast("脚本运行失败",
                                "网络未接通，请检查网络",
                            icon_path=None,
                            duration=5,
                            threaded=True)                   
                        while toaster.notification_active(): time.sleep(0.1)# 等待提示框关闭
                        break
                    else:
                        print(result)
                        from win10toast import ToastNotifier #连接成功，通知
                        toaster = ToastNotifier()
                        toaster.show_toast("脚本运行成功",
                                "校园网已连接",
                            icon_path=None,
                            duration=5,
                            threaded=True)                   
                        while toaster.notification_active(): time.sleep(0.1)# 等待提示框关闭
                        break




