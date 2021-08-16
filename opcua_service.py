import random
from time import sleep
from opcua import Server


server = Server()
server.set_endpoint("opc.tcp://127.0.0.1:12345")
server.register_namespace("Production Line 1")

objects = server.get_objects_node()
tempSensor = objects.add_object('ns=2;s="TS"', "Temperature Sensor")
tempSensor.add_variable('ns=2; s="TS_VendorName"', "TS Vendor Name", "Deloitte")
tempSensor.add_variable('ns=2; s="TS_SerialNumber"', "TS Serial Number", 1984)
temp = tempSensor.add_variable('ns=2; s="TS_Temperature"', "TS Temperature", 20)

temperature = 20.0
try:
    print("OPC-UA Service is starting")
    server.start()
    print("Service is running")
    while True:
        temperature += random.uniform(-1,1)
        temp.set_value(temperature)
        print("New Temperature: "+ str(temp.get_value()))
        sleep(2)
finally:
    server.stop()
    print("Service is stopped")