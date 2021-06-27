# Catch events from multiple mice on Linux by Python
It might be useful for controlling something in Linux or hardware, connected to linux PC (e.g. Raspberry Pi), using internal mouse buttons, wheel and optical sensor. It works both in GUI and in console-only modes. The program reads from files `mouse*` in the folder `/dev/input`.

This is an example, when up to four mice connected to [Raspberry Pi Zero](https://www.raspberrypi.org/products/raspberry-pi-zero/) via [USB HUB HAT](https://www.waveshare.com/usb-hub-hat.htm) and extra USB-hub. In this case connecting WiFi adapter to the USB HUB HAT hangs the system - it's recommened to connect it to extra USB-hub for stubility.

![image](https://user-images.githubusercontent.com/702860/123551573-ae925000-d772-11eb-8e09-9ba608b77486.png)

USB HUB HAT behaves more stable in this then case, than regular USB-hubs (tried cheap and more expencive ones, with external power). This USB HUB HAT actually can be connected to the RPi board with micro-USB to USB-A cable - no need to connect it to GPIO connector.

Run:
```
python3 multiple-mice.py
```

Because of large number of printed messages - the program consumes 100% of RPi Zero CPU. When `print()` is commented (not used) - 10-15% of CPU for moving 2 mice, up to 50% for moving 4 mice.
