import shutil
import sys

def check_disk_usage(disk,min_absolute,min_percent):
	"""Returns True if there is enough free disk space, flase otherwhise"""
	du =shutil.disk_usage(disk)
	#calculate percentage of the free space
	percent_free = 100 * du.free / du.total
	gigabytes_free = du.free / 2**30
	if percent_free < min_percent or gigabytes_free < min_absolute:
		return False
	return True

if not check_disk_usage("/",2,10):
	print("ERROR: Not enough disk space")
	sys.extir(1)

print("Everything ok")
sys.exit(0)
