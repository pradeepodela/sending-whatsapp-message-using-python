mport pywhatkit as kit
msg = input("enter what msg  you want send: ")
num = input("pls enter the number to whome you want to text: ")
hr = int(input ("pls enter at what time you want to deliver the txt (in hrs): "))
min = int(input("pls enter min: "))
kit.sendwhatmsg("+91"+num, msg, hr, min)
# to install:- pip install pywhatkit
