import VL53L1X

DEBUG = True

class TOFSensorPart(object):

	# Initialize the TOF sensor.
	def __init__(self, index):

                print("Initializing TOF Sensor...")
		# Initialize the i2c bus.
		self.sensor = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
		self.sensor.open()
		self.set_i2c_address(index)

		# 1 = Short Range, 2 = Medium Range, 3 = Long Range
		self.sensor.start_ranging(1)

		self.distance = 1000
		self.index = index

	# Since we're using multiple sensors, when the index
	# is different, reassign the i2c_address so we can
	# collect data from all the sensors at once.
	def set_i2c_address(self, index):
		address = 0x29
		if (index == 2):
			pass
		elif (index == 1):
			address = 0x2a
		else:
			address = 0x2b
		if (DEBUG) print("Address is: ", address)
		self.sensor.set_address(address)

	# Gather data from the TOF sensor.
	def poll(self):
		self.distance = self.sensor.get_distance()
		if (DEBUG) print("tof ", self.index, " distance: ", self.distance)
	
	# Run the part.
	def run(self):
		self.poll()
		return self.distance

	# Run threaded.
	def run_threaded(self):
		self.poll()
		return self.distance

	# Stop running the part & perform cleanup.
	def shutdown(self):
		self.sensor.stop_ranging()
		self.sensor.close()
