#Proposto por @ezra#2037

# Recebe o inteiro n
n = int(input())

# Recebe a lista
lst = [int(v) for v in input().split(' ')]

# Pre-calcula os valores da lista
for i in range(1, n):
	lst[i] += lst[i - 1]

# Recebe o inteiro m
m = int(input())

for i in range(m):
	# Recebe os intervalos l e r
	l, r = [int(x) - 1 for x in input().split(' ')]
	
	res = lst[r] - (0 if l - 1 < 0 else lst[l - 1])
	print(res)