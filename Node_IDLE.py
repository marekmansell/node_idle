import serial
from time import sleep, time
from threading import Thread

def listener():
	# sleep(.5)
	# ser.write("import machine\n\r".encode())
	# sleep(.5)
	# ser.write("pin = machine.Pin(2, machine.Pin.OUT)\n\r".encode())
	# sleep(.5)
	# ser.write("pin.value(0)\n\r".encode())
	while True:
		out = input()
		out += "\r"
		out = out.encode()
		ser.write(out)


ser = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=.2)
ser.flushInput()
Thread(target=listener).start()



while True:
	a = []
	while not ser.inWaiting():
		sleep(.01)
	
	while ser.inWaiting():
		a.append(ser.read(1))
	# if a != [b"\n\r"]:
	print(b"".join(a).decode(), end="")

	# [print(ser.read(1).decode(), end="") for x in range(ser.inWaiting())]
