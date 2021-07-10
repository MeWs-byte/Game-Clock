#!/usr/bin/env python

import threading
import time
from segmentTimer import showTimer, showTimerb,showTimerc,showTimerd, endGame, showTimerc #, showTimerb
from datetime import datetime, timedelta
import flaskapp
import button
import blinky

lock = threading.Lock()



def flaskThread():
   
    while True:
        print("flask")
        flaskapp.flaskRunner()
        
        
        #lock.acquire()
        
        #lock.release()
        time.sleep(5) 

def logicThread():
    global gameTime, gameTimeB, gameStatus, pushbutton1, pushbutton2, endGame, endIt, newTime, newTimeb
    while True:
        print(flaskapp.gameTime)
        print(flaskapp.gameStatus)
        print(endGame)
        if endGame != 'True':
            
            if flaskapp.gameStatus == 'started' and button.pushbutton1 == 'on':
                showTimer(int(flaskapp.gameTime),00)
                #button.pushbutton1 = 'off'
                #button.pushbutton2 = 'on'
                
            if flaskapp.gameStatus == 'started' and button.pushbutton2 == 'on':
                showTimerb(int(flaskapp.gameTime),00)
                
            if flaskapp.gameStatus == 'startedB' and button.pushbutton1 == 'on':
                if button.newTime == 100000:
                
                    showTimerc(int(flaskapp.gameTimeB),00)
                    #button.pushbutton1 = 'off'
                    #button.pushbutton2 = 'on'
                    print(button.newTime)
                    print('thisis newtime ba')
                else:
                    m, s = divmod(button.newTime, 60)
                    
                    showTimerc(int(m),int(s))
                    
                      
            if flaskapp.gameStatus == 'startedB' and button.pushbutton2 == 'on':
                if button.newTimeb == 100000:
                    showTimerd(int(flaskapp.gameTimeB),00)                
                    #button.pushbutton1 = 'on'
                    #button.pushbutton2 = 'off'
                    print(button.newTimeb)
                    print('thisis newtime bb')
                else:
                    m, s = divmod(button.newTimeb, 60)
                    
                    showTimerd(int(m),int(s))                
            
            #if button.pushbutton2 == 'on' and flaskapp.gameStatus == 'started':
            #    showTimerb(int(flaskapp.gameTime),00)
                    
            #lock.acquire()
            #print(flaskapp.gameTime)
            #lock.release()
            time.sleep(0.001)   #0.00001   

def buttonThread():
    global gameTime, pushbutton1, pushbutton2
    while True:
        button.waitforpushbutton()
        
        print('pushbutton1',button.pushbutton1)
        print('pushbutton2',button.pushbutton2)
        #showTimer(0,11)
        time.sleep(1) 
        
def ledThread():
    global pushbutton1, pushbutton2, endIt
    while True:
        if button.pushbutton1 == 'on':
            blinky.ledOneOff()
            blinky.ledTwoOn()

        if button.pushbutton2 == 'on':

            blinky.ledOneOn()
            blinky.ledTwoOff() 
            
        if button.endIt == 'ended':
            blinky.ledOneTwoQuickBlink()
            time.sleep(1)  
            button.endIt = 'Clear'
            button.pushbutton2 = 'off'
            button.pushbutton1 = 'off'                 
        
            
        
        time.sleep(1) # 0.001

# create threads
thread1 = threading.Thread(target = flaskThread, args = ())
thread2 = threading.Thread(target = logicThread, args = ())
thread3 = threading.Thread(target = buttonThread, args = ())
thread4 = threading.Thread(target = ledThread, args = ())

# Starting the threads  
thread1.start() 
thread2.start() 
thread3.start() 
thread4.start() 
# Waiting for both the threads to finish executing 
thread1.join()
thread2.join()
thread3.join()
thread4.join()