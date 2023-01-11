import os
import sys

def check_reboot():
	"""just updating a commetn"""
	return os.path.exists("/run/reboot-required")

def check_disk_usage(disk,min_gb,min_percent):
	"""Returns True if there is enough free disk space, flase otherwhise"""
	du =shutil.disk_usage(disk)
	#calculate percentage of the free space
	percent_free = 100 * du.free / du.total
	gigabytes_free = du.free / 2**30
	if percent_free < min_percent or gigabytes_free < min_gb:
		return True
	return False

def main():
	if check_reboot():
		print("pending reboot")
		sys.exit(1)
	if  check_disk_usage(disk="/",min_gb=2,min_percent=10):
		print("ERROR: Not enough disk space")
		sys.extir(1)
	print("Everthing ok.")
	sys.exit(0)

main()
