import random
from time import sleep
from opcua import Server


server = Server()
server.set_endpoint("opc.tcp://172.31.57.176:12345")
server.register_namespace("productionLine1")

objects = server.get_objects_node()
tempSensor = objects.add_object('ns=2;s="tempSensor"', "tempSensor")
tempSensor.add_variable('ns=2; s="vendorName"', "vendorName", "Deloitte")
tempSensor.add_variable('ns=2; s="serialNumber"', "serialNumber", 1984)
temp = tempSensor.add_variable('ns=2; s="temperature"', "temperature", 20)

temperature = 20.0
try:
    print("OPC-UA Service is starting")
    server.start()
    print("Service is running")
    while True:
        temperature += random.uniform(-1, 1)
        temp.set_value(temperature)
        print("New Temperature: " + str(temp.get_value()))
        sleep(2)
finally:
    server.stop()
    print("Service is stopped")