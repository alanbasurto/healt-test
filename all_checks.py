import os
import sys
import shutil

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

def main():
	if check_reboot():
		print("pending reboot")
		sys.exit(1)
	if  check_root_full():
		print("Root partitiom full")
		sys.extir(1)
	print("Everthing ok.")
	sys.exit(0)

main()
