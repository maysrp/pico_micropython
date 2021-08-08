import ws2812b
pixels = ws2812b.ws2812b(10,0,0)
#设置10个RGB灯
pixels.set_pixel(5,10,0,0)
pixels.set_pixel_line(5,7,0,10,0)
pixels.fill(20,5,0)
pixels.show()