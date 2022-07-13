from machine import Pin, PWM
import utime

MID = 1500000
MIN = 1000000
MAX = 2000000

led = machine.Pin("LED", machine.Pin.OUT)

pwm15 = PWM(Pin(15))
pwm12 = PWM(Pin(12))

pwm15.freq(50)
pwm15.duty_ns(MID)

pwm12.freq(50)
pwm12.duty_ns(MID)

print("Starting")

while True:     
    led.on()

    pwm15.duty_ns(MIN)
    pwm12.duty_ns(MIN)
    utime.sleep(1)

    pwm15.duty_ns(MID)
    pwm12.duty_ns(MID)
    utime.sleep(1)
    
    pwm15.duty_ns(MAX)
    pwm12.duty_ns(MAX)
    utime.sleep(1)
