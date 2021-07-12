# Retro Display 15min timer V2
# Tony Goodhew 29 April 2017
# a cat showed up and tweaked the code
 
# Import required libraries
import RPi.GPIO as GPIO
import time         
import button 
import blinky

#from flaskapp import gameStatus
endGame = 'False'
GPIO.setwarnings(False)
# Connections
#    A
#  F   B
#    G    Segment positions
#  E   C
#    D  dp
 
#Colour Br R  O  Y  G  Bl P G
#       A  B  C  D  E  F  G dp
LEDs = [11,4,23,8,7,10,18,25] #GPIO pins
#Colour W  Bk Br R
#       Th H  T  U
cols = [22,27,17,24]   #GPIO pins
 
# Tell GPIO library to use GPIO references
GPIO.setmode(GPIO.BCM)
# Setup LED pins as outputs
for x in range(8):
    GPIO.setup(LEDs[x], GPIO.OUT)
    GPIO.output(LEDs[x], 0)
# Setup col pins as output pins
for x in range(4):
    GPIO.setup(cols[x], GPIO.OUT)
    GPIO.output(cols[x], 0)
 
#one row per digit - 0 to 9
nums =[1,1,1,1,1,1,0,  # 0
       0,1,1,0,0,0,0,  # 1
       1,1,0,1,1,0,1,  # 2
       1,1,1,1,0,0,1,  # 3
       0,1,1,0,0,1,1,  # 4
       1,0,1,1,0,1,1,  # 5
       1,0,1,1,1,1,1,  # 6
       1,1,1,0,0,0,0,  # 7
       1,1,1,1,1,1,1,  # 8
       1,1,1,0,0,1,1]  # 9
 
def show_num(val,col,dp): #Displays one digit briefly
    for x in range(4): GPIO.output(cols[x],1)
    GPIO.output(cols[col], 0) # Turn col ON
    offset = val * 7
    for p in range(offset,offset + 7):
        x=p-offset
        if nums[p] == 1:
            GPIO.output(LEDs[x], 1)
        else:
            GPIO.output(LEDs[x], 0)
    # Decimal point needed?
    if dp == True:
        GPIO.output(LEDs[7], 1)
    else:
        GPIO.output(LEDs[7], 0)
    #time.sleep(0.000000000000000005) #temp delay 0,005
    time.sleep(0.005) #temp delay 0,005

    GPIO.output(cols[col], 1)  # Turn col off 
     
def show_number(val):  #Base 10
    digits =[0,0,0,0]
    abs_val = abs(val)
    temp_val = abs_val
    digits[0] = temp_val//1000
    temp_val = temp_val - digits[0] * 1000
    digits[1] = temp_val // 100
    temp_val = temp_val - digits[1] * 100
    digits[2] = temp_val // 10
    digits[3] = temp_val % 10
    for cycle in range(5):
        for col in range(4):
            show_num(digits[col],col,(col == 1))
 
# +++ Main +++
def showTimer(mins,sec):
    global pushbutton1, pushbutton2, newTime
    global gameStatus 
    global endGame
    #mins = 15
    #sec = 0
    n = mins * 100 + sec
    x = time.time()
    y = x + 1.0
    try:
        global pushbutton1, pushbutton2, endIt, newTime
        while mins > -1 and button.pushbutton1 == "on":
            print('this is n ')
            print(n)
            if n == 0:
                button.endIt = 'ended'
                button.pushbutton1 = 'off'
                button.pushbutton2 = 'off'
                gameStatus = 'ended'
                endGame = 'True'
                blinky.ledTwoBlink()
                
                print('game has ended, player 2 wins')
                
            while x < y:
                show_number(n)
                x = time.time()      
            sec = sec - 1
            button.newTime = n
            print(button.newTime)
            print('this is button.newTime just about this messsaaage')
            
            if (sec == -1):
                sec = 59
                mins = mins - 1
            
            n = mins * 100 + sec
            y = y + 1.0
        
        
        
    
    except KeyboardInterrupt:
        GPIO.cleanup()
    
   
        
    
    print('\nDone')
    
def showTimerb(mins,sec):
    global pushbutton1, pushbutton2, newTime
    global gameStatus   
    global endGame 
    #mins = 15
    #sec = 0
    n = mins * 100 + sec
    x = time.time()
    y = x + 1.0
    try:
        global pushbutton1, pushbutton2, endIt, newTime
        while mins > -1 and button.pushbutton2 == "on":
            if n == 0:
                button.endIt = 'ended'
                button.pushbutton1 = 'off'
                button.pushbutton2 = 'off'
                print('game has ended, player 2 wins')
                gameStatus = 'ended'
                endGame = 'True'   
                blinky.ledOneBlink()         
            print(n)
            while x < y:
                show_number(n)
                x = time.time()      
            sec = sec - 1
            button.newTime = n
            print(button.newTime)
            print('this is button.newTime just about this messsaaage')
                        
            if (sec == -1):
                sec = 59
                mins = mins - 1
            n = mins * 100 + sec
            y = y + 1.0
        
        
        
    
    except KeyboardInterrupt:
        GPIO.cleanup()

   
    print('\nDone')
   
   
   
def showTimerc(mins,sec):
    global pushbutton1, pushbutton2, newTime
    global gameStatus   
    global endGame 
    #mins = 15
    #sec = 0
    n = mins * 100 + sec
    x = time.time()
    y = x + 1.0
    try:
        global pushbutton1, pushbutton2, endIt, newTime
        while mins > -1 and button.pushbutton1 == "on":
            if n == 0:
                button.endIt = 'ended'
                button.pushbutton1 = 'off'
                button.pushbutton2 = 'off'
                print('game has ended, player 2 wins')
                gameStatus = 'ended'
                endGame = 'True'   
                blinky.ledOneBlink()         
            print(n)
            while x < y:
                show_number(n)
                x = time.time()      
            sec = sec - 1
            button.newTime = n
            print(button.newTime)
            print('this is button.newTime just about this messsaaage')
                        
            if (sec == -1):
                sec = 59
                mins = mins - 1
            n = mins * 100 + sec
            y = y + 1.0
        
        
        
    
    except KeyboardInterrupt:
        GPIO.cleanup()

   
    print('\nDone') 
    
def showTimerd(mins,sec):
    global pushbutton1, pushbutton2, newTimeb
    global gameStatus   
    global endGame 
    #mins = 15
    #sec = 0
    n = mins * 100 + sec
    x = time.time()
    y = x + 1.0
    try:
        global pushbutton1, pushbutton2, endIt, newTimeb
        while mins > -1 and button.pushbutton2 == "on":
            if n == 0:
                button.endIt = 'ended'
                button.pushbutton1 = 'off'
                button.pushbutton2 = 'off'
                print('game has ended, player 2 wins')
                gameStatus = 'ended'
                endGame = 'True'   
                blinky.ledOneBlink()         
            print(n)
            while x < y:
                show_number(n)
                x = time.time()      
            sec = sec - 1
            button.newTimeb = n
            print(button.newTimeb)
            print('this is button.newTimebbbbbbb just about this messsaaage')
                        
            if (sec == -1):
                sec = 59
                mins = mins - 1
            n = mins * 100 + sec
            y = y + 1.0
        
        
        
    
    except KeyboardInterrupt:
        GPIO.cleanup()

   
    print('\nDone') 
