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
		print("here")
		x+=1
		fileName = "test" + str(x)
		tshark = "C:\\Program Files\\Wireshark\\tshark.exe"
		try:
			os.system("tshark -i Ethernet -T fields -e \"frame.time\" -e \"ip.src\" -e \"ip.dst\" -e \"tcp.srcport\" -e \"tcp.port\" -e \"tcp.dstport\" -c 10 -w" + fileName)
			print(x)
		except:
			print("tshark error")
			print(x)

tshark()
print(2+2)