#!/usr/bin/env python3
# coding: utf-8

from time import localtime,strftime,sleep

import Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# Raspberry Pi hardware SPI config:
DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

# Hardware SPI usage:
disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

# Initialize library.
disp.begin(contrast=60)

# Clear display.
disp.clear()
disp.display()
while(True):
    time_string = strftime("%H:%M:%S", localtime())
    image= Image.new('1', ( LCD.LCDWIDTH,LCD.LCDHEIGHT))
    draw= ImageDraw.Draw(image)
    draw.rectangle((0,0,84,48), outline=0, fill=1)
    font= ImageFont.load_default()
    draw.text((8,20), str(time_string), font=font)
    disp.image(image)
    disp.display()
    sleep(1)
