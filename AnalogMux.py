import mraa

class AnalogMux:
	def __init__(self):
		self.sig = mraa.Aio(0)
		self.s0 = mraa.Gpio(15)
		self.s0.dir(mraa.DIR_OUT)
		self.s1 = mraa.Gpio(16)
		self.s1.dir(mraa.DIR_OUT)
		self.s2 = mraa.Gpio(17)
		self.s2.dir(mraa.DIR_OUT)

	def read(self, pin):
		self.s0.write(pin%2)
		self.s1.write((pin/2)%2)
		self.s1.write((pin/4)%2)
#		print ("pin: %d = %d %d %d" % (pin, pin%2, (pin/2)%2, (pin/4)%2))
		return self.sig.read()
