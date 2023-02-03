a = int(input())
b = int(input())
if a % 10 == 0 or b % 10 == 0:
    print('YES')
else:
    print('NO')
'''
Проверим, что число a — положительное, а b — неотрицательное:

    if a > 0 and not (b < 0):

Или можно вместо not (b < 0) записать (b >= 0).

'''