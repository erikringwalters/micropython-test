from machine import Pin, PWM
import utime

MID = 1500000
MIN = 1000000
MAX = 2000000

led = machine.Pin("LED", machine.Pin.OUT)

pwm15 = PWM(Pin(15))

pwm15.freq(50)
pwm15.duty_ns(MID)

while True: 
    print("Starting")
    led.on()

    pwm15.duty_ns(MIN)
    utime.sleep(1)
    pwm15.duty_ns(MID)
    utime.sleep(1)
    pwm15.duty_ns(MAX)
    utime.sleep(1)
