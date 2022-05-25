 
#import
from rasp_pi_calculator_function import *
import RPi.GPIO as GPIO
# import time
 

#set up of IO for LCD display and 4x4 keyboard  
peripherals_setup()
# Initialise display
lcd_init()
keybInit()
a=0
number1=[]
numberOutput1=''
while True:
    oldA=a
    a=readKeyb()
    if(( a != "E")and (a!=oldA)):
        lcd_string(str(a),LCD_LINE_1,1)
        number1.append(a)
        numberOutput1=''
        for x in number1:
            numberOutput1 +=''+ str(x)
        print(numberOutput1)
        
        lcd_string(numberOutput1,LCD_LINE_2,1)

    if(( a == "C") ):
        lcd_byte(0x01,LCD_CMD) # 000001 Clear display
        number1.clear()

    # Send some centred text
    # lcd_string("Rasbperry Pi",LCD_LINE_1,2)
    # lcd_string("16x2 LCD Test",LCD_LINE_2,2)
 
    # time.sleep(3) # 3 second delay
 
    # # Send some left justified text
    # lcd_string("1234567890123456",LCD_LINE_1,1)
    # lcd_string("abcdefghijklmnop",LCD_LINE_2,1)
 
    # time.sleep(3) # 3 second delay
 
    # # Send some right justified text
    # lcd_string("Raspberrypi-spy",LCD_LINE_1,3)
    # lcd_string(".co.uk",LCD_LINE_2,3)
 
    # time.sleep(3) # 20 second delay
 
    # # Send some centred text
    # lcd_string("Follow me on",LCD_LINE_1,2)
    # lcd_string("Twitter @RPiSpy",LCD_LINE_2,2)
 
    time.sleep(0.3)
 

 
