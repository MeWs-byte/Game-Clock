# GameClock - a turn based timer
This is a pi zero based gameclock to keep track of time during the game of Go, chess, whatever you want a turn based timer for .

* Download this repo to your pi 
`git clone https://github.com/MeWs-byte/Game-Clock.git`
* Go into the folder
`cd Game-Clock`
* Install requirements
`sudo pip3 install -r requirements.txt`
* Run the program to test if everything works
`sudo python3 thready.py`

-Once the program is running you can input the time settings from a webserver on your local network running on the adress of your Pi Zero on port 5000

-http://THEIPOFYOURPI:5000

-Input time and game mode in the webserver and each press your button to end your turn. If your LED is burning it means that the current time being displayed is yours. If you want to end the game prematurely just tap the reset button in the web app. 

## What do I need to build it?

* 5641AS 7-segment display
* 8x 100 Ohm , 2 x 10k Ohm , 2 x 330 Ohm Resistors
* 2 LEDs
* 2 Pushbuttons
* Pi Zero
 

 [ Schematics can be found in the hardware folder to build your circuit. ](/hardware)
 
 
 ### EXTRA: 
 
 Personally I want the program to run every time the pi boots, let's run it as a systemd service!
 
 save configuration as 
`sudo nano /lib/systemd/system/gameclock.service`
* Paste this into the file:
 ```
[Unit]
Description=gameclock
After=network.target

[Service]
ExecStart=/usr/bin/python3 thready.py
WorkingDirectory=/home/pi/Game-Clock
StandardOutput=inherit
StandardError=inherit
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```
 
 * `sudo chmod 777 /lib/systemd/system/gameclock.service`
* `sudo systemctl daemon-reload`
* `sudo systemctl enable gameclock.service`
