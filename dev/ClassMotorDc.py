class Motor:
    def __init__(self, pwm, in1, in2):
        self.in1 = in1
        self.in2 = in2
        self.pwm = pwm
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
    
    def forward(self, speed):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
        self.pwm.ChangeDutyCycle(speed)
    
    def backward(self, speed):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(speed)
    
    def stop(self):
        self.pwm.ChangeDutyCycle(0)