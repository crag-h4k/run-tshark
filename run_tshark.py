import os, time
def timer(func):
	def wrapper(*args,**kwargs):
		start = time.time()
		result = func(*args,**kwargs)
		end = time.time()
		print(func.__name__ +" took " + str((end-start)*1000) + "mil sec")
		return result
	return wrapper

@timer
def tshark():
	x=1
	while True:
		fileName = "test" + str(x)
		tshark = "C:\\Program Files\\Wireshark\\tshark.exe"
		os.system("tshark -i en0  -T fields -e \"frame.time\" -e \"ip.src\" -e \"ip.dst\" -e \"tcp.srcport\" -e \"tcp.port\" -e \"tcp.dstport\" -c 10 -w ./captures/" + fileName)
		print("Tshark capture: " + str(x))
		x += 1
tshark()
