import mraa

class RelayBoard():

	def __init__(self):
		self.relays = 10* [0]
		self.relayPins = {1:9,2:10,3:11,4:12,5:13}
		for i in range(1,len(self.relayPins)):
			relay = mraa.Gpio(self.relayPins[i])
			self.relays[i]= relay
			self.relays[i].dir(mraa.DIR_OUT)
			self.relays[i].write(1)

	#Use this to configure a relay
	def setRelay(self,relay,value):
		# I logically NOT the value here because the relay board for some reason is
		# in it's on position at low voltage. I understand a relay to be on 
		# if the light is on.
		self.relays[relay].write(not value)

	# Use this to turn on and off two relays at the same time
	# Corresponds to switching a motor from it's primary controller
	# to it's secondary controller in the event of a fault	
	def setMotorOutput(self,motor,value):
		relayMotorDict = {1:(7,6), 2 : (5,4), 3: (3,2)}
		
		relays = relayMotorDict[motor]

		self.setRelay(relays[0],value)
		self.setRelay(relays[1],value)

if __name__ == "__main__":
	relayArray = RelayBoard()

	relayArray.setRelay(2,True)	
		
