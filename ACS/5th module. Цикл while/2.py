a = int(input())
for i in range(a, 0, -1):
	if a > 2**i:
		print(i, 2**i)
		break

'Для заданного целого X найдите наибольшее целое число N, где 2^n меньше или равно X\
Напечатайте значение экмпоненты и результат выражения 2^n'