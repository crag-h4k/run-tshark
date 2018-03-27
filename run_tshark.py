from os import system
from time import sleep


def main():

	def print_net_interfaces():
		system("tshark -D")
		interface = input("which interface? Type name of interface, not number\n")
		return interface

	def run_it():
		run_interval = input("How often to run tshark, in seconds? 0 for no wait between captures\n")
		return run_interval


	def capture_num():
		packet_num = input("How many packets per cycle?\n")
		return packet_num

	#interface = print_net_interfaces()
	interface = "en0"
	#packet_num = capture_num()
	packet_num = str(100)
	#run_interval = run_it()
	run_interval = 0
	i = 0
	while True:
		fileName = "capture_" + str(i)
		tshark = "C:\\Program Files\\Wireshark\\tshark.exe"
		system("tshark -i " + interface +  " -T fields -e \"frame.time\" -e \"ip.src\" -e \"ip.dst\" -e \"tcp.srcport\" -e \"tcp.port\" -e \"tcp.dstport\" -c " + packet_num  + " -T ek > ./captures/" + fileName + ".json")
		print("Tshark capture: " + str(i))
		int(i)
		i += 1
		sleep(int(run_interval))

main()
exit()
