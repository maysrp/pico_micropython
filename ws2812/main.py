from neopixel import Neopixel

pixels = Neopixel(10, 0, 0, "GRB")

# 10个灯 使用GPIO0 状态0 使用RGB（GRB）
# 从0开始

pixels.set_pixel(5, (10, 0, 0))
pixels.set_pixel_line(5, 7, (0, 10, 0))