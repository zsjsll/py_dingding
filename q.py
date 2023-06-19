import uiautomator2 as u2

# //18803bf5  设备序列号，如果只有一个设备可以不传，设备序列号获取方式可以在连接好设备后再dos窗口通过
# //指令  adb devices查看


d = u2.connect("4c99a1fa")

d.screen_on()
print(d.info)
d.app_start("com.alibaba.android.rimet")
