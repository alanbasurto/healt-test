import os
import sys

def check_reboot():
	"""comment"""
	return os.path.exists("/run/reboot-required")
	"""comment"""
		"""comment"""	"""comment"""
			"""comment"""
				"""comment"""

def main():
	if check_reboot():
		print("pending reboot")
		sys.exit(1)
	print("Everthing ok.")
	sys.exit(0)

main()
