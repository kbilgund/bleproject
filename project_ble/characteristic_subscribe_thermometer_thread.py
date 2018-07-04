import gatt
import threading
import time

manager = gatt.DeviceManager(adapter_name='hci0')

connected=False
startRun=False

class AnyDevice(gatt.Device):

    def services_resolved(self):
        super().services_resolved()

        device_information_service = next(
            s for s in self.services
            if s.uuid == '00001809-0000-1000-8000-00805f9b34fb')

        temperature_characteristic = next(
            c for c in device_information_service.characteristics
            if c.uuid == '00002a1c-0000-1000-8000-00805f9b34fb')

        temperature_characteristic.enable_notifications()

    def characteristic_value_updated(self, characteristic, value):
        print("temperature:", value)

    def connect_succeeded(self):
        super().connect_succeeded()
        print("[%s] Connected" % (self.mac_address))
        connected = True

    def connect_failed(self, error):
        super().connect_failed(error)
        print("[%s] Connection failed: %s" % (self.mac_address, str(error)))
        connected = False 

    def disconnect_succeeded(self):
        super().disconnect_succeeded()
        print("[%s] Disconnected" % (self.mac_address))
        print(self.services)
        print(self.is_services_resolved())
        connected = False 
"""
    def services_resolved(self):
        super().services_resolved()

        print("[%s] Resolved services" % (self.mac_address))
        for service in self.services:
            print("[%s]  Service [%s]" % (self.mac_address, service.uuid))
            for characteristic in service.characteristics:
                print("[%s]    Characteristic [%s]" % (self.mac_address, characteristic.uuid))
"""

def connectThread():
	print("thread1") 
	while(1):
		print("thread1") 
		if(connected==False):
			device.connect()
		#	manager.stop()
			startRun = True
			time.sleep(2)
		else:
			time.sleep(2)

def connectThread2():
	print("thread2") 
	while(1):
		print("thread2") 
		if(startRun==True):
			manager.run()
		time.sleep(2)

mainThread = threading.Thread(target=connectThread,args=())
mainThread2 = threading.Thread(target=connectThread2,args=())
device = AnyDevice(mac_address='98:7b:f3:34:9b:66', manager=manager)

device.connect()
device.connect()
device.connect()
device.connect()

mainThread.start()
mainThread2.start()



