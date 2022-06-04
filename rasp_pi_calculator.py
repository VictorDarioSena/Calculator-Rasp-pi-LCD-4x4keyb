 
#import
from rasp_pi_calculator_function import *
import RPi.GPIO as GPIO
# import time
 

#set up of IO for LCD display and 4x4 keyboard  
peripherals_setup()
# Initialise display
lcd_init()
keybInit()
a=""
b=""
capture="E"
number1=[]
number2=[]
number3=[]
screenNumber1Sign=""
screenNumber2Sign=""
screenNumber3Sign=""
screenNumber1=""
screenNumber2=""
screenNumber3=""
memoryNumber1="0"
memoryNumber2="0"
operator='  '
operand1=0
operand2=0
operand3=0
memory1=0
memory2=0
useMemory=False
equalSign="   " 
numberOutput1=''
stage=0
signNumber1= False
signNumber1= False
refreshScreen=True
while True:

    
    a=readKeyb()        # read keyboard and update capture variable only if exist release between pushes
    if(a != b):    
        capture=a
        b = a 
        refreshScreen=True
    else:
        capture=""

    if(stage==0):

        if(len(capture) == 1 ):         #expected number 0 to 9,  "-"" sign or *1 memory1 *2 memory2
            number1.append(capture)
            stage=1
        if(capture == " - "):        
            screenNumber1Sign="-"
            stage=1

        if(useMemory):                  
            if(capture == "1"): 
                number1= list(char for char in str(memoryNumber1))
                stage=1  

            if(capture == "2"):
                number1=list(char for char in str(memoryNumber2))
                stage=1

        if(capture == " * "):
            useMemory=True
        

    elif(stage==1):                 #expected number 0 to 9, or operation sign
        
        if(len(capture) == 1):
            number1.append(capture)
            
            
        if(len(capture) == 3):        
            operator = capture
            stage=2

    elif(stage==2):                 #expected number 0 to 9, or - sign

        if(len(capture) == 1 ):
            number2.append(capture)
            stage=3
        if(capture == " - "):        
            screenNumber2Sign="-"
            stage=3

    elif(stage==3):                     #expected number 0 to 9, or = sign

        if(len(capture) == 1):
            number2.append(capture)
            
        if(len(capture) == 2):        
            equalSign = " = "
            stage=4

    elif(stage==4):                     #doing the singned math here
        if(screenNumber1Sign=="-"):
            operand1=float(screenNumber1)*(-1)
        else:
            operand1=float(screenNumber1)

        if(screenNumber2Sign=="-"):
            operand2=float(screenNumber2)*(-1)
        else:
            operand2=float(screenNumber2)

         


        if(operator == " + "):
            operand3=round(operand1+operand2,4)
        elif(operator == " - "): 
            operand3=round(operand1-operand2,4)
        elif(operator == " * "):
            operand3=round(operand1*operand2,4) 
        elif(operator == " / "):
            try:
                operand3=round(operand1/operand2,4)
            except ZeroDivisionError():
                operand3=80085

        memory2=memory1
        memory1=operand3
        memoryNumber1=str(memory1)
        memoryNumber2=str(memory2)       

        if(operand3<0):
            screenNumber3Sign="-"   
        else:
            screenNumber3Sign=""

        screenNumber3=str(abs(operand3))
        print(screenNumber3)
        refreshScreen=True
        stage=5

    elif(stage==5):
        if(capture=="C   "):
             stage=0   

    if(capture=="C   "):        #clear screen and variables to start over. memori 1 and memory 2 persists
        a=""
        b=""
        capture="E"
        number1=[]
        number2=[]
        number3=[]
        screenNumber1Sign=""
        screenNumber2Sign=""
        screenNumber3Sign=""
        screenNumber1=""
        screenNumber2=""
        screenNumber3=""
        operator='  '
        operand1=0
        operand2=0
        operand3=0
        useMemory=False
        equalSign="   " 
        numberOutput1=''
        stage=0


    

    if(refreshScreen):                  #refresh only when are new data to avoid Lcd flickering
        screenNumber1=(''.join(number1))
        screenNumber2=(''.join(number2))
     


        refresh_screen(screenNumber1Sign,screenNumber1,operator,screenNumber2Sign,screenNumber2,equalSign,screenNumber3Sign,screenNumber3,memoryNumber1,memoryNumber2)
        refreshScreen=False

 
    time.sleep(0.3)
 

 
