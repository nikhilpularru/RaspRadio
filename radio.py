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
