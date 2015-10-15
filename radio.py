import os
from nanpy import Arduino, Lcd

Arduino.pinMode(14, input)

# Setup the LCD pins for the Keypad Shield
lcd = Lcd([8,9,7,6,5,4],[16,2])

max_trax = 6                                    

def getKey():                                    # Function to Translate the analogRead values from the Keys to a Command
   val = Arduino.analogRead(14)
   if val == 1023:
      return "NONE"
   elif val < 100:
      return "RIGHT"
   elif val < 150:
      return "UP"
   elif val < 330:
      return "DOWN"
   elif val < 510:
      return "LEFT"
   elif val < 750:
      return "SEL"
   else:
      return "KBD_FAULT"


def getTrack():
   L= [S.strip('\n') for S in os.popen('mpc').readlines()]    # Get the Track info from the stdout of the mpc command
   station = L[0][0:15]                                                         # Pick out the Station and Track info
   track = L[0][-16:-1]
   lcd.printString(16*" ", 0, 0)                                            # Send it out to the LCD Display
   lcd.printString(station, 0, 0)
   lcd.printString(16*" ", 0, 1)
   lcd.printString(track, 0, 1)
   print L
   print station
   print track


os.system("mpc clear")
os.system("sudo amixer set PCM -- 80%")
os.system("mpc add http://icecast2.rte.ie/ieradio1")
os.system("mpc add http://76.73.3.245:6969")
os.system("mpc add http://listen.radionomy.com/the-smooth-lounge")
os.system("mpc add http://radionova128.media.vistatec.ie:80")
os.system("mpc add http://newstalk.fmstreams.com:8080")

track_num = 1                                                     # Start off on Track number 1
os.system("mpc play "+str(track_num))            # Tell the OS to Play it
getTrack()                                                  # Send the Track info to the LCD

while True:
   key = getKey()                                                    # Do something if a key was pressed
   if key == "RIGHT":
      track_num += 1
      if track_num > max_trax:
         track_num = max_trax
      os.system("mpc play " + str(track_num))
      getTrack()
   elif key == "LEFT":
      track_num -= 1
      if track_num < 1:
         track_num = 1
      os.system("mpc play " + str(track_num))
      getTrack()
   elif key == "SEL":
      os.system("mpc toggle")
      getTrack()
   elif key == "UP":
      os.system("sudo shutdown -h now")
