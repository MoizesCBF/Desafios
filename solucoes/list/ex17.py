#!/usr/bin/env python3

# Funcao recursiva (Força Bruta) - Complexidade: Exponencial
def rec(c, at, mark, l, r, x, _max, _min, _sum):
	if _sum > r: return 0

	res = 0

	if _max - _min >= x and _sum >= l and _sum <= r:
		res += 1

	for i in range(at, len(c)):
		if mark[i]: continue

		res += rec(c, i + 1,  mark, l, r, x, max(_max, c[i]), min(_min, c[i]), _sum + c[i])

	return res


# Recebe os valores de entrada
n, l, r, x = [int(v) for v in input().split(' ')]
c = [int(i) for i in input().split(' ')]

# Cria a lista para nao repeticao
mark = [False for i in range(n)]

res = 0
# Chama a funcao recursiva
for i in range(n):
	mark[i] = True
	res += rec(c, i, mark, l, r, x, c[i], c[i], c[i])

print(res)