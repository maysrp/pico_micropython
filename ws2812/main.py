from neopixel import Neopixel
pixels = Neopixel(1, 0, 0, "GRB")

# 10个灯 状态 使用GPIO0  使用RGB（GRB）
# 从0开始

pixels.set_pixel(5, (10, 0, 0))
pixels.set_pixel_line(5, 7, (0, 10, 0))