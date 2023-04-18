class Motor:
    def __init__(self, pin1, pin2):
        self.pin1 = pin1
        self.pin2 = pin2
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
    
    def forward(self, speed):
        GPIO.output(self.pin1, GPIO.HIGH)
        GPIO.output(self.pin2, GPIO.LOW)
        self.pwm = GPIO.PWM(self.pin1, 100)
        self.pwm.start(speed)
    
    def backward(self, speed):
        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.HIGH)
        self.pwm = GPIO.PWM(self.pin2, 100)
        self.pwm.start(speed)
    
    def stop(self):
        self.pwm.stop()