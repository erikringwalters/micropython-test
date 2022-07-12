from machine import Pin, Timer
# from time import sleep

print("Starting")

led = Pin(15, Pin.OUT)
tim  = Timer()

def tick(timer):
    global led
    led.toggle()

tim.init(freq=2.5, mode=Timer.PERIODIC, callback=tick)
