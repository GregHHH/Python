import sys

def pytacringe(arg1, arg2, arg3):
	if arg1 * arg1 == (arg2 * arg2) + (arg3 * arg3):
		print("c'est carré")
	elif arg2 * arg2 == (arg1 * arg1) + (arg3 * arg3):
		print("c'est carré")
	elif arg3 * arg3 == (arg1 * arg1) + (arg2 * arg2):
		print("c'est carré")
	else:
		print("pas carré")

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

pytacringe(a, b, c)