import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time # Import the sleep function from the time module
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(14, GPIO.OUT, initial=GPIO.LOW) # Set pin 14 to be an output pin and set initial value to low (off)
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW) # Set pin 14 to be an output pin and set initial value to low (off)

def ledOneTwoBlink():
    
    
    GPIO.output(14, GPIO.HIGH) # Turn on
 
    time.sleep(1)
    GPIO.output(14, GPIO.LOW) # Turn on
 
    time.sleep(1)   
    GPIO.output(15, GPIO.HIGH) # Turn on
    
    time.sleep(1)

    GPIO.output(15, GPIO.LOW) # Turn on
    
    time.sleep(1)
    
def ledOneOn():
    
    
    GPIO.output(14, GPIO.HIGH) # Turn on
 
  
    
def ledOneOff():
    
    
 
    GPIO.output(14, GPIO.LOW) # Turn on
 

    
def ledTwoOn():
    
    

  
    GPIO.output(15, GPIO.HIGH) # Turn on
    

    
def ledTwoOff():
    
    


    GPIO.output(15, GPIO.LOW) # Turn on
    
 
    
def ledOneTwoQuickBlink():
    
    
    GPIO.output(14, GPIO.HIGH) # Turn on
 
    time.sleep(0.2)
    GPIO.output(14, GPIO.LOW) # Turn on
 
    time.sleep(0.2)   
    GPIO.output(15, GPIO.HIGH) # Turn on
    
    time.sleep(0.2)

    GPIO.output(15, GPIO.LOW) # Turn on
    
    time.sleep(0.2)
    GPIO.output(14, GPIO.HIGH) # Turn on
 
    time.sleep(0.2)
    GPIO.output(14, GPIO.LOW) # Turn on
 
    time.sleep(0.2)   
    GPIO.output(15, GPIO.HIGH) # Turn on
    
    time.sleep(0.2)

    GPIO.output(15, GPIO.LOW) # Turn on
    
    time.sleep(0.2)
    
    GPIO.output(14, GPIO.HIGH) # Turn on
 
    time.sleep(0.2)
    GPIO.output(14, GPIO.LOW) # Turn on
 
    time.sleep(0.2)   
    GPIO.output(15, GPIO.HIGH) # Turn on
    
    time.sleep(0.2)

    GPIO.output(15, GPIO.LOW) # Turn on
    
    time.sleep(0.2)
    
    GPIO.output(14, GPIO.HIGH) # Turn on
 
    time.sleep(0.2)
    GPIO.output(14, GPIO.LOW) # Turn on
 
    time.sleep(0.2)   
    GPIO.output(15, GPIO.HIGH) # Turn on
    
    time.sleep(0.2)

    GPIO.output(15, GPIO.LOW) # Turn on
    
    time.sleep(0.2)
    
    GPIO.output(14, GPIO.HIGH) # Turn on
 
    time.sleep(0.2)
    GPIO.output(14, GPIO.LOW) # Turn on
 
    time.sleep(0.2)   
    GPIO.output(15, GPIO.HIGH) # Turn on
    
    time.sleep(0.2)

    GPIO.output(15, GPIO.LOW) # Turn on
    
    time.sleep(0.2)
    
    GPIO.output(14, GPIO.HIGH) # Turn on
 
    time.sleep(0.2)
    GPIO.output(14, GPIO.LOW) # Turn on
 
    time.sleep(0.2)   
    GPIO.output(15, GPIO.HIGH) # Turn on
    
    time.sleep(0.2)

    GPIO.output(15, GPIO.LOW) # Turn on
    
    time.sleep(0.2)
    
    GPIO.output(14, GPIO.HIGH) # Turn on
 
    time.sleep(0.2)
    GPIO.output(14, GPIO.LOW) # Turn on
 
    time.sleep(0.2)   
    GPIO.output(15, GPIO.HIGH) # Turn on
    
    time.sleep(0.2)

    GPIO.output(15, GPIO.LOW) # Turn on
    
    time.sleep(0.2)
    
def ledOneBlink():
    
    
    GPIO.output(14, GPIO.HIGH) # Turn on
 
    time.sleep(0.2)
    GPIO.output(14, GPIO.LOW) # Turn on
 
    time.sleep(0.2)  

def ledTwoBlink():
    
    GPIO.output(15, GPIO.HIGH) # Turn on
    
    time.sleep(0.2)

    GPIO.output(15, GPIO.LOW) # Turn on
    
    time.sleep(0.2)        
    
#while True:
    #ledTwoBlink()