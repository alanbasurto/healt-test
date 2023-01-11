import os
import sys
import shutil
import socket

def check_reboot():
	"""just updating a commetn"""
	return os.path.exists("/run/reboot-required")

def check_disk_full(disk,min_gb,min_percent):
	"""Returns True if there is enough free disk space, flase otherwhise"""
	du =shutil.disk_usage(disk)
	#calculate percentage of the free space
	percent_free = 100 * du.free / du.total
	gigabytes_free = du.free / 2**30
	if gigabytes_free < min_gb or percent_free < min_percent:
		return True
	return False

def check_root_full():
		"""Returns true if the rooot partition is full, flase otherwise"""
		return check_disk_full(disk="/",min_gb=2,min_percent=10)

def check_no_network():
	"""Return True if it fails to resolve google's URL"""
	try:
		socket.gethostbyname("wwww.google.com")
		return False
	except:
		return True

def main():
	checks = [
		(check_reboot,"Pending Reboot"),
		(check_root_full,"Root partition full"),
		(check_no_network,"No working network")
	]
	everything_ok = True
	for check,msg in checks:
		if check():
			print(msg)
			everything_ok = False
	if not everything_ok:
		sys.exit(1)
		
	print("Everthing ok.")
	sys.exit(0)

main()
