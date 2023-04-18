#!/usr/bin/env python
from motor import setup
from motor import setSpeed
from motor import forward
from time import sleep


try:  
           
    setup()
    setSpeed(10)
    forward()
    #backward()
    
    # for value in range(10, 50):
        # print ('Set speed value: %d' % value)
        # setSpeed(value)
        # sleep(0.2)
        
    while True:    
            nn = input("Set speed value:")
            setSpeed(int(nn))
  
finally:                # this block will run no matter how the try block exits  
        exit                # clean up after yourself
