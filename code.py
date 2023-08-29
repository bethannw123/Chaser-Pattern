import board
import digitalio
import time

button=digitalio.DigitalInOut(board.GP10)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

button.value
print(button.value)

while True:
    if button.value == True:
       print("Button is not pressed.")
       time.sleep(.3)
    else:
        print("Button is pressed.")
        time.sleep(.3)
# Write your code here :-)
