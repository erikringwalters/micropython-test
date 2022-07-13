from machine import Pin, PWM
import utime

MID = 1500000
MIN = 1000000
MAX = 2000000

led = machine.Pin("LED", machine.Pin.OUT)

pwm12 = PWM(Pin(12))
pwm14 = PWM(Pin(14))
pwm15 = PWM(Pin(15))

pwm12.freq(50)
pwm12.duty_ns(MID)

pwm14.freq(50)
pwm14.duty_ns(MID)

pwm15.freq(50)
pwm15.duty_ns(MID)


print("Starting")

while True:     
    led.on()

    pwm12.duty_ns(MIN)
    pwm14.duty_ns(MIN)
    pwm15.duty_ns(MIN)
    utime.sleep(1)

    pwm12.duty_ns(MID)    
    pwm14.duty_ns(MID)
    pwm15.duty_ns(MID)
    utime.sleep(1)
    
    pwm12.duty_ns(MAX)
    pwm14.duty_ns(MAX)
    pwm15.duty_ns(MAX)
    utime.sleep(1)
