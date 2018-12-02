# if port can not br oppend test the ports on linux terminal with :
# python3 -m serial.tools.list_ports -v

from serial import Serial  # add Serial library for Serial communication
#identify arduino port
Arduino_Serial = Serial ('/dev/ttyACM0', 9600)  # Create Serial port object called arduinoSerialData
# print (ArduinoSerial.readline())  # read the serial data and print it as line

while True :  # infinite loop
    input_data = input("Enter the servo mode ")  # waits until user enters data

    if input_data == '1':  # if the entered data is 1
        Arduino_Serial.write(str.encode('1'))  # send 1 to arduino

    if input_data == '0':  # if the entered data is 0
        Arduino_Serial.write(str.encode('0'))  # send 0 to arduino
