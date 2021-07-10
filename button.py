from gpiozero import Button
from time import sleep
import time

bBtn = Button(26, pull_up=False)
bBtnn = Button(16, pull_up=False)
pushbutton1 = ''
pushbutton2 = ''
endIt = 'NotEnded'
def waitforpushbutton():
    global pushbutton1, pushbutton2
    
    def buTest(but):
        global pushbutton1, pushbutton2
        #sleep(0.5) #adjust to your liking
        act = but.is_active
        if act:
            
            # long press action here , try to make this sleep a bit shorter
            print('Button {} pressed'.format(str(but.pin)))
            print('player1 button')
            pushbutton1 = 'on'
            pushbutton2 = 'off'
            
    def buTesty(but):
        global pushbutton2, pushbutton1
        #sleep(0.5) #adjust to your liking
        act = but.is_active
        if act:
            
            # long press action here , try to make this sleep a bit shorter
            print('Button {} pressed'.format(str(but.pin)))
            print('player2 button')
            pushbutton2 = 'on'
            pushbutton1 = 'off'
    
    bBtn.when_pressed = buTest
    bBtnn.when_pressed = buTesty

    
