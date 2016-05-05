import mraa

def getPrimaryBatteryVoltage():
	factor = .01611
	analogPin = mraa.Aio(3)
	voltage = factor*analogPin.read()
	return voltage

def getSecondaryBatteryVoltage():
	factor = .0182
	analogPin = mraa.Aio(4)
	voltage = factor*analogPin.read()
	return voltage

def test():
	print(getPrimaryBatteryVoltage())
	print(getSecondaryBatteryVoltage())

test()
