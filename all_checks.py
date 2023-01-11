import os
import sys

def check_reboot():
	"""just updating a commetn"""
	return os.path.exists("/run/reboot-required")


def main():
	if check_reboot():
		print("pending reboot")
		sys.exit(1)
	print("Everthing ok.")
	sys.exit(0)

main()
