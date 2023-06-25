import uiautomator2 as u2

# //18803bf5  设备序列号，如果只有一个设备可以不传，设备序列号获取方式可以在连接好设备后再dos窗口通过
# //指令  adb devices查看


d = u2.connect("2100cb76")
# d = u2.connect("860BDMK229ZQ")

if d.info["screenOn"]:
    pass
else:
    d.screen_on()
    d.swipe(
        d.info["displayWidth"] * 0.5,
        d.info["displayHeight"] * 0.9,
        d.info["displayWidth"] * 0.5,
        d.info["displayHeight"] * 0.1,
        duration=0.35,
    )
# d.press("volume_mute")

d.app_start("com.alibaba.android.rimet")
