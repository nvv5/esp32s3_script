from machine import Pin, ADC
import time
from neopixel import NeoPixel

pin = Pin(48, Pin.OUT)
np = NeoPixel(pin, 1)
# 配置 ADC 引脚
adc_pin = Pin(2)  # 假设连接的 ADC 引脚是 GPIO 2

# 创建 ADC 对象
adc = ADC(adc_pin)

# 读取 ADC 信号
while True:
    adc_values = []
    for _ in range(10):  # 进行10次采样
        adc_values.append(adc.read())  # 读取 ADC 信号值
        time.sleep_ms(10)  # 间隔10毫秒
    adc_value_avg = sum(adc_values) // len(adc_values)  # 计算平均值
    
    if adc_value_avg > 80:
        brightness=int(adc_value_avg / 4095 * 255*1.5)
        np[0] = (0, 0, brightness)
        np.write()
        print("Average ADC value:", adc_value_avg,"Brightness:",brightness)  # 打印平均值
    else:
        np[0] = (0, 0, 0)
        np.write()
        print("Average ADC value:", adc_value_avg,"Brightness:0")
    time.sleep(1)
