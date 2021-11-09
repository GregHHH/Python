import sys

def is_prime(nb):
	i = 2
	if (nb < 2):
		return 0
	while (i <= nb / i):
		if (nb / i * i == nb):
			return 0
		i = i + 1
	return 1

a = int(sys.argv[1])
print(is_prime(a))

