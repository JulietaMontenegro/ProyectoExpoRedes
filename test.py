# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel

# Configuración inicial
pixel_pin = board.D18
num_pixels = 300
ORDER = neopixel.GRB

# Inicialización de los NeoPixels
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.5, auto_write=False, pixel_order=ORDER
)


def blinkRojo(color, duration):
    pixels.fill(color)  
    pixels.show()  
    time.sleep(duration)  
    pixels.fill((0, 0, 0))
    pixels.show()  
    time.sleep(duration)  


def relampago():
    veces = 6
    actual = 0
    for actual in range (veces):
        pixels.fill((255, 255, 255))     
        pixels.show()  
        time.sleep(0.01)
        pixels.fill((0, 0, 0))
        pixels.show()  
        time.sleep(0.01)  


def inicioJuegos():
    for i in range(num_pixels):
        for j in range(i+1):
            pixels[j] = (255, 0, 0)
        pixels.show()
        time.sleep(0.005)


def tiempoJuego():
    pixels.fill((255, 0, 0))
    pixels.show()
    time.sleep(5)
    pixels.show()
    relampago()


def apagar():
    pixels.fill((0, 0, 0))
    pixels.show() 


def cielo():
    for i in range(num_pixels):
        for j in range(i+1):
            pixels[j] = (41, 164, 60)
        pixels.show()
        time.sleep(0.005)    



def efectoDeOla():
    for i in range(num_pixels):

        for j in range(i+1):
            if (i>5):
                pixels[j-5] = (0, 0, 0)
            pixels[j] = (82, 128, 121)           
        pixels.show()
        time.sleep(0.025)    



# inicioJuegos()
# while True:
#     tiempoJuego()







