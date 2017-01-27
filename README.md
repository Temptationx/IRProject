# IRProject

使用手机遥控电视

项目分为三个部分：
1. 红外学习模块
	用 Arduino 与红外接收模块连接，使用IRremote库的示例就可以得到红外编码
2. 红外发射模块(irsend)
	Arduino加上红外发射模块，通过USB串口与树莓派连接，通信格式是0xAA + 32位红外编码
3. 人机交互界面(website)
	单页webapp形式，服务器使用Python+Flask，运行在Raspberry上，使用串口与Arduino通信
	网址是IP:8000/ir