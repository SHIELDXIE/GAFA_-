# GAFA_校园网一键登录脚本

version：1.0    

#使用方式:  
  1.安装Python运行环境 https://www.python.org/downloads/  
  2.浏览器打开校园网登录页，打开开发者选项（f12）
  ![image](https://user-images.githubusercontent.com/37254173/160872034-4019d578-9285-4d32-8f37-73f40d647102.png)  
  3.登录校园网，抓取登录 GET_URL, 并复制保存
  ![image](https://user-images.githubusercontent.com/37254173/160872188-bdd61d83-d71d-4456-8b2d-81e2fdddda68.png)  
  4.编辑脚本（以windows记事本为例），在response = requests.get('__') 中填入GET_URL  
  ![image](https://user-images.githubusercontent.com/37254173/160873171-690d5989-b54b-4cb3-91f9-8f55c4946e79.png)  
  5.完成
