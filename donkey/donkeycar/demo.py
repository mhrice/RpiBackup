from donkeycar.vehicle import Vehicle
from donkeycar.parts.tofsensor import TOFSensorPart

V = Vehicle()

tof_sensor = TOFSensorPart(2)

V.add(tof_sensor, outputs=["tof/2"]

V.start()
