import gatt

manager = gatt.DeviceManager(adapter_name='hci0')

class AnyDevice(gatt.Device):
    def services_resolved(self):
        super().services_resolved()

        device_information_service = next(
            s for s in self.services
            if s.uuid == '00001809-0000-1000-8000-00805f9b34fb')

        temperature_characteristic = next(
            c for c in device_information_service.characteristics
            if c.uuid == '00002a1e-0000-1000-8000-00805f9b34fb')

        temperature_characteristic.enable_notifications()

    def characteristic_value_updated(self, characteristic, value):
        print("temperature:", value)


device = AnyDevice(mac_address='98:7b:f3:34:9b:66', manager=manager)
device.connect()

manager.run()
